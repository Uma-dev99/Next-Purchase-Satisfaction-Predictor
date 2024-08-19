import logging
import pandas as pd
from zenml import  step

class IngestData:
    def __init__(self,data_path:str):
        self.data_path = data_path

    def get_data(self):
        logging.info("Ingest data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_df(data_path:str) -> pd.DataFrame:
    """
    Ingesting the data from data_path.
    Args:
        data_path: path of the data
    Returns:
        pd.Dataframe: the ingested data

    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data :{e}")
        raise e