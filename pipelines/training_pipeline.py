from zenml import pipelines
from steps.ingest_data import ingest_df
from steps.cleaned_data import clean_df
@pipelines
def training_pipeline(data_path:str):

