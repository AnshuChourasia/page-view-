import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'],index_col='date')

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
    ]

def draw_line_plot():
    # Draw line plot
    global df

    # Create a figure and plot the line chart
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    global df

    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month, then calculate the mean
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Reorder months to be calendar order
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_grouped = df_grouped[month_order]

    # Create the bar plot
    fig = df_grouped.plot(kind='bar', figsize=(12, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title='Months')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
        df_box = df.copy()
        df_box.reset_index(inplace=True)  # 'date' becomes a column

    # Create 'year' and 'month' columns
        df_box['year'] = df_box['date'].dt.year
        df_box['month'] = df_box['date'].dt.strftime('%b')  # Abbreviated month names
        df_box['month_num'] = df_box['date'].dt.month       # Numeric month for sorting

    # Sort the DataFrame by month number to ensure correct order in plots
        df_box = df_box.sort_values('month_num')

    # Set up the subplot grid
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

    # Year-wise Box Plot (Trend)
        sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
        axes[0].set_title("Year-wise Box Plot (Trend)")
        axes[0].set_xlabel("Year")
        axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot (Seasonality)
        sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
        axes[1].set_title("Month-wise Box Plot (Seasonality)")
        axes[1].set_xlabel("Month")
        axes[1].set_ylabel("Page Views")

        plt.tight_layout()
    # Save image and return fig (don't change this part)
        fig.savefig('box_plot.png')
        return fig
