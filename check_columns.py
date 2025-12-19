import pandas as pd
import glob

csv_files = glob.glob('data/*.csv')

for file in csv_files:
    df = pd.read_csv(file)
    print(f"Columns in {file}:")
    print(df.columns.tolist())
    print('-'*40)
