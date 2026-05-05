from src.DataSciencePro.constants import *
from src.DataSciencePro.utils.common import read_yaml, create_directories
from src.DataSciencePro.entity.entity_config import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig


class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        param_file_path: Path = PARAM_FILE_PATH,
        scheme_file_path: Path = SCHEME_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(param_file_path)
        self.schema = read_yaml(scheme_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
    def get_data_validation_config(self)-> DataValidationConfig:
        config= self.config.data_validation
        schema= self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config= DataValidationConfig(
            root_dir= config.root_dir,
            unzip_dir= config.unzip_dir,
            status_file= config.status_file,
            all_schema= schema
                    
        )
        return data_validation_config
    
    def get_data_tranformation_config(self)-> DataTransformationConfig:
        config= self.config.data_transfromation
        schema= self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_tranformation_config= DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            all_schema= schema
                    
        )
        return data_tranformation_config
    
    def get_modeltrainer_config(self)-> ModelTrainerConfig:
        config= self.config.model_trainer
        params= self.params.ElasticNet
        schema= self.schema.TARGET_COLUMN

        
        
        create_directories([config.root_dir])
        
        modeltrainer_config= ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha= params.alpha,
            l1_ratio= params.l1_ratio,
            target_column= schema.name
                    
        )
        return modeltrainer_config
    
    
    