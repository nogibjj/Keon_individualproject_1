"We will use pytest to test our functions from src/script_descriptive_stats.py:"
import sys

sys.path.append("/workspaces/Keon_individualproject_1")
sys.path.append("/workspaces/Keon_individualproject_1/src")
from src.main import run_descriptive_stats
import polars as pl


def test_descriptive_stats():
    "Test the descriptive stats function"
    data = pl.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    target_column = "mpg"

    results = run_descriptive_stats(data, target_column)

    assert 'Target Column' in results
    assert 'Mean' in results
    assert 'Median' in results
    assert 'Standard Deviation' in results
