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
6. 
7. 


### Clean Data
1. 