import pandas as pd

df = pd.read_csv('data/clean_job_data_with_skills.csv', encoding='latin1')

# rest of your code...


# Function to convert salary range string to average number
def avg_salary(s):
    if pd.isna(s):
        return None
    s = str(s).replace('$', '').replace(',', '').strip()
    if '-' in s:
        parts = s.split('-')
        try:
            low = float(parts[0].strip())
            high = float(parts[1].strip())
            return (low + high) / 2
        except:
            return None
    else:
        try:
            return float(s)
        except:
            return None

# Apply function to salary column
df['avg_salary'] = df['salary'].apply(avg_salary)

# Remove rows where salary could not be converted
df_clean = df.dropna(subset=['avg_salary'])

# Group by job title and calculate average salary
role_salary = df_clean.groupby('title')['avg_salary'].mean().reset_index()

# Save result to CSV for Power BI
role_salary.to_csv('data/role_salary.csv', index=False)

print("Role vs Salary data saved to data/role_salary.csv")
