from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def format(x, _):
    """
    Format ticker to 1000 = 1k
    """
    if x >= 1_000:
        return f'{x / 1_000:.0f}k'
    else:
        return str(int(x))


def scatter_1900(income, population):
    """
    Take two data set
    Put values of 1900 in a list
    Print the lists on a graph
    """
    try:
        population = population.set_index('country')
        income = income.set_index('country')

        x_vals = []
        y_vals = []

        for country in population.index:
            if country in income.index:
                income_value = income.at[country, '1900']
                popu_value = population.at[country, '1900']

                if pd.isna(income_value) or pd.isna(popu_value):
                    continue

                if isinstance(popu_value, str):
                    if 'k' in popu_value:
                        popu_value = float(popu_value.replace('k', '')) * 1_000
                    else:
                        popu_value = float(popu_value)

                x_vals.append(float(popu_value))
                y_vals.append(float(income_value))

        plt.scatter(x_vals, y_vals, alpha=0.7)

        plt.xscale('log')
        plt.xticks([300, 1_000, 10_000])
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format))

        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expentancy')
        plt.title('1900')

        plt.show()

    except Exception as e:
        print("Error:", e)


def main():
    """
    Load the two data set
    Print the wanted data
    """
    data = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data2 = load("../life_expectancy_years.csv")
    scatter_1900(data2, data)


if __name__ == "__main__":
    main()
