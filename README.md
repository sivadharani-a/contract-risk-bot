🧠 GenAI Contract Risk Analysis Assistant for SMEs

This project is a GenAI-powered legal assistant that helps small and medium businesses understand legal risks in contracts using Natural Language Processing (NLP) and AI.

The system analyzes uploaded contracts, detects potentially risky clauses, assigns risk levels, and explains legal terms in plain business language.

🚀 Features

📄 Upload contracts in PDF, DOCX, or TXT format

✂️ Automatic clause segmentation

🧠 Named Entity Recognition (NER) for legal elements

⚖️ Detection of legal risk types:

Indemnity clauses

Penalty clauses

Termination terms

Liability-related conditions

Non-compete & IP transfer references

📊 Clause-level risk classification (Low / Medium / High)

🧮 Overall contract risk score

💬 Plain-language explanations of risky clauses using GenAI

🔁 Built-in fallback explanations if AI service is unavailable

🏗️ System Architecture
User Upload
   ↓
Text Extraction (PDF/DOCX/TXT)
   ↓
Clause Segmentation
   ↓
NER + Legal Risk Detection
   ↓
Risk Scoring Engine
   ↓
Explanation Engine (AI + Fallback)
   ↓
Streamlit Dashboard
🛠️ Tech Stack

Python

Streamlit (Web UI)

spaCy (NLP processing)

OpenAI GPT (Legal explanation generation)

pdfplumber / python-docx (Text extraction)

🎯 Problem Solved

Legal contracts are often complex and difficult for small businesses to interpret. This tool helps SMEs:

✔ Identify legal risks before signing agreements
✔ Understand contract clauses in simple language
✔ Make more informed business decisions
✔ Reduce dependence on immediate legal consultation

🔒 Security Note
API keys and sensitive credentials are never displayed in the application.

Ensure your OpenAI API key is stored securely as an environment variable:

OPENAI_API_KEY=your_key_here
▶️ Running Locally
pip install -r requirements.txt
streamlit run app.py

📌 Future Enhancements

Multilingual contract support
Downloadable legal risk reports
Clause similarity comparison with standard templates

👨‍💻 Developed For

Career Carnival 2026 Hackathon – Data Science Round
GenAI + Legal NLP Use Case
