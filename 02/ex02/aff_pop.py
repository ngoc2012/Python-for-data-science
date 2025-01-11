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


def data_collect(fn: str) -> pd.DataFrame:
    """
    Function to load data from a CSV file
    """
    df = load(fn)
    if df is None:
        print("Failed to load data.")
        return None
    if "country" not in df.columns:
        print("Missing 'country' column.")
        return None
    return df

def main():
    """
    Main function to load data and plot population projections
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

    try:
        filtered_df.columns = filtered_df.columns.astype(int)
    except ValueError:
        print("Error: Non-numeric columns detected in year columns.")
        return

    filtered_df = filtered_df.loc[
        :,
        (filtered_df.columns >= 1800) & (filtered_df.columns <= 2050)
        ]

    numeric_data = filtered_df.copy()
    for col in numeric_data.columns:
        numeric_data[col] = numeric_data[col].map(convert_population)

    numeric_data = numeric_data.T

    colors = [
        "#2077b4",
        "#028002",
        "#1f77b4",  # Blue
        "#ff7f0e",  # Orange
        "#2ca02c",  # Green
        "#d62728",  # Red
        "#9467bd",  # Purple
        "#8c564b",  # Brown
        "#e377c2",  # Pink
        "#7f7f7f",  # Gray
        "#bcbd22",  # Yellow-green
        "#17becf"   # Cyan
        ]

    if len(countries) > len(colors):
        for i in range(len(countries) - len(colors)):
            colors.append(colors[i % len(colors)])

    plt.figure(figsize=(8, 6))
    for i, country in enumerate(numeric_data.columns):
        plt.plot(
            numeric_data.index,
            numeric_data[country],
            label=country,
            color=colors[i],
        )

    plt.xticks(range(1800, 2050, 40))
    plt.title("Population Projections", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(
        lambda x,
        pos: f'{int(x / 1e6)}M'
        ))

    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))

    plt.legend(
        loc='lower right',
        fontsize=12
        )
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    main()
