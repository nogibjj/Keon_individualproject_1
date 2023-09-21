# IDS706-Individual Project 1

This project uses Continuous Integration/Continuous Development in Python script and Jupyter notebooks through Github Actions.

## Video Description

[Link](https://youtu.be/9PpnvsMWJpQ)

## Github Actions

Runs the several processes like `install` to automatically install packages from `requirements.txt` to `format`,`lint`,`test` my scripts and notebook and when passed creates the badges below.

[![Format](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/format.yml)

[![Lint](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/lint.yml)

[![OnInstall](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/install.yml)

[![Test](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Keon_individualproject_1/actions/workflows/test.yml) 

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
   
## Data

The [dataset](https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv)
is about about various cars `Models`, `Miles per gallon`, `Cylinders`, `Gear` `Horsepower`.

## Data Statistics

<img width="903" alt="Screenshot 2023-09-20 at 4 18 17 PM" src="https://github.com/nogibjj/Keon_individualproject_1/assets/125210401/4f2fe092-294e-4a00-afb0-d73f851d4c79">

  
## Visualisation 

A scatter plot is generated to compare the variables of Miles per Gallon and Horsepower

![output](https://github.com/nogibjj/IDS706_mini_project_2/assets/125210401/ce1cb228-d3f5-4888-a51a-845cee91a1b5)

<img width="598" alt="Screenshot 2023-09-20 at 4 21 20 PM" src="https://github.com/nogibjj/Keon_individualproject_1/assets/125210401/1d64e3ce-9bfb-4d7f-bac3-fc8ad193531e">

## Test_Scripts

includes test_script.py to test script and test_lib.py to test library

# Automation 

## Makefile 

Contains instructions for installing packages for installing code via `requirements.txt` 
   * `tests` - tests verifying csv input and verifying descriptive statistics output
   * `Formats`- Black
   * `lint` - Ruff

notebook, script and lib
 
## Requirements.txt

The requirements.txt file has a list of packages to be installed for any required project.

   * `polars==0.19.2`
   * `matplotlib==3.7.2`
   * `black==22.3.0`
   * `ruff==0.0.290`
   * `nbval==0.10.0`
   * `jupyter == 1.0.0`
   * `nbqa==1.7.0`


## devcontainer

The .devcontainer folder mainly contains two files -

- Dockerfile defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues

- devcontainer.json is a json file that specifies the environment variables including the installed extensions in the virtual environment

