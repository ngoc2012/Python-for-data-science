import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def convert_income(value: str) -> float:
    """
    Function to convert population values to numeric
    """
    try:
        if value.endswith("B") or value.endswith("b"):
            return float(value[:-1]) * 1_000_000_000
        elif value.endswith("M") or value.endswith("m"):
            return float(value[:-1]) * 1_000_000
        elif value.endswith("K") or value.endswith("k"):
            return float(value[:-1]) * 1_000
        else:
            return float(value)
    except (ValueError, AttributeError):
        print(f"Invalid income value: {value}")
        return None  # Return None for invalid values


def data_collect(fn_life:str, fn_income:str, year: str) -> pd.DataFrame:
    """
    Function to collect data
    """
    df_life = load(fn_life)
    df_income = load(fn_income)
    
    dfs = [df_life, df_income]

    if not all(df is not None and not df.empty for df in dfs):
        print("Failed to load data.")
        return None
    if not all("country" in df.columns for df in dfs):
        print("Missing 'country' column.")
        return None

    year = "1900"
    
    df_life_year = df_life[["country", year]]
    df_income_year = df_income[["country", year]]
    
    combined_df = pd.merge(df_life_year, df_income_year, on="country", how="inner", suffixes=('_life', '_income'))
    combined_df = combined_df.rename(columns={year + "_life": "Life Expectancy", year + "_income": "Income"})
    
    combined_df["Income"] = combined_df["Income"].apply(convert_income)

    combined_df = combined_df.dropna()

    combined_df["Life Expectancy"] = combined_df["Life Expectancy"].astype(float)

    return combined_df


def main():
    """
    Main function to load data and plot population projections
    """
    df = data_collect(
            "life_expectancy_years.csv",
            "income_per_person_gdppercapita_ppp_inflation_adjusted_data_error.csv",
            "1900"
            )

    if df is None:
        print("Failed to load data.")
        return

    # Plotting life expectancy vs. income
    plt.figure(figsize=(8, 6))
    plt.scatter(combined_df["Income"], df["Life Expectancy"], color="blue", alpha=0.6)
    
    plt.xscale('log')

    plt.title("Life Expectancy vs Income in " + year, fontsize=14)
    plt.xlabel("Income (PPP Adjusted)", fontsize=12)
    plt.ylabel("Life Expectancy (years)", fontsize=12)
    
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(
        lambda x,
        pos: f'{int(x / 1000)}k'
        ))

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
