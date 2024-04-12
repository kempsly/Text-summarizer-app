from Text_Summarizer_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from Text_Summarizer_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from Text_Summarizer_Project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from Text_Summarizer_Project.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
 
from Text_Summarizer_Project.logging import logger



# from Text_Summarizer_Project.logging import logger
# logger.info("Welcome to text summarization app!")

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e