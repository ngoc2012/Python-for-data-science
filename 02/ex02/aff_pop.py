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

    if df is None:
        print("Failed to load data.")
        return
    if "country" not in df.columns:
        print("Missing 'country' column.")
        return

    countries = ["Belgium", "France"]
    for country in countries:
        if country not in df["country"].unique():
            print(f"{country} data not found.")
            return
    filtered_df = df[df["country"].isin(countries)].set_index("country")
    filtered_df.columns = filtered_df.columns.astype(int)

    print(filtered_df)
    numeric_data = filtered_df.copy()
    for col in numeric_data.columns:
        numeric_data[col] = numeric_data[col].map(convert_population)

    # Transpose for plotting (years as index)
    numeric_data = numeric_data.T

    plt.figure(figsize=(8, 6))
    for country in numeric_data.columns:
        plt.plot(numeric_data.index, numeric_data[country], label=country)

    plt.xticks(range(1800, 2050, 40))
    plt.xlim(1800, 2050)
    plt.title("Population Projections", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()

    plt.show()

    
    
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
