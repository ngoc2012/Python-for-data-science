import matplotlib.pyplot as plt
from load_csv import load

def main():
    df = load("life_expectancy_years.csv")
    print(df)
    data = df[df["country"] == "France"]
    # Convert columns to numeric years and corresponding values
    years = data.columns[1:].astype(int)  # Exclude the 'country' column
    values = data.iloc[0, 1:].astype(float)  # Row for France, exclude 'country'
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, label="France", color="#468fc1", linewidth=2)
    
    plt.title("France Life expectancy Projections", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life expectancy", fontsize=12)
    plt.tight_layout()
    
    plt.show()

if __name__ == '__main__':
    main()
