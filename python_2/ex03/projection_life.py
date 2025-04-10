from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def format(x, _):
    if x >= 1_000:
        return f'{x / 1_000:.0f}k'
    else:
        return str(int(x))


def scatter_1900(metric_df, pop_df):
    try:
        pop_df = pop_df.set_index('country')
        metric_df = metric_df.set_index('country')

        x_vals = []  # Population
        y_vals = []  # Metric
        labels = []

        for country in pop_df.index:
            if country in metric_df.index:
                metric_value = metric_df.at[country, '1900']
                pop_value = pop_df.at[country, '1900']

                if pd.isna(metric_value) or pd.isna(pop_value):
                    continue

                if isinstance(pop_value, str):
                    if 'k' in pop_value:
                        pop_value = float(pop_value.replace('k', '')) * 1_000
                    else:
                        pop_value = float(pop_value)

                x_vals.append(float(pop_value))
                y_vals.append(float(metric_value))
                labels.append(country)

        # plt.figure(figsize=(10, 6))
        plt.scatter(x_vals, y_vals, alpha=0.7)

        plt.xscale('log')
        plt.xticks([300, 1_000, 10_000])
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format))

        plt.xlim(300, 10_500)
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format))
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expentancy')
        plt.title('1900')

        # Apply human-readable formatting to x-axis now (Population)
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format))

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error:", e)


def main():
    data = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data2 = load("../life_expectancy_years.csv")
    scatter_1900(data2, data)


if __name__ == "__main__":
    main()
