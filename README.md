# Learn Snowpark

Learn Snowpark is a project aimed at acquiring proficiency in using Snowpark, a tool developed by Snowflake for running SQL queries in programming language environments like Python. This project is based on the official Snowflake-Labs template called 'snowpark-python-template' (https://github.com/Snowflake-Labs/snowpark-python-template).

The initial task accomplished in this project involved uploading the classic Iris dataset to Snowflake for analysis, a common dataset in the field of machine learning. Following this, a series of comprehensive tests and analyses were conducted, including:

- EDA (Exploratory Data Analysis): Extensive exploratory data analysis was performed using various tools such as [ydata_profiling](https://docs.profiling.ydata.ai/4.6/), [sweetviz](https://github.com/fbdesignpro/sweetviz), and [dtale](https://github.com/man-group/dtale). These tools were employed to gain valuable insights into the dataset, understand its characteristics, and identify patterns and trends in the data. The EDA process played a crucial role in preparing the data for further analysis and decision-making. 

## Setup

### JSON connector

The JSON connector has been developed by me so that I don't have to use environment variables. Simply create a *connection.json* file in the root of the project with the following format. 

````json
{
    "account"   : "<replace with your account identifer>",
    "user"      : "<replace with your username>",
    "password"  : "<replace with your password>",
    "role"      : "<replace with your role>",
    "warehouse" : "<replace with your warehouse>",
    "database"  : "<replace with your database>",
    "schema"    : "<replace with your schema>"
  }
````

Once we have it, we have to use the *get_json_config* function found in the *src/util/local.py* script.

### Enviroment variables 

Original connection mode of the template. Set the following environment variables with your Snowflake account information:

```bash
# Linux/MacOS
export SNOWSQL_ACCOUNT=<replace with your account identifer>
export SNOWSQL_USER=<replace with your username>
export SNOWSQL_ROLE=<replace with your role>
export SNOWSQL_PWD=<replace with your password>
export SNOWSQL_DATABASE=<replace with your database>
export SNOWSQL_SCHEMA=<replace with your schema>
export SNOWSQL_WAREHOUSE=<replace with your warehouse>
```

```powershell
# Windows/PowerShell
$env:SNOWSQL_ACCOUNT = "<replace with your account identifer>"
$env:SNOWSQL_USER = "<replace with your username>"
$env:SNOWSQL_ROLE = "<replace with your role>"
$env:SNOWSQL_PWD = "<replace with your password>"
$env:SNOWSQL_DATABASE = "<replace with your database>"
$env:SNOWSQL_SCHEMA = "<replace with your schema>"
$env:SNOWSQL_WAREHOUSE = "<replace with your warehouse>"
```

Optional: You can set this env var permanently by editing your bash profile (on Linux/MacOS) or 
using the System Properties menu (on Windows).

### Install dependencies

Create and activate a conda environment using [Anaconda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands):

```bash
conda env create --file environment.yml
conda activate snowpark
```

### Configure IDE

#### VS Code

Press `Ctrl`+`Shift`+`P` to open the command palette, then select **Python: Select Interpreter** and select the **snowpark** interpreter under the **Conda** list.

#### PyCharm

Go to **File** > **Settings** > **Project** > **Python Interpreter** and select the snowpark interpreter.

## Prereqs

- A Snowflake account
- Python 3.8 or greater
- An IDE or code editor (VS Code, PyCharm, etc.)
- Iris dataset: [https://archive.ics.uci.edu/dataset/53/iris](https://archive.ics.uci.edu/dataset/53/iris)

## Usage

Once you've set your credentials and installed the packages, you can test your connection to Snowflake by executing the stored procedure in [`app.py`](src/procs/app.py):

```bash
python src/app.py
```

You should see the following output:

```
------------------------------------------------------
|Hello world                                         |
------------------------------------------------------
|Welcome to Snowflake!                               |
|Learn more: https://www.snowflake.com/snowpark/     |
------------------------------------------------------
```

### EDA 

```bash
python src/eda.py <ydata | dtale | sweetviz> <connection.json>
```

### Run tests

You can run the test suite locally from the project root:

```bash
python -m pytest
```

## Docs

- [Snowpark Developer Guide for Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)
- [Creating Stored Procedures](https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-sprocs)
- [Snowpark API Reference](https://docs.snowflake.com/developer-guide/snowpark/reference/python/index.html)

## Contributing

Have an idea for an improvement? Fork this repository and open a PR with your idea!
