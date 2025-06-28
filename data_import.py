import pandas as pd

def load_faa_ntsb_data():
    url = "https://raw.githubusercontent.com/aaronraimist/FAA-Preliminary-Accident-and-Incident-Data/main/FAA-Accident-Incident-Data.csv"
    df = pd.read_csv(url)
    print("Sample FAA/NTSB Crash Data:")
    print(df.head())
    return df

if __name__ == "__main__":
    load_faa_ntsb_data() 