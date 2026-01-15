"""
Time Series Visualization for freeCodeCamp Forum Page Views

This module provides functions to visualize daily page view data
using line plots, bar charts, and box plots to analyze trends,
seasonality, and distributions over time.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean_data(csv_path: str) -> pd.DataFrame:
    """
    Load and clean the freeCodeCamp forum page views dataset.

    Cleaning steps:
    - Parse dates
    - Set date as index
    - Remove extreme outliers (top and bottom 2.5%)

    Parameters
    ----------
    csv_path : str
        Path to the CSV dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe indexed by date.
    """
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    df = df[
        (df["value"] >= df["value"].quantile(0.025)) &
        (df["value"] <= df["value"].quantile(0.975))
    ]

    return df


def draw_line_plot(df: pd.DataFrame):
    """
    Draw a line plot showing daily forum page views over time.

    Returns
    -------
    matplotlib.figure.Figure
        Line plot figure.
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df["value"], color="red", linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views (2016–2019)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.tight_layout()
    plt.savefig("outputs/line_plot.png")

    return fig


def draw_bar_plot(df: pd.DataFrame):
    """
    Draw a bar plot showing average monthly page views per year.

    Returns
    -------
    matplotlib.figure.Figure
        Bar plot figure.
    """
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_bar.plot(kind="bar", figsize=(14, 7)).figure
    plt.xlabel("Year")
    plt.ylabel("Average Page Views")
    plt.legend(title="Month")

    plt.tight_layout()
    plt.savefig("outputs/bar_plot.png")

    return fig


def draw_box_plot(df: pd.DataFrame):
    """
    Draw box plots to visualize yearly trends and monthly seasonality.

    Returns
    -------
    matplotlib.figure.Figure
        Box plot figure.
    """
    df_box = df.copy().reset_index()
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        order=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.tight_layout()
    plt.savefig("outputs/box_plot.png")

    return fig
