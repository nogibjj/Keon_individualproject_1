"We will use pytest to test our functions from src/lib.py"

import sys
import polars as pl
import matplotlib.pyplot as plt

sys.path.append("/workspaces/Keon_individualproject_1")

from src.lib import stat_mean,stat_median,stat_std,stat_summary
from src.lib import data_csv


def test_polars_descriptive_stat_mean():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    mean_mpg = stat_mean(cars, target_column)

    calculated_mean = cars[target_column].sum()/len(cars[target_column])
    assert mean_mpg == calculated_mean

def test_polars_descriptive_stat_median():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    median_mpg = stat_median(cars, target_column)

    calculated_median = cars[target_column].median()
    assert median_mpg == calculated_median

def test_polars_descriptive_stat_std():
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"
    std_mpg = stat_std(cars, target_column)

    calculated_std = cars[target_column].std()
    assert std_mpg == calculated_std

if __name__ == "__main__":
    test_polars_descriptive_stat_mean()
    test_polars_descriptive_stat_median()
    test_polars_descriptive_stat_std()
