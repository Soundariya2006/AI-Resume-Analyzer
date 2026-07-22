import pandas as pd

def extract_skills(text):

    skills = pd.read_csv(
        "skills.csv",
        header=None
    )[0].tolist()

    found = []

    text = text.lower()

    for skill in skills:

        if skill.lower() in text:

            found.append(skill)

    return found