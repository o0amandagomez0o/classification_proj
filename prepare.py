import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import acquire

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

from env import host, user, password

def clean_telco(df):
    """
    clean_telco will take an acquired df and 
    covert to numeric representation: 'total_charges', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'payment_type'
    encode to binary: 'gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', 'churn'
    drop: 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'payment_type': due to redundancy/new encoded cols 
        and concat to the end of df
    
    return: single cleaned dataframe
    """
    
    # convert total_charges from obj to float
    df.total_charges = pd.to_numeric(df.total_charges, errors='coerce').astype('float64')
    # convert 11 blank total_charges of newly est. custs to ZERO.
    df.total_charges = df.total_charges.fillna(value=0)
    
    df.gender = df.gender.replace({'Female': 0, 'Male': 1})
    df.partner = df.partner.replace({'No': 0, 'Yes': 1})
    df.dependents = df.dependents.replace({'No': 0, 'Yes': 1})
    df.phone_service = df.phone_service.replace({'No': 0, 'Yes': 1})
    df.paperless_billing = df.paperless_billing.replace({'No': 0, 'Yes': 1})
    df.churn = df.churn.replace({'No': 0, 'Yes': 1})
    
    df.multiple_lines = df.multiple_lines.replace({'No': 0, 'Yes': 1, 'No phone service': 3})
    df.online_security = df.online_security.replace({'No': 0, 'Yes': 1, 'No internet service': 3})
    df.online_backup = df.online_backup.replace({'No': 0, 'Yes': 1, 'No internet service': 3})
    df.device_protection = df.device_protection.replace({'No': 0, 'Yes': 1, 'No internet service': 3})
    df.tech_support = df.tech_support.replace({'No': 0, 'Yes': 1, 'No internet service': 3})
    df.streaming_tv = df.streaming_tv.replace({'No': 0, 'Yes': 1, 'No internet service': 3})
    df.streaming_movies = df.streaming_movies.replace({'No': 0, 'Yes': 1, 'No internet service': 3})
    df.contract_type = df.contract_type.replace({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    df.internet_service_type = df.internet_service_type.replace({'None': 0, 'DSL': 1, 'Fiber optic': 2})
    df.payment_type = df.payment_type.replace({'Mailed check': 'mchk', 'Electronic check': 'echk', 'Bank transfer (automatic)': 'abt', 'Credit card (automatic)': 'acc'})
    
    pymttype_dummies = pd.get_dummies(df.payment_type, prefix='pymt_type', drop_first=True)
    
    dropcols = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'payment_type']
    df.drop(columns= dropcols, inplace=True)
    
    df = pd.concat([df, pymttype_dummies], axis =1)


    return df





def prep_telco(df):
    """
    prep_telco will take one argument(df) and 
    run clean_telco to remove/rename/encode columns
    then split our data into 20/80, 
    then split the 80% into 30/70
    
    perform a train, validate, test split
    
    return: the three split pandas dataframes-train/validate/test
    """
    df = clean_telco(df)
    train_validate, test = train_test_split(df, test_size=0.2, random_state=3210, stratify=df.churn)
    train, validate = train_test_split(train_validate, train_size=0.7, random_state=3210, stratify=train_validate.churn)
    return train, validate, test