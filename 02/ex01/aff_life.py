from load_csv import load


df = load("life_expectancy_years.csv")
print(df)
france_data = df[df["country"] == "France"]
