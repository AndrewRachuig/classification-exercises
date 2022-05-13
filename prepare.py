import acquire
import pandas as pd
import numpy as np
# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer


def prep_iris(iris):
    '''
    Takes in a dirty iris dataframe and returns a cleaned/transformed iris dataframe as per the requirements in the exercises.
    Arguments: iris - a pandas dataframe with the expected feature names and columns
    Return: clean_iris - a dataframe with the requisite transformations applied to it.
    The returned Dataframe is not yet split for train, validate, test.
    '''
    iris.drop(columns = ['Unnamed: 0', 'species_id', 'measurement_id'], inplace=True)
    iris.rename(columns = {'species_name': 'species'}, inplace=True)
    dummy_df = pd.get_dummies(iris.species, dummy_na=False, drop_first=True)
    iris = pd.concat([iris, dummy_df], axis = 1)
    return iris


def clean_titanic_data(df):
    '''
    Takes in a titanic dataframe and returns a cleaned dataframe
    Arguments: df - a pandas dataframe with the expected feature names and columns
    Return: clean_df - a dataframe with the cleaning operations performed on it
    '''
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    # Drop columsn
    columns_to_drop = ['Unnamed: 0','embarked', 'class', 'passenger_id', 'deck']
    df = df.drop(columns = columns_to_drop)
    # Encoded categorical variables
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na=False, drop_first=[True, True])
    # Concatenate dummy_df to data
    df = pd.concat([df, dummy_df], axis = 1)
    return df.drop(columns = ['sex', 'embark_town'])

def impute_age_titanic(train, validate, test):
    '''
    Imputes the mean age of train to all three datasets
    '''
    imputer = SimpleImputer(strategy ='mean', missing_values=np.nan)
    imputer = imputer.fit(train[['age']])
    train[['age']] = imputer.transform(train[['age']])
    validate[['age']] = imputer.transform(validate[['age']])
    test[['age']] = imputer.transform(test[['age']])
    return train, validate, test

def prep_titanic_data(df):
    df = clean_titanic_data(df)
    train, test = train_test_split(df, train_size = 0.8, stratify = df.survived, random_state = 1234)
    train, validate = train_test_split(train, train_size = 0.7, stratify = train.survived, random_state = 1234)
    train, validate, test = impute_age_titanic(train, validate, test)
    return train, validate, test


def prep_telco(telco):
    '''
    Takes in a dirty telco dataframe and returns a cleaned/transformed telco dataframe
    Arguments: telco - a pandas dataframe with the expected feature names and columns
    Return: clean_telco - a dataframe with various cleaning operations performed on it.
    
    '''
    telco.drop(columns = ['Unnamed: 0', 'customer_id', 'internet_service_type_id', 'payment_type_id', 'contract_type_id', 'phone_service'], inplace=True)
    telco.drop_duplicates(inplace=True)
    telco.total_charges.replace(' ', '0', inplace=True)
    telco['total_charges'] = pd.to_numeric(telco['total_charges'], errors='coerce')
    dummies_list = telco.select_dtypes('object').columns
    dummy_df = pd.get_dummies(telco[dummies_list], dummy_na=False, drop_first=[True, True])
    telco = pd.concat([telco, dummy_df], axis = 1)
    
    # Before splitting the resulting cleaned dataframe into Train, Validate, Test subsets I would need to drop the 
    # original categorical columns used to create the dummy categorical columns. That could be done here before 
    # returning the cleaned telco dataframe.
    return telco

