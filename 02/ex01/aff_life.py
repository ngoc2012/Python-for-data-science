import matplotlib.pyplot as plt
from load_csv import load

def main():
    df = load("life_expectancy_years.csv")
    print(df)
    france_data = df[df["country"] == "France"]
    # Convert columns to numeric years and corresponding values
    years = france_data.columns[1:].astype(int)  # Exclude the 'country' column
    values = france_data.iloc[0, 1:].astype(float)  # Row for France, exclude 'country'
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, label="France", color="#468fc1", linewidth=2)
    
    # Add labels, title, and legend
    plt.title("France Life Expectancy Projections", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    #plt.grid(True, linestyle="--", alpha=0.6)
    #plt.legend(fontsize=12)
    plt.tight_layout()
    
    # Show the plot
    plt.show()

if __name__ == '__main__':
    main()
