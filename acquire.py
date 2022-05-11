import env
import os

# The following function can be used to create or access a local cache of data

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