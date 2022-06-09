import pandas as pd

def clean_weather(df, columns):
    for c in columns:
        df[c].replace(["M", "T"], [0, 0.0001], inplace=True)
    return df