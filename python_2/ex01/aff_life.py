from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def find_country(data, country) -> pd.DataFrame:
    """
    Take a data set and a country to find
    Return the row of the country in the data
    """
    try:
        selected_country = data[data["country"] == country]
        if selected_country.empty:
            raise ValueError("Country not found")

        return (selected_country)

    except ValueError as e:
        print(f"Value error: {e}")
        exit(1)

    except Exception as e:
        print(f"Exception error: {e} # Get first row (as Series)")
        exit(1)


def print_graph(data):
    """
    Take a data set
    Print the data in a graph
    """
    population = data.drop(columns='country').iloc[0]

    population.index = population.index.astype(int)

    population.plot(kind='line', title='France Life Expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.grid(True)
    plt.show()


def main():
    """
    Load the data
    Isolate the country wanted
    Print it's data
    """
    country_searched = 'France'
    data = load("../life_expectancy_years.csv")
    country = find_country(data, country_searched)
    print_graph(country)


if __name__ == "__main__":
    main()
