import lib
import polars as pl

car = lib.data_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
print(car.head())

def run_descriptive_stats(df: pl.DataFrame, col: str) -> dict:
    "Runs descriptive statistics on the passed dataset"

    res = {
        'Target Column': col,
        'Mean': round(lib.stat_mean(df, col), 2),
        'Median': round(lib.stat_median(df, col), 2),
        'Standard Deviation': round(lib.stat_std(df, col), 2)
    }

    return res

print(lib.stat_mean(car, "mpg"))
print(lib.stat_median(car, "mpg"))
print(lib.stat_std(car, "mpg"))
print(lib.stat_summary(car, "mpg"))
lib.visualize_data(car)
