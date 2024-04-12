from Text_Summarizer_Project.config.configuration import ConfigurationManager
from Text_Summarizer_Project.components.data_transformation import DataTransformation
from Text_Summarizer_Project.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()