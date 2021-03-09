to do:
- [ ] https://github.com/Churning-Up-the-Heat/classification-project/blob/master/readme.md
- [ ] readme
- [ ] add vizs to uni/bi/multi part
- [ ] create talking points
- [ ] time yourself
- [ ] 




# Classification Project
## TELCO's Feelin' the Churn
![alt text](FeelChurn.jpg "Feel it")
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






