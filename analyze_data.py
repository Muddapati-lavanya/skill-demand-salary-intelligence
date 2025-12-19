import pandas as pd
import re

def parse_salary(salary_str):
    salary_str = str(salary_str).replace('$', '').replace(',', '').strip()
    numbers = re.findall(r'\d+\.?\d*', salary_str)
    if not numbers:
        return None
    numbers = list(map(float, numbers))
    if len(numbers) == 1:
        return numbers[0]
    else:
        return sum(numbers) / len(numbers)

# Load data
df = pd.read_csv('data/clean_job_data_with_skills.csv')

# Clean salary column
df['salary'] = df['salary'].apply(parse_salary)

# Drop rows where salary couldn't be converted
df = df.dropna(subset=['salary'])

# Explode skills into separate rows
df_skills = df.assign(skills=df['skills'].str.split(', ')).explode('skills')

# Count jobs per skill
skill_counts = df_skills['skills'].value_counts()
print("Job counts per skill:")
print(skill_counts)

# Average salary per skill
skill_salary = df_skills.groupby('skills')['salary'].mean().sort_values(ascending=False)
print("\nAverage salary per skill:")
print(skill_salary)

# Job counts by location
location_counts = df['location'].value_counts()
print("\nJob counts by location:")
print(location_counts)
