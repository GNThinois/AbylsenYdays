import pandas as pd
import config
from sqlalchemy import create_engine

user = config.WAMP_username
pw = config.WAMP_password
db = config.WAMP_database


def upload_df_to_wamp(df):
    """
    Upload a pandas DataFrame to the WAMP database.

    Args:
        df (pandas.DataFrame): The DataFrame to be uploaded.
    """
    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine(f'mysql+pymysql://{user}:{pw}@localhost/{db}')

    # Upload the DataFrame to the 'job_offers' table in the database
    df.to_sql(name='job_offers', con=engine, if_exists='replace', index=False)


def fetch_data_from_wamp():
    """
    Fetch data from the 'job_offers' table in the WAMP database and return it as a pandas DataFrame.

    Returns:
        pandas.DataFrame: The fetched data as a DataFrame.
    """
    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine(f'mysql+pymysql://{user}:{pw}@localhost/{db}')

    # Fetch the data from the 'job_offers' table and store it in a DataFrame
    with engine.connect() as connection:
        query = "SELECT * FROM job_offers"
        df = pd.read_sql(query, connection)

    return df
