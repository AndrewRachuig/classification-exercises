import acquire
import pandas as pd


def prep_iris(iris):
    '''
    Takes in a dirty iris dataframe and outputs a cleaned/transformed iris dataframe as per the requirements in the exercises.
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


