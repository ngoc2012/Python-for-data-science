import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def convert_income(value):
    """
    Function to convert population values to numeric
    """
    if value.endswith("B") or value.endswith("b"):
        return float(value[:-1]) * 1_000_000_000
    elif value.endswith("M") or value.endswith("m"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("K") or value.endswith("k"):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def main():
    """
    Main function to load data and plot population projections
    """
    df_life = load("life_expectancy_years.csv")
    print(df_life)
    df_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    print(df_income)
    dfs = [df_life, df_income]
    
    if not all(df is not None and not df.empty for df in dfs):
        print("Failed to load data.")
        return
    if not all("country" in df.columns for df in dfs):
        print("Missing 'country' column.")
        return

    year = 1900
    
    df_life_year = df_life[["country", str(year)]]
    df_income_year = df_income[["country", str(year)]]
    
    # Merge the data on 'country'
    combined_df = pd.merge(df_life_year, df_income_year, on="country", how="inner", suffixes=('_life', '_income'))

    print(combined_df)
    
    # Rename columns for clarity
    combined_df = combined_df.rename(columns={"1900_life": "Life Expectancy", "1900_income": "Income"})
    
    combined_df["Income"] = combined_df["Income"].apply(convert_income)

    combined_df["Life Expectancy"] = pd.to_numeric(combined_df["Life Expectancy"], errors='coerce')

    combined_df["Life Expectancy"] = combined_df["Life Expectancy"].fillna(combined_df["Life Expectancy"].median())
    combined_df["Life Expectancy"] = combined_df["Life Expectancy"].astype(float)

    
    print(combined_df)

    

    # Plotting life expectancy vs. income
    plt.figure(figsize=(8, 6))
    plt.scatter(combined_df["Income"], combined_df["Life Expectancy"], color="blue", alpha=0.6)
    
    plt.xscale('log')

    plt.title("Life Expectancy vs Income in " + str(year), fontsize=14)
    plt.xlabel("Income (PPP Adjusted)", fontsize=12)
    plt.ylabel("Life Expectancy (years)", fontsize=12)
    
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(
        lambda x,
        pos: f'{int(x / 1000)}k'
        ))

    plt.tight_layout()
    plt.show()

    # countries = ["Belgium", "France"]
    # for country in countries:
    #     if country not in df["country"].unique():
    #         print(f"{country} data not found.")
    #         return
    # filtered_df = df[df["country"].isin(countries)].set_index("country")

    # try:
    #     filtered_df.columns = filtered_df.columns.astype(int)
    # except ValueError:
    #     print("Error: Non-numeric columns detected in year columns.")
    #     return

    # filtered_df = filtered_df.loc[
    #     :,
    #     (filtered_df.columns >= 1800) & (filtered_df.columns <= 2050)
    #     ]

    # numeric_data = filtered_df.copy()
    # for col in numeric_data.columns:
    #     numeric_data[col] = numeric_data[col].map(convert_population)

    # colors = [
    #     "#2077b4",
    #     "#028002",
    #     "#1f77b4",  # Blue
    #     "#ff7f0e",  # Orange
    #     "#2ca02c",  # Green
    #     "#d62728",  # Red
    #     "#9467bd",  # Purple
    #     "#8c564b",  # Brown
    #     "#e377c2",  # Pink
    #     "#7f7f7f",  # Gray
    #     "#bcbd22",  # Yellow-green
    #     "#17becf"   # Cyan
    #     ]

    # if len(countries) > len(colors):
    #     for i in range(len(countries) - len(colors)):
    #         colors.append(colors[i % len(colors)])

    # # Transpose for plotting (years as index)
    # numeric_data = numeric_data.T

    # plt.figure(figsize=(8, 6))
    # for i, country in enumerate(numeric_data.columns):
    #     plt.plot(
    #         numeric_data.index,
    #         numeric_data[country],
    #         label=country,
    #         color=colors[i],
    #     )

    # plt.xticks(range(1800, 2050, 40))
    # plt.title("Population Projections", fontsize=12)
    # plt.xlabel("Year", fontsize=12)
    # plt.ylabel("Population", fontsize=12)

    # plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(
    #     lambda x,
    #     pos: f'{int(x / 1e6)}M'
    #     ))

    # plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))

    # plt.legend(
    #     loc='lower right',
    #     fontsize=12
    #     )
    # plt.tight_layout()

    # plt.show()


if __name__ == '__main__':
    main()
