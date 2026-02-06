import streamlit as st
from extractor import extract_text
from clause_parser import split_into_clauses
from risk_engine import assess_clause_risk, overall_risk_score
import os

st.write("API Key Loaded:", os.getenv("OPENAI_API_KEY") is not None)
st.title("📄 Contract Risk Analysis Bot")

file = st.file_uploader("Upload a contract", type=["pdf", "docx", "txt"])

if file:
    text = extract_text(file)
    clauses = split_into_clauses(text)

    results = []
    for c in clauses:
        risk, types = assess_clause_risk(c)
        results.append({"clause": c, "risk": risk, "types": types})

    score = overall_risk_score(results)
    st.metric("Overall Contract Risk Score", f"{score}/100")
    st.subheader("Contract Summary")

    st.write(f"""
    This contract contains **{len(results)} clauses**.

    Overall Risk Score: **{score}/100**

    High Risk Clauses: **{sum(1 for r in results if r['risk']=='High')}**  
    Medium Risk Clauses: **{sum(1 for r in results if r['risk']=='Medium')}**
    """)
    st.subheader("Clause Analysis")

    for r in results:
        if r["risk"] == "High":
            st.error("High Risk Clause")
        elif r["risk"] == "Medium":
            st.warning("Medium Risk Clause")
        else:
            st.success("Low Risk Clause")

        st.write(r["clause"])

        if r["types"]:
            st.caption(f"Detected: {', '.join(r['types'])}")

        from llm_engine import explain_clause

        if r["risk"] != "Low":
            explanation = explain_clause(r["clause"], r["risk"], r["types"])
            st.info(explanation)