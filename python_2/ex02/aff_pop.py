from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def find_country(data, country) -> pd.DataFrame:
    """
    Take a data set and a country to find
    Return the row of the country in the data
    """
    try:
        selected_country = data[data["country"] == country]
        if selected_country.empty:
            raise ValueError("Country not found")

        return selected_country

    except ValueError as e:
        print(f"Value error: {e}")
        exit(1)

    except Exception as e:
        print(f"Exception error: {e}")
        exit(1)


def print_graph(data, countries):
    """
    Take a data set and a tab of countries
    Print the data of the countries
    """
    try:
        for country in countries:
            country_data = find_country(data, country)
            population = country_data.drop(columns='country').iloc[0]
            population.index = population.index.astype(int)

            population = population.apply(lambda x: float(x.replace('M', '')))

            plt.plot(population.index, population.values, label=country)

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population (Millions)')
        plt.legend()

        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(20))

        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(40))
        plt.xlim(1800, 2050)

        plt.show()

    except Exception:
        print("Exception error")
        exit(1)


def main():
    """
    Load the data
    Print it's data of the wanted countries
    """
    countries_searched = ["France", "Belgium"]
    data = load("../population_total.csv")
    print_graph(data, countries_searched)


if __name__ == "__main__":
    main()
