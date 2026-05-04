from src.DataSciencePro.components.data_ingestion import DataIngestion
from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro import logger


STAGGING_NAME= "data_ingestion_stage"

class DataIngestionPipeline:
     def __init__(self):
         pass
     def initiate_data_ingestion(self):
         config= ConfigurationManager()
         data_ingestion_config= config.get_data_ingestion_config()
         data_ingestion = DataIngestion(config= data_ingestion_config)
         data_ingestion.download_file()
         data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
        object= DataIngestionPipeline()
        object.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
        