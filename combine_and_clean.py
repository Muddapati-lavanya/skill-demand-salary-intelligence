import pandas as pd
import glob

# Get list of CSV files in data folder
csv_files = glob.glob('data/*.csv')

df_list = []

for file in csv_files:
    print(f"Loading {file}")
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Drop duplicates
combined_df = combined_df.drop_duplicates()

# Drop rows with missing salary or description
combined_df = combined_df.dropna(subset=['salary', 'description'])

# Keep only relevant columns (based on your CSVs)
columns_needed = ['title', 'description', 'salary', 'location']
combined_df = combined_df[columns_needed]

# Save combined clean dataset
combined_df.to_csv('data/clean_job_data.csv', index=False)

print("Combined and cleaned dataset saved to data/clean_job_data.csv")
