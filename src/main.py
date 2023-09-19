import lib

car = lib.data_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
print(car.head())

print(lib.stat_mean(car, "mpg"))
print(lib.stat_median(car, "mpg"))
print(lib.stat_std(car, "mpg"))
print(lib.stat_summary(car, "mpg"))
lib.visualize_data(car)
lib.plot_hist(car, "mpg")