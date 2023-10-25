from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import DataFrame

from src.util.local import get_env_var_config, get_json_config
from src import functions
import sys

from ydata_profiling import ProfileReport
import sweetviz
import dtale

def run(snowpark_session: Session, eda_library: str) -> DataFrame:
    """
    Generate a new table from IRIS data with sepal and petal sizes in cm pairs.
    """

    # Get DATA table
    df = snowpark_session.read.table("DATA")

    # Profile the data
    print("Profiling data...")
    df_pd = df.toPandas()
    if eda_library == "ydata":
        profile = ProfileReport(df_pd, title="Pandas Profiling Report")
        profile.to_file("reports/ydata_profiling.html")
    elif eda_library == "sweetviz":
        report = sweetviz.analyze(df_pd)
        report.show_html("reports/sweetviz.html")
    elif eda_library == "dtale":
        d = dtale.show(df_pd, subprocess=False)
    else:
        raise ValueError("Invalid EDA library")


if __name__ == "__main__":

    # Args. with json or env vars 
    if (len(sys.argv) == 2 and sys.argv[1] == '-h') or len(sys.argv) != 3:
        print('Usage: python app.py <eda_library> [json_path]')
        print('If no json_path is provided, the script will attempt to use environment variables.')
        sys.exit(0)
    elif len(sys.argv) > 2:
        connection_parameters = get_json_config(sys.argv[2])
    else:
        connection_parameters = get_env_var_config()

    eda_library = sys.argv[1]

    print("Creating Snowpark session...")

    session = Session.builder.configs(connection_parameters).create()
    session.add_import(functions.__file__, 'src.functions')

    print("Running stored procedure...")
    run(session, eda_library=eda_library)

