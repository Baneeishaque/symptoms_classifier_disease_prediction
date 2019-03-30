import json

import pandas


# TODO : Make Function - get_data_frame_from_csv(url,column_names)


def get_data_frame():
    url = "data/Disease-Symptom_Knowledge_Database.csv"
    with open('data/symptoms.json') as json_file:
        symptoms_json = json.load(json_file)
    column_names = symptoms_json + ['class']
    return pandas.read_csv(url, names=column_names, engine='python')
