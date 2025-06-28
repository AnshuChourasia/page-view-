import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    
    df = pd.read_csv("epa-sea-level.csv")
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces

# Now this won't crash:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    

    result_all = linregress(df['year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = result_all.slope * x_all + result_all.intercept
    ax.plot(x_all, y_all, 'r', label='Best Fit: All Data')

    df_recent = df[df['year'] >= 2000]
    result_recent = linregress(df_recent['year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = result_recent.slope * x_recent + result_recent.intercept
    ax.plot(x_recent, y_recent, 'green', label='Best Fit: 2000 onward')

    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()
    ax.grid(True)

    fig.savefig("sea_level_plot.png")
    print("Saved as sea_level_plot.png")

draw_plot()




