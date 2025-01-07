from load_csv import load


# print(load("life_expectancy_years.csv"))

# invalid_file = "invalid.csv"
# with open(invalid_file, "w") as f:
#     f.write("not,a,csv,file\n")

# result = load(invalid_file)


header_file = "header_only.csv"
# with open(header_file, "w") as f:
#     f.write("country,1800,1801,1802\n")

result = load(header_file)

# Verify that the DataFrame is empty except for the column names
# self.assertIsInstance(result, pd.DataFrame)
# self.assertTrue(result.empty)  # Empty DataFrame has no rows
# self.assertListEqual(list(result.columns), ["country", "1800", "1801", "1802"])
