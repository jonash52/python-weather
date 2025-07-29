import pandas as pd
import os


def append_to_excel(new_data):
    df_new = pd.DataFrame([new_data])

    if os.path.exists("pogoda.xlsx"):
        df_existing = pd.read_excel("pogoda.xlsx")
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel("pogoda.xlsx", index=False)
    print("Zapisano do pliku EXCEL")