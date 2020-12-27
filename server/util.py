import pickle
import json
import numpy as np
import os
import pandas as pd

__gender = None
__dependents = None
__education = None
__self_employed = None
__property_area = None
__married = None

__data_columns = None
__model = None

def get_estimated_loan(gend, dependent, edu, self_emp, prop_area, marry, income, com_income, loan_am, loan_term, credit_hist):
    column_temp = ['Dependents', 'Education', 'ApplicantIncome', 'CoapplicantIncome',
                   'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Gender_Female',
                   'Gender_Male', 'Self_Employed_1.0', 'Self_Employed_2.0',
                   'Property_Area_1', 'Property_Area_2', 'Property_Area_3', 'Married_No',
                   'Married_Yes']
    x = pd.DataFrame(columns=column_temp)
    for i in range(0, 16):
        x.loc[0, x.columns[i]] = 0

    x.iloc[0, 2] = income
    x.iloc[0, 3] = com_income
    x.iloc[0, 4] = loan_am
    x.iloc[0, 5] = loan_term
    x.iloc[0, 6] = credit_hist
    # gender object column
    if gend == 'Male':
        x.iloc[0, 7] = 0
        x.iloc[0, 8] = 1
    else:
        x.iloc[0, 7] = 1
        x.iloc[0, 8] = 0

    # dependent object column
    if dependent == 0:
        x.iloc[0, 0] = 0
    elif dependent == 1:
        x.iloc[0, 0] = 1
    elif dependent == 2:
        x.iloc[0, 0] = 2
    else:
        x.iloc[0, 0] = 3

    # education object column
    if edu == 'Graduate':
        x.iloc[0, 1] = 0
    else:
        x.iloc[0, 1] = 1

    # self_employment object column
    if self_emp == 'No':
        x.iloc[0, 9] = 0
        x.iloc[0, 10] = 1
    else:
        x.iloc[0, 9] = 1
        x.iloc[0, 10] = 0

    # property area object column
    if prop_area == 'Semiurban':
        x.iloc[0, 11] = 1
        x.iloc[0, 12] = 0
        x.iloc[0, 12] = 0
    elif prop_area == 'Urban':
        x.iloc[0, 11] = 0
        x.iloc[0, 12] = 1
        x.iloc[0, 12] = 0
    else:
        x.iloc[0, 11] = 0
        x.iloc[0, 12] = 0
        x.iloc[0, 12] = 1

    # marriage object column
    if marry == 'No':
        x.iloc[0, 14] = 1
        x.iloc[0, 15] = 0
    else:
        x.iloc[0, 14] = 0
        x.iloc[0, 15] = 1

    opt = None
    b = str(__model.predict(x)[0])
    if b == '1':
        opt = 'Accepted'
    else:
        opt = 'Not Accepted'
    return opt

def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __model
    with open("./artifacts/a_loan_data_rfc.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

load_saved_artifacts()
