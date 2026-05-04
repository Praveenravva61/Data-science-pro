from src.DataSciencePro.components.data_validation import Data_validation
from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro import logger

STAGGING_NAME= "data_validation_stage"


class DataValidationPipeline:
     def __init__(self):
         pass
     def initiate_data_validation(self):
         
         config= ConfigurationManager()
         data_validation_config= config.get_data_validation_config()
         data_validation = Data_validation(config= data_validation_config)
         data_validation.validation_all_columns()
         
         
         
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
        object= DataValidationPipeline()
        object.initiate_data_validation()
        logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
 

