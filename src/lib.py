import polars as pl
import matplotlib.pyplot as plt


def stat_summary(df: pl.DataFrame, col: str):
    return df.describe()

def stat_mean(df: pl.DataFrame, col: str) -> float:
    return df[col].sum() / len(df[col])

def stat_median(df: pl.DataFrame, col: str) -> float:
    return df[col].median()

def stat_std(df: pl.DataFrame, col: str) -> float:
    return df[col].std()

def visualize_data(df):
    plt.scatter(df["mpg"], df["hp"])
    plt.xlabel("Miles Per Gallon")
    plt.ylabel("Horse Power")
    plt.title("Miles per gallon changes with automible weight")
    plt.show()

    #if not jupyter:
    visualization_path = '/workspaces/Keon_individualproject_1/output'
    plt.savefig(visualization_path)  # save png


def plot_hist(df, col):
    data = df[col]
    plt.hist(data, bins=5, edgecolor="k")

    plt.xlabel('Miles Per Gallon')
    plt.ylabel('Number of Cars')
    plt.title('Number of Cars')
    plt.show()

    
    # if not jupyter:
    visualization_path = '/workspaces/Keon_individualproject_1/output'
    plt.savefig(visualization_path)  # save png

# def save_plot(file_name, df):
#     visualize_data(df).savefig(
#         "pythonproject/figures/" + f"scatter_plot_{file_name}.png"
#     )

def data_csv(file_path):
    try:
        data = pl.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None


# if __name__ == '__main__':
#     cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
#     print(cars.head())
#     print(stat_mean(cars, 'mpg'))
#     print(stat_median(cars, 'mpg'))
#     print(stat_std(cars, 'mpg'))
#     print(stat_summary(cars, "mpg"))
#     visualize_data(cars)
