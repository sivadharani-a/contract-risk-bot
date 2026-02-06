import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

def explain_clause(clause, risk, types):
    try:
        if client:
            prompt = f"""
Explain this contract clause in simple business language.

Clause:
{clause}

Risk Level: {risk}
Risk Types: {', '.join(types)}

Provide:
1. Simple explanation
2. Why it is risky
3. Suggest safer alternative wording
"""
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )
            return response.output_text
    except Exception:
        pass

    # 🔁 ALWAYS SHOW THIS IF AI FAILS
    if "Indemnity" in types:
        return "⚠️ This clause makes one party financially responsible for losses or damages. This can create serious financial risk if liability is unlimited."
    if "Penalty" in types:
        return "⚠️ This clause may impose financial penalties or damages. Review limits, caps, and conditions that trigger payment."
    if "Termination" in types:
        return "⚠️ This clause allows the contract to be ended under certain conditions. Check notice periods and financial consequences."
    return "⚠️ This clause contains legal or financial obligations that may carry risk."