import env
import os
import pandas as pd


'''
# The following function is an example of how a function can be used to create and/or access a local cache of data

def get_date_example(): #this can be any file type, not just csv
    filename = "example.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        #if no local file exists, read it in from the source and put it in a dataframe

        file_location = "https://sampleurl.com"
        df = pd.read_csv(file_location)

        #Write this dataframe into a cached local copy
        df.to_csv(filename)

        #returns the df to the calling code to be used
        return df
'''


def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT *
        FROM passengers;        
        '''
        url = env.get_db_url('titanic_db')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  

def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT *
        FROM measurements
        JOIN
        species USING(species_id);      
        '''
        url = env.get_db_url('iris_db')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  

def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        query = '''
        SELECT * 
        FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id);     
        '''
        url = env.get_db_url('telco_churn')
        df = pd.read_sql(query, url)
        df.to_csv(filename)

        return df  
