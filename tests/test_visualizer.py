"""
Test script for time series visualization functions.

This script loads the dataset and runs all visualization functions
to verify they execute without errors.
"""

from src.time_series_visualizer import (
    load_and_clean_data,
    draw_line_plot,
    draw_bar_plot,
    draw_box_plot,
)

DATA_PATH = "data/raw/fcc-forum-pageviews.csv"


def run_all_tests():
    df = load_and_clean_data(DATA_PATH)

    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)

    print("All visualization functions executed successfully.")


if __name__ == "__main__":
    run_all_tests()
