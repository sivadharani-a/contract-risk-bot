risk_keywords = {
    "Penalty": ["penalty", "fine", "damages", "liable"],
    "Indemnity": ["indemnify", "hold harmless"],
    "Termination": ["terminate", "breach", "notice period"],
    "Auto Renewal": ["automatically renew", "auto-renew"],
    "Non-compete": ["non-compete", "restrict"],
    "IP Transfer": ["intellectual property", "assign ownership"]
}

def assess_clause_risk(clause):
    clause_lower = clause.lower()
    matched_types = []

    for rtype, words in risk_keywords.items():
        if any(w in clause_lower for w in words):
            matched_types.append(rtype)

    if not matched_types:
        return "Low", []

    if "Penalty" in matched_types or "Indemnity" in matched_types:
        return "High", matched_types

    return "Medium", matched_types


def overall_risk_score(results):
    score_map = {"Low": 1, "Medium": 2, "High": 3}
    total = sum(score_map[r["risk"]] for r in results)
    max_score = len(results) * 3
    return round((total / max_score) * 100, 2)