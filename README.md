# Chat with Customer Data (Generative AI Project)

## Project Overview

This project is an AI-powered tool that allows users to ask natural language questions about a customer dataset stored in an Excel file. The system uses Google Gemini API to understand user queries, converts them into structured filters, processes the data using Pandas, and returns accurate insights.

It works like a smart data analyst chatbot for real estate/customer leads.

---

##  Features

- Ask questions in natural language
- AI converts query into structured filters
- Works on Excel dataset
- Supports:
  - Count queries
  - Average calculations
  - Filtering by budget, location, property type
  - Data summaries
- Clean and readable output
- Streamlit-based UI (if used)

---

## Project Structure

chat-customer-data/
├── app.py                  # Streamlit frontend
├── main.py                 # Core logic (AI + data processing)
├── requirements.txt        # Dependencies
├── .env.example           # Example API key format
├── .gitignore             # Ignored files
├── data/
│   └── pune_real_estate_leads_updated.xlsx
└── README.md

---

## Installation Guide

### 1. Clone the repository
git clone https://github.com/SudarshanSM/chat-customer-data.git
cd chat-customer-data

---

### 2. Create virtual environment
python -m venv venv

Activate:
- Linux/Mac:
  source venv/bin/activate

- Windows:
  venv\Scripts\activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Setup environment variables

Create a `.env` file in the root folder:

GEMINI_API_KEY=your_api_key_here

---

### 5. Run the application
streamlit run app.py

---

## Example Queries

- How many customers have budget above 90 lakhs?
- List customers looking for 2BHK in Pune
- What is the average budget?
- Give summary of high-intent customers
- Show customers in Mumbai with budget below 50 lakhs

---

## How It Works

1. User enters a natural language question
2. Gemini API converts it into structured JSON
3. Pandas processes the Excel dataset
4. System performs:
   - Filtering / Counting / Averaging / Summarizing
5. Result is displayed in readable format

---

## Security Note

- API key is stored in `.env` file
- `.env` is excluded using `.gitignore`
- Each user must use their own Gemini API key

---

## Tech Stack

- Python
- Pandas
- Streamlit
- Google Gemini API
- OpenPyXL
- python-dotenv

---

## Future Improvements

- Add chatbot memory
- Support SQL database integration
- Improve UI dashboard
- Export results as PDF/Excel
- Multi-user analytics system

---

## 👨‍💻 Author

SudarshanSM  
Generative AI Internship Project
