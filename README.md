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
2. rename: 'internet_service_type', 'payment_type' values
3. encode to binary: 'gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', 'churn'
4. dummy_encode: 'payment_type', 'internet_service_type', 'contract_type'
5. drop: 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'payment_type': due to redundancy/new encoded cols 
6. concat dummies to the end of df
7. return: single cleaned dataframe


### Prepare Data
1. takes in `clean_telco(df)`
2. creates column that converts tenure unit to years
3. creates column to determine if row is a multi-line phone customer, by summing 'phone_service' + 'multiple_lines'
4. creates column to determine if row is a single-line phone customer, by summing 'phone_service' + 'multiple_lines'
5. creates column to determine if row is a single w/dependents customer, by summing 'partner' + 'dependents'
6. creates column to determine if row is a single w/o dependents customer, by summing 'partner' + 'dependents'
7. creates column to determine if row is a not single w/ dependents customer, by summing 'partner' + 'dependents'
8. creates column to determine if row is a customer streaming media, by summing 'streaming_tv' + 'streaming_movies'
9. creates column to determine if row is a customer taking advantage of online security or backup, by summing 'online_security' + 'online_backup'
10. creates column to determine if row is a customer has autobill pay, by summing 'pymt_type_abt' + 'pymt_type_acc' 
11. drops columns: 'partner', 'dependents', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type', 'intserv_none'
12. returns single clean df

### Split Data
1. train_validate_test will take one argument(df) and 
2. run prep_telco to remove/rename/encode columns
3. then split our data into 20/80, 
4. then split the 80% into 30/70
5. perform a train, validate, test split
6. return: the three split pandas dataframes: train/validate/test



# Data Dictionary
|    column_name    |                              description                             | key                                        |  dtype  |                            value_counts                            |
|:-----------------:|:--------------------------------------------------------------------:|--------------------------------------------|:-------:|:------------------------------------------------------------------:|
| customer_id       | TELCO customer id                                                    |                                            | object  | 3943 non-null                                                      |
| gender            | customer gender                                                      | 1 = male, 0 = female                       | int64   | 3943 non-null, 1=male: 2027, 0=female: 1916                        |
| senior_citizen    | customer senior citizen (age) status                                 | 1 = senior citizen, 0 = not senior citizen | int64   | 3943 non-null, 1=senior citizen: 647, 0=not senior citizen: 3296   |
| tenure            | TELCO customer tenure in months                                      |                                            | int64   | 3943 non-null, min: 0 mo, max: 72 mo                               |
| phone_service     | tracks if customer has TELCO phone service                           | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 3572, 0=no: 371                              |
| multiple_lines    | tracks if TELCO phone customer has multiple lines                    | 1 = yes, 0 = no, 3 = no phone service      | int64   | 3943 non-null, 1=yes: 1696, 0=no: 1876, 3=no phone service: 371    |
| online_security   | tracks if TELCO internet customer uses online security               | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1130, 0=no: 1973, 3=no internet service: 840 |
| online_backup     | tracks if TELCO internet customer uses online backup                 | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1396, 0=no: 1705, 3=no internet service: 840 |
| device_protection | tracks if TELCO internet customer uses device protection             | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1351, 0=no: 1752, 3=no internet service: 840 |
| tech_support      | tracks if TELCO internet customer uses tech support                  | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1133, 0=no: 1970, 3=no internet service: 840 |
| paperless_billing | tracks if TELCO customer is signed up for paperless billing          | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2335, 0=no: 1608                             |
| monthly_charges   | lists expected month bill for TELCO customer                         |                                            | float64 | 3943 non-null                                                      |
| total_charges     | lists total charges billed to customer over their TELCO lifetime     |                                            | float64 | 3943 non-null                                                      |
| churn             | tracks if customer has left TELCO                                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1046, 0=no: 2897,                            |
| pymt_type_abt     | tracks if TELCO customer pays using Automatic Bank Transfers         | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 875, 0=no: 3068                              |
| pymt_type_acc     | tracks if TELCO customer pays using Automatic Credit Card payments   | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 883, 0=no: 3060                              |
| pymt_type_echk    | tracks if TELCO customer pays using Electronic Check payments        | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1290, 0=no: 2653                             |
| pymt_type_mchk    | tracks if TELCO customer pays using Electronic Check payments        | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 895, 0=no: 3048                              |
| intserv_dsl       | tracks if TELCO internet customer has DSL                            | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1369, 0=no: 2574                             |
| intserv_fiber     | tracks if TELCO internet customer has Fiber Optic                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1734, 0=no: 2209                             |
| contract_1yr      | tracks if TELCO customer has a 1 year contract                       | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 822, 0=no: 3121                              |
| contract_2yr      | tracks if TELCO customer has a 2 year contract                       | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 947, 0=no: 2996                              |
| contract_m2m      | tracks if TELCO customer has a 2 year contract                       | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2174, 0=no: 1769                             |
| phone_multi_line  | tracks if TELCO phone customer has multiple lines                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1696, 0=no: 2247                             |
| phone_sgl_line    | tracks if TELCO phone customer has multiple lines                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1876, 0=no: 2067                             |
| sgl_dependents    | tracks if TELCO customer is Single With Dependents                   | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1153, 0=no: 2790                             |
| sgl_no_dep        | tracks if TELCO customer is Single WithOUT Dependents                | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1803, 0=no: 2140                             |
| fam_house         | tracks if TELCO customer is NOT Single With Dependents               | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 987, 0=no: 2956                              |
| stream_media      | tracks if TELCO internet customer streams any media (TV/movies)      | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2804, 0=no: 1139                             |
| online_feats      | tracks if TELCO internet customer is using online security or backup | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2733, 0=no: 1210                             |
| auto_billpay      | tracks if TELCO customer is signed up for Automatic Billpay          | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1758, 0=no: 2158                             |