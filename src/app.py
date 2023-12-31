"""
An example stored procedure. __main__ provides an entrypoint for local development
and testing.
"""

from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import col, DataFrame
from snowflake.snowpark.functions import udf

from src.util.local import get_env_var_config, get_json_config
from src import functions
import sys

def run(snowpark_session: Session) -> DataFrame:
    """
    A sample stored procedure which creates a small DataFrame, prints it to the
    console, and returns the number of rows in the table.
    """

    combine_udf = udf(functions.combine)

    schema = ["col_1", "col_2"]

    data = [
        ("Welcome to ", "Learn Snowpark!"),
        ("Learn more: ", "https://github.com/agr17/learn-snowpark"),
    ]

    df = snowpark_session.create_dataframe(data, schema)

    df2 = df.select(combine_udf(col("col_1"), col("col_2")).as_("hello_world")).sort(
        "hello_world", ascending=False
    )

    return df2


if __name__ == "__main__":

    # Args. with json or env vars
    if len(sys.argv) > 1 and sys.argv[1] == '-h':
        print('Usage: python app.py [json_path]')
        print('If no json_path is provided, the script will attempt to use environment variables.')
        sys.exit(0)
    elif len(sys.argv) > 1:
        connection_parameters = get_json_config(sys.argv[1])
    else:
        connection_parameters = get_env_var_config()

    session = Session.builder.configs(connection_parameters).create()
    session.add_import(functions.__file__, 'src.functions')

    print("Running stored procedure...")
    result = run(session)

    print("Stored procedure complete:")
    result.show()
