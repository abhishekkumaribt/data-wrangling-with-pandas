# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 

# Find out the information of the `job` column.

# Check the `loan_status`  approval rate by `job`

# Check the percentage of loan approved by `education`

# Check the percentage of loan approved by `previous loan status`

# Create a pivot table between `loan_status` and `marital ` with values form `age`

# Loan status based on marital status whose status is married

#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
data = pd.read_csv(path, delimiter=";")
print(data.head())

data = data.replace("unknown", np.NaN)

data.rename(columns={"loan" : "previous_loan_status", "y" : "loan_status"}, inplace=True)

print(data.job.value_counts())

print(data.job.describe())

loan_approval = data.fillna("no").groupby(by=["job", "loan_status"]).count().iloc[:,0].unstack()
loan_approval["percent"] = loan_approval.yes/(loan_approval.yes+loan_approval.no)

print(loan_approval)

loan_approval_edu = data.fillna("unknown").groupby(by=["education", "loan_status"]).count().iloc[:,0].unstack()
loan_approval_edu["percent"] = loan_approval_edu.yes/(loan_approval_edu.yes+loan_approval_edu.no)

print(loan_approval_edu)

loan_approval_prev_loan = data.fillna("unknown").groupby(by=["previous_loan_status", "loan_status"]).count().iloc[:,0].unstack()
loan_approval_prev_loan["percent"] = loan_approval_prev_loan.yes/(loan_approval_prev_loan.yes+loan_approval_prev_loan.no)

print(loan_approval_prev_loan)

loan_st_mar = data.pivot_table(index="loan_status", columns="marital", values="age")

print(loan_st_mar["married"])

df_credit_score = pd.DataFrame(columns=['customer_id','score'])

df_branch_1 = pd.DataFrame({'customer_id': [1, 2], 'first_name': ["Abhishek", "Sikandar"], 'last_name' : ["kumar", "kumar"]})

df_branch_2 = pd.DataFrame({'customer_id': [3, 4], 'first_name': ["Anurag", "Sushil"], 'last_name' : ["kumar", "kumar"]})

df_credit_score = pd.DataFrame({'customer_id': [1, 2], 'score': ["10", "10"]})

df_new = pd.concat([df_branch_1, df_branch_2])
print(df_new)

print(pd.merge(df_new, df_credit_score, on="customer_id"))


