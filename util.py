import pandas as pd

PATH = R"C:\Users\DQQ\dOWNLOADS\athlete_events.csv"

def get_data(PATH):
    df = pd.read_csv(PATH)
    return df
# print(get_data(PATH))

def get_olympic_data():
    df = get_data(PATH)
    df["Medal"] = df["Medal"].fillna("NO INFO")
    medals = df[df["Medal"]!="NO INFO"].copy()
    medals = medals.groupby(["Team","Medal"])[["Team"]].count()
    medals.rename(columns={"Team":"Count"},inplace=True)
    medals.reset_index(inplace=True)
    medals.sort_values("Count",ascending=False, inplace=True)
    return medals.iloc[:20]

def get_countries():
    data = get_olympic_data()
    countries = list(set(data["Team"].tolist()))
    return countries

print(get_countries())