from src.textSummarizer.pipeline.stage_01_data_ingestion  import DataIngestionPipeline

from src.textSummarizer.logging import logger

STAGE_NAME  = "DATA INGESTION STAGE"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
