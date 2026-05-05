from src.DataSciencePro import logger
from src.DataSciencePro.pipelines.data_ingestion_pipeline import STAGGING_NAME, DataIngestionPipeline
from src.DataSciencePro.pipelines.data_validation_pipeline import STAGGING_NAME, DataValidationPipeline
from src.DataSciencePro.pipelines.data_transformation_pipeline import STAGGING_NAME, DataTransformationPipeline
from src.DataSciencePro.pipelines.Model_trainer_pipeline import STAGGING_NAME, ModelTrainingPipeline


STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
    object= DataIngestionPipeline()
    object.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGGING_NAME= 'Data Validation Stage'

try:
    logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
    object= DataValidationPipeline()
    object.initiate_data_validation()
    logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGGING_NAME= 'Data Transformation Stage'
try:
    logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
    object= DataTransformationPipeline()
    object.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGGING_NAME = "Model_Training_Stage"

try:
    logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
    object= ModelTrainingPipeline()
    object.Model_training()
    logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    
    