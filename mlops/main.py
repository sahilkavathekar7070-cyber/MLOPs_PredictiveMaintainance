from src.data_ingestion import data_ingestion
from src.logger import logger

def main() :
    # Step 1 : Data Ingestion
    df = data_ingestion()

main()