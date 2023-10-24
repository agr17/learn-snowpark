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
    Generate a new table from IRIS data with sepal and petal sizes in cm pairs.
    """

    combine_sizes = udf(functions.combine_sizes)

    # Get DATA table
    df = snowpark_session.read.table("DATA")

    # Create new table with sepal and petal sizes
    df2 = df.select(combine_sizes(col("SEPAL_LENGTH"), col("SEPAL_WIDTH")).as_("SEPAL_SIZE"),
                    combine_sizes(col("PETAL_LENGTH"), col("PETAL_WIDTH")).as_("PETAL_SIZE"),
                    col("CLASS").as_("SPECIES"))
    
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
