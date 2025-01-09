import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """
    Function to convert population values to numeric
    """
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("k"):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def main():
    """
    Main function
    """
    df = load("population_total.csv")
    print(df)
    # if df is None:
    #     print("Failed to load data.")
    #     return
    # if "country" not in df.columns:
    #     print("Missing 'country' column.")
    #     return
    # if "France" not in df["country"].unique():
    #     print("France data not found.")
    #     return
    # data = df[df["country"] == "France"]
    # try:
    #     years = data.columns[1:].astype(int)
    #     values = data.iloc[0, 1:].astype(float)
    # except Exception as e:
    #     print(f"An error occurred: {e}")

    # plt.figure(figsize=(8, 6))
    # plt.plot(years, values, label="France", color="#468fc1", linewidth=2)

    # plt.xticks(range(1800, 2100, 40))
    # plt.title("France Life expectancy Projections", fontsize=12)
    # plt.xlabel("Year", fontsize=12)
    # plt.ylabel("Life expectancy", fontsize=12)
    # plt.tight_layout()

    # plt.show()


if __name__ == '__main__':
    main()
