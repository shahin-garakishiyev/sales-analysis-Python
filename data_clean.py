import pandas as pd

def clean_data(df):
    df["Sale_date"] = pd.to_datetime(df["Sale_date"], format="%d.%m.%Y")
    df["Weekday"] = df["Sale_date"].dt.day_name()
    df["Master_name"] = df["Master_name"].fillna("No Master")
    
    df["Day_type"] = df["Weekday"].apply(
        lambda x: "Weekend" if x in ["Saturday", "Sunday"] else "Weekday")
        
    return df