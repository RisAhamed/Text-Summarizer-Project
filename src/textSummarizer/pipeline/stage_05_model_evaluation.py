from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_evaluation import ModelEvaluation
from src.textSummarizer.logging import logger
from pathlib import Path


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate()