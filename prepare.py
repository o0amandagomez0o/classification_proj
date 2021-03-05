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
    covert: 
    encode: 'gender', 'partner', 'dependents'
    and drop:
        - due to un-necessity 
        - due to redundancy/enew encoded cols
    
    return: single cleaned dataframe
    """
    
    df.gender = df.gender.replace({'Female': 0, 'Male': 1})
    df.partner = df.partner.replace({'No': 0, 'Yes': 1})
    df.dependents = df.dependents.replace({'No': 0, 'Yes': 1})


    return df