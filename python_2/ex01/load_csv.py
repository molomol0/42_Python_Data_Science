import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        loaded_data = pd.read_csv(path)
        return loaded_data
    except Exception as e:
        print("Exception error: couldn't load data file")
        exit (1)
