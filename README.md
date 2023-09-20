# IDS706-Individual Project 1

[![Format](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/format.yml)

[![Lint](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/lint.yml)

[![OnInstall](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/install.yml)

[![Test](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/test.yml) 


## Purpose 

The purpose of this project is using Pandas to load a dataframe. I used a `pd.DataFrame` as a sample data and test its descriptions using the function `pandas_descriptive_stats_*()`. 
The visualization on a scatter plot.

## Jupyter Notebook 
 * Contains cells that perform descriptive statistics using `Polars`.
 * Tested by using `nbval plugin`.
   
## Python Script 

 * Performs the same descriptive statistics using `Polars`.

## lib.py 

 * file that shares the common functions between the Python Script and Jupyter Notebook such as:
   `stat_summary()`
   ` stat_mean()`
   ` stat_std()`
   ` stat_median`
   ` visualize_data`
   `plot_hist`
   `data_csv`
 
## Makefile 

Runs `installs` code via `requirements.txt` whivh also `tests`, `Formats`,`lint` notebook, script and lib


The [dataset](https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv)
 is about about various cars `Models`, `Miles per gallon`, `Cylinders`, `Gear` etc...

test_script.py to test script
test_lib.py to test library
GitHub Actions performs all four Makefile commands with badges for each one in the README.md

  
## Visualisation 

A scatter plot is generated to compare the variables of Miles per Gallon and Horsepower

![output](https://github.com/nogibjj/IDS706_mini_project_2/assets/125210401/ce1cb228-d3f5-4888-a51a-845cee91a1b5)


![output](https://github.com/nogibjj/Keon_individualproject_1/assets/125210401/86cdd849-f14d-49d6-b5b0-24469655845d)


## Automation 

used takes into Consideration

## 1. devcontainer

The .devcontainer folder mainly contains two files -

Dockerfile defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
devcontainer.json is a json file that specifies the environment variables including the installed extensions in the virtual environment

## 2. Makefile

The Makefile contains instructions for installing packages (specified in requirements.txt), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term 'Check...' ), and linting the code using pylint


## 3. GitHub Actions
  
Github Actions uses the main.yml file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions
  
## 4. Requirements.txt

The requirements.txt file has a list of packages to be installed for any required project. Currently, my requirements file only contains generic python packages, more specific packages can and will be added depending on scope of projects over time.
