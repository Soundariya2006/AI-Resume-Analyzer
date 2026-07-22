def calculate_ats_score(text, skills):

    score = 0

    text = text.lower()

    if len(text) > 1000:
        score += 20

    if len(skills) >= 5:
        score += 20

    if "project" in text:
        score += 15

    if "education" in text:
        score += 15

    if "experience" in text:
        score += 15

    if "certification" in text or "certifications" in text:
        score += 15

    return min(score, 100)