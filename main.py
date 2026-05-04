from src.DataSciencePro import logger
from src.DataSciencePro.pipelines.data_ingestion import STAGGING_NAME, DataIngestionPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
    object= DataIngestionPipeline()
    object.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("Welcome to our custom logging data science Project")