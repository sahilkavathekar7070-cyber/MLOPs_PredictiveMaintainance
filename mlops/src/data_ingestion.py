import pandas as pd
from src.logger import logger

def data_ingestion() :

    try :
        ''' 
        Title : Predictive Maintainance for Coal Mine Application

        Independent Column : ['record_id', 'timestamp', 'mine_id', 'conveyor_id', 'idler_id',
       'vibration_rms', 'vibration_peak', 'vibration_kurtosis',
       'vibration_crest_factor', 'bpfo_amplitude', 'bpfi_amplitude',
       'bsf_amplitude', 'ftf_amplitude', 'bearing_temperature',
       'acoustic_level', 'rotational_speed', 'ambient_temperature', 'humidity',
       'dust_concentration', 'moisture_level', 'operating_hours',
       'conveyor_load', 'belt_speed', 'motor_current', 'lubrication_age_hours',
       'last_maintenance_hours', 'previous_failure_count',
       'seal_condition_score', 'bearing_age_months', ]

        Target Column : 'failure_within_7_days'
        '''
        logger.info(f'Data Ingestion Started.......')
        df = pd.read_csv(r'C:\MLOPs_PredictiveMaintainance\mlops\data\raw\preventative_maintainance_dataset.csv')
        logger.info(f'Data Ingestion Completed with {df.shape}')
        logger.info(f'Data Columns :{df.columns}')
        return df

    except Exception as e :
        logger.exception(f'File not found....{e}')
        raise