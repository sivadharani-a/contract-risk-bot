def explain_clause(clause, risk, types):
    prompt = f"""
    You are a legal assistant. Explain this contract clause in simple business language.

    Clause:
    {clause}

    Risk Level: {risk}
    Risk Types: {', '.join(types)}

    Provide:
    1. Simple explanation
    2. Why this could be risky
    3. Suggest safer alternative wording
    """

    # Call GPT/Claude API here
    return response_text