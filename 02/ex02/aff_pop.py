import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("population_total.csv")
    data = df[df["country"] == "France"]
    years = data.columns[1:].astype(int)
    values = data.iloc[0, 1:].astype(float)

    plt.figure(figsize=(10, 6))
    plt.plot(years, values, label="France", color="#468fc1", linewidth=2)

    plt.xticks(range(1800, 2100, 40))
    plt.title("France Life expectancy Projections", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life expectancy", fontsize=12)
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    main()
