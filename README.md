# Classification Project
## TELCO's Feelin' the Churn
![alt text](agomez/Downloads/FeelChurn.jpg "Feel it")
___

[Project Planning](#planning)
[Data Dictionary](#data-dictionary)


# <a name="planning"></a>Planning 

### Project Objectives
- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.

- Create modules (`acquire.py`, `prepare.py`) that make your process repeateable.

- Construct a model to predict customer churn using classification techniques.


### Business Goals
- Find drivers for customer churn at Telco.

- Construct a ML classification model that accurately predicts customer churn.

- Document your process well enough to be presented or read like a report.

### Deliverables
- a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

- a `README.md` file containing the project description with goals, a data dictionary, project planning, instructions or an explanation of how someone else can recreate your project and findings, key findings, recommendations, and takeaways from your project.

- a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn)

- individual modules, .py files, that hold your functions to acquire and prepare your data.







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



# <a name="data-dictionary"></a>Data Dictionary
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
| sen_int           | tracks if TELCO customer is a senior citizen with internet           | 1 = yes, 0 = no                            | int64   | 3943 non-null                                                      |
| sen_int_techsup   | tracks if senior citizen internet customer used tech support         | 1 = yes, 0 = no                            | int64   | 3943 non-null                                                      |

### <a name="split-data"></a>Split Data
1. train_validate_test will take one argument(df) and 
2. run prep_telco to remove/rename/encode columns
3. then split our data into 20/80, 
4. then split the 80% into 30/70
5. perform a train, validate, test split
6. return: the three split pandas dataframes: train/validate/test


### <a name="explore-data"></a>Explore Data
1. List features as either categorical or quantitative
2. Store lists as variables: 'cat_vars' & 'quant_vars'
3. Run Univariable Stats function from `explore.py`
4. Analyze and document takeaways.
5. Run Bivariable Stats function from `explore.py`
6. Analyze and document takeaways.
7. Run Multivariable Stats function from `explore.py`
4. Analyze and document takeaways.


# univar takeaways:
- 74% of total cust base churned in past 72 months
- Gender seems balanced, males are 51% of custs though
- Only 16% of custs are elderly
- Only a quarter of custs are family units
- 30% are single parents
- 46% are bachelor(ette)s; almost half!
- 91% (3572) of cust base use our phone service
    - 48% of them (1696) have multiline phones
- 56% of int cust are Fiber (1734)
    - 88% of int cust use online feats
    - 90% of int cust stream media
    - 57% of int cust DON'T use device protection
    - 64% of int cust DON'T use tech support
- 59% of custs are enrolled in paperless billing
- 45% of custs are enrolled in auto billpay
    - majority 33% of all cust pay using echk
- contracts
    - 1yr = 21%
    - 2yr = 24%
    - M2M = 55%
- tenure
    - most amount of custs are new and old
- monthly charges: 
    - high amt of cust pay low bills, then the rest of data is almost normal with a left skew
    - total charges decrease exponentially


# bivar takeaways:
- gender doesn't seem to be a driver of churn
- seniors churn at a higher rate (40%), although that could be a bit morbid... And they are a MUCH smaller fraction of total customers.
    - 42% seniors w/internet churned, 7% total churn
- Non-elderly churn at 24%
- Families: Do they keep services for those who depend on them?
    - 15% of family household churn
    - 34% of single custs churn
    - 25% of single parents churn
- phone service has a high p-value (0.718) doesn't affect churn
    - phone_multi_line p-value = 0.08
    - phone_sgl_line p-value = 0.14
- internet: has very low p-values
    - 19% of DSL cust churn, 7% total cust
    - 41% of Fiber cust churn, 18% total cust
    - 15% of churned cust did not use online feats
    - 17% of churned cust streamed media
    - 18% of churned cust did NOT have device protection
    - 21% of churned cust did NOT use tech support
- billpay: has a very low p-val (2.653218x10^-46)
    - 15% of billpayer churned, 7% of total custs: 45% total custs use billpay
    - 36% of non billpay cust churned, 20% of total custs: 55% total cust do NOT use billpay
    - 46% of e-pymt custs churned, 15% of total custs: 33% of total cust use echk
    - 21% of mailed check custs churned, 5% of total custs: 23% total custs mail checks
- contracts: 
    - 2% of 2yr custs churn, 0.06% total, account for 24% of total custs
    - 11% of 1yr custs churn, 2.5% total, account for 22% of total custs
    - 43% of M2M custs churn, 24% total, account for 55% of total custs
- charges: as monthly charges increase(threshold approx $65) a larger amt of custs drop off


# multivar takeaways:
- Elderly churn at higher rates, although they are a significantly smaller pop.
    - this happens within the first few months: are they confused/need tech help?
    - as monthly charges increase, so does their churn rate.
        - binary/disc
        - cat/cat
        - null: no relationship
        - chi2
        
- Fiber custs are churning in droves, they are a larger pop, this is a problem. 
    - for what seems to be high monthly charges.
    - most within the first year.
        - ttest
        
        
- High amt of non-billpayers churn within the first two yrs and steadily continue.
    - large amt non-billpayers monthly charges are low.
        -  so are the total charges b'c they churn within the first 20 months.
        
- M2M cust are also a large pop churn.
    - for what seems to be high monthly charges.
    - M2M cust that stay have varying monthly charges.





