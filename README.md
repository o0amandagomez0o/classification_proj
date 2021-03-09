
# Classification Project: TELCO Data Set


___

[[Project Planning](#planning)]
[[Key Findings](#key-findings)]
[[Tested Hypotheses](#tested-hypotheses)]
[[Recommendations](#recommendations)]
[[Takeaways](#takeaways)]
[[Data Dictionary](#data-dictionary)]
[[Workflow](#workflow)]


# <a name="planning"></a>Planning 

### Project Objectives
We here at TELCO Communications™ take customer satisfaction to heart. We are always looking to improve our customer's experience with our company. Today, we would like to explore the possible drivers of our customer churn rate. The following Jupyter Notebook offers in depth exploration, analysis, and models to project how drivers affect our customer experience and ultimate retention.


### Business Goals
- Identify drivers for customer churn at TELCO.
- Construct a ML classification model that accurately predicts customer churn.
    + create CSV file of these predictions.


### Deliverables
- a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn.

- a `README.md` file containing the project description with goals, a data dictionary, project planning, key findings, recommendations, and takeaways from your project.

- a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn)

- individual modules, .py files, that hold your functions to acquire and prepare your data.

___
# <a name="key-findings"></a>Key Findings
### 1. Elderly churn at higher rates (40%), although they are a significantly smaller population.
- this happens within the first few months: are they confused/need tech help?
- as monthly charges increase, so does their churn rate.
        
### 2. Fiber customers are churning in droves (41%), they are a larger population, this is a problem. 
- for what seems to be high monthly charges.
- most within the first year.
        
### 3. High amount of non-billpayers (55%) churn within the first two years and steadily continue.
- large amount non-billpayers monthly charges are low.
    -  so are the total charges because they churn within the first 20 months.
        
### 4. Month-to-Month customers are also a large population churn.
- for what seems to be high monthly charges.
- Month-to-Month customers that stay have varying monthly charges.

___
# <a name="tested-hypotheses"></a>Tested Hypotheses 
> ### $Hypothesis_{1}$
> $H_{0}$: "Elderly status and churn rates are INDEPENDENT."
>
> $H_{a}$: "There is a relationship between elderly customers and whether they leave TELCO."

> ### $Hypothesis_{2}$
> $H_{0}$: "Monthly charges are the same for the Fiber & Non-Fiber customers."
>
> $H_{a}$: "Monthly charges for Fiber & Non-Fiber customers are different."

> ### $Hypothesis_{3}$
> $H_{0}$: "Contract status and churn rates are INDEPENDENT."
>
> $H_{a}$: "There is a relationship between contracted customers and whether they leave TELCO."

> ### $Hypothesis_{4}$
> $H_{0}$: "Having automatic bill pay and churn rates are INDEPENDENT."
>
> $H_{a}$: "There is a relationship between customers using automatic bill pay and whether they leave TELCO."





___
# <a name="recommendations"></a>Recommendations
1. Create a Tier 3 Customer Service Representative Team that will be allocated time to reach out to our elderly clients, to offer technical support. These CSRs should be picked on they customer feedback courtesy and helpfullness scores.

1. Analyze costs to provide Fiber internet customers better deals to retain during the first 12 months.

1. Reexamine sales procedures to enroll customers in automatic bill pay during the intial signup.
    - possibly intentivize them with a discount.
1. Our non-contract customers are our largest population of churn. 
    - Allow our customers their freedom of contracts
    - Although, by building customer loyalty program, with incentives:
        - customers will enjoy receiving discounts from their provider and choose to stay with a company that gives back.




___
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

___
# <a name="workflow"></a>Workflow

1. [Prep Your Repo](final_telco.ipynb#prep-your-repo)
2. [Import](final_telco.ipynb#import)
2. [Acquire Data](final_telco.ipynb#acquire-data)
3. [Clean, Prep & Split Data](final_telco.ipynb#clean-prep-and-split-df)
5. [Explore Data](final_telco.ipynb#explore-data)
    - [Hypothesis Testing](final_telco.ipynb#hypothesis-testing)
6. [Identify Baseline](final_telco.ipynb#identify-baseline)
7. [Modeling](final_telco.ipynb#modeling)
    - [Train](final_telco.ipynb#train)
    - [Validate](final_telco.ipynb#validate)
    - [Test](final_telco.ipynb#test)
8. [Predict on Test Model](final_telco.ipynb#predict-on-test-model)
9. [Export Predictions to CSV](final_telco.ipynb#export-predictions-to-csv)

