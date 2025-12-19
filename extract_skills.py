import pandas as pd

# Load cleaned data
df = pd.read_csv('data/clean_job_data.csv')

# Define skills to look for
skills = ['Python', 'SQL', 'Excel', 'Power BI', 'Tableau']

def extract_skills(text):
    found_skills = []
    desc = str(text).lower()
    for skill in skills:
        if skill.lower() in desc:
            found_skills.append(skill)
    return ', '.join(found_skills)

# Extract skills from job description and title
df['skills'] = df['description'].apply(extract_skills)

# Save updated dataset
df.to_csv('data/clean_job_data_with_skills.csv', index=False)

print("Skills extracted and saved to data/clean_job_data_with_skills.csv")
