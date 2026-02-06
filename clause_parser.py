import re

def split_into_clauses(text):
    if not text:
        return []

    # Remove table of contents header only
    text = re.sub(r'Table of contents.*?\n', '', text, flags=re.IGNORECASE)

    text = text.replace('\r', '\n')

    pattern = r'\n\s*(\d+(?:\.\d+)*[\)\.]?)\s+'
    parts = re.split(pattern, text)

    clauses = []
    buffer = ""

    for part in parts:
        if not part:
            continue  # Skip None or empty parts

        if re.match(r'^\d+(?:\.\d+)*[\)\.]?$', part.strip()):
            if buffer.strip():
                clauses.append(buffer.strip())
            buffer = ""
        else:
            buffer += " " + part

    if buffer.strip():
        clauses.append(buffer.strip())

    clean_clauses = [
        c.strip() for c in clauses
        if 40 < len(c.strip()) < 1500
    ]

    return clean_clauses