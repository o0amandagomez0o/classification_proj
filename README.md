    - Create new repo: 'classification_proj'
        - clone
    - Create .gitignore that includes env.py
        - push
    - Create env.py file that store MySQL login credentials to obtain TELCO data.
        - save
        - confirm it is ignored (git status)
    - Create README.md file to begin notating steps taken so far.
        - save
        - push
    - Create a Jupyter Lab environment to continue working in.
    - Create Jupyter Notebook to begin data pipeline: 'telco001'


# Jupyter Notebook

### Acquire Data
1. Use mySQL to confirm the MySQL query I want to use.
2. Add `get_connection` function to `acquire.py`
    - this will connect me to the Codeup DB to pull dataset from MySQL.
3. Create `get_telco_data` function and add to `acquire.py`
    - this will use the query from step one to obtain `customers`table from `telco_churn` database.
4. Add all imports necessary
5. read telco data from MySQL into a df using `get_telco_data` function


### Clean Data
1. covert to numeric representation: 'total_charges', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'payment_type'
2. encode to binary: 'gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', 'churn'
3. drop: 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'payment_type': due to redundancy/new encoded cols 
4. concat to the end of df
5. single cleaned dataframe


### Prepare Data
1. prep_telco will take one argument(df) and 
2. run clean_telco to remove/rename/encode columns
3. then split our data into 20/80, 
4. then split the 80% into 30/70
5. perform a train, validate, test split
6. return: the three split pandas dataframes-train/validate/test