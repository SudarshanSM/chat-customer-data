import os
import json
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

# =========================
# 🔑 LOAD API KEY SAFELY
# =========================
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")


# =========================
# 📊 LOAD DATASET
# =========================
def load_data():
    df = pd.read_excel("data/pune_real_estate_leads_updated.xlsx")
    return df


# =========================
# 🧠 CONVERT QUESTION → JSON
# =========================
def parse_question(question):
    prompt = f"""
    Convert this question into structured JSON for filtering real estate data.

    Question: {question}

    Return ONLY JSON in this format:
    {{
        "operation": "count/filter/average/summary",
        "filters": {{
            "budget": "above 90L / below 50L / null",
            "property_type": "2BHK / 3BHK / null",
            "location": "city or null"
        }}
    }}
    """

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except:
        return {
            "operation": "unknown",
            "filters": {}
        }


# =========================
# 🔍 FILTER DATA
# =========================
def filter_data(df, filters):
    result = df

    # Budget filter
    if "Budget" in df.columns and filters.get("budget"):
        value = filters["budget"]

        try:
            if "above" in value:
                num = int(value.split("above")[1].replace("L", "").strip())
                result = result[result["Budget"] > num]

            elif "below" in value:
                num = int(value.split("below")[1].replace("L", "").strip())
                result = result[result["Budget"] < num]
        except:
            pass

    # Property Type filter
    if "Property Type" in df.columns and filters.get("property_type"):
        result = result[result["Property Type"] == filters["property_type"]]

    # Location filter
    if "Location" in df.columns and filters.get("location"):
        result = result[result["Location"] == filters["location"]]

    return result


# =========================
# 📈 COMPUTE ANSWER
# =========================
def compute_answer(df, operation):

    if operation == "count":
        return f"Total Leads: {len(df)}"

    elif operation == "average" and "Budget" in df.columns:
        return f"Average Budget: {df['Budget'].mean():.2f} Lakhs"

    elif operation == "filter":
        return df.to_string(index=False)

    elif operation == "summary":
        return f"""
📊 Total Leads: {len(df)}
📌 Columns: {list(df.columns)}

🔎 Sample Data:
{df.head(5).to_string(index=False)}
"""

    return df.to_string(index=False)


# =========================
# 🚀 MAIN PIPELINE FUNCTION
# =========================
def process_query(question):
    df = load_data()

    parsed = parse_question(question)

    filtered_df = filter_data(df, parsed.get("filters", {}))

    result = compute_answer(filtered_df, parsed.get("operation"))

    return result