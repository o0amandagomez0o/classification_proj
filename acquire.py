import pandas as pd
import numpy as np
import os
from env import host, user, password




def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'




def get_telco_data():
    '''
    This function reads in the telco data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    
    sql_query = 'select * from customers join contract_types using (contract_type_id) join internet_service_types using (internet_service_type_id) join payment_types using (payment_type_id);'
    return pd.read_sql(sql_query, get_connection('telco_churn'))