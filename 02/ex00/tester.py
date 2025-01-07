from load_csv import load


# print(load("life_expectancy_years.csv"))

invalid_file = "invalid.csv"
with open(invalid_file, "w") as f:
    f.write("not,a,csv,file\n")

result = load(invalid_file)