# Import Dependencies
import pandas as pd
from collections import defaultdict

df = pd.read_excel('raw_data.xlsx')
print('The data is ...')
print(df.head())

data = df.fillna(method='ffill')
print('The data after fill NaN is ...')
print(data.head())

# TODO : Print array as string line
print('The data columns are : ', list(data))


# Process Disease and Symptom Names
def process_data(passed_data):
    data_list = []
    data_name = passed_data.replace('^', '_').split('_')
    n = 1
    for names in data_name:
        if n % 2 == 0:
            data_list.append(names)
        n += 1
    return data_list


disease_list = []
disease_symptom_dict = defaultdict(list)
disease_symptom_count = {}
count = 0

for idx, row in data.iterrows():

    # Get the Disease Names
    if (row['Disease'] != "\xc2\xa0") and (row['Disease'] != ""):
        disease = row['Disease']
        disease_list = process_data(passed_data=disease)
        count = row['Count of Disease Occurrence']

    # Get the Symptoms Corresponding to Diseases
    if (row['Symptom'] != "\xc2\xa0") and (row['Symptom'] != ""):
        symptom = row['Symptom']
        symptom_list = process_data(passed_data=symptom)
        for d in disease_list:
            for s in symptom_list:
                disease_symptom_dict[d].append(s)
            disease_symptom_count[d] = count

# See that the data is Processed Correctly
print('The disease-symptoms mapping is : ', disease_symptom_dict)

# Count of Disease Occurrence w.r.t each Disease
print('The No.of occurrences of each symptom is : ', disease_symptom_count)

print('The disease-symptoms data table is ...')
df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease', 'Symptom'])
print(df1.head())

# for values in disease_symptom_count.items():
#     print(values[1])
#
# print(df1.head())

# print('The disease-no. of occurrences data table is ...')
# for values in disease_symptom_count.items():
#     print(values[0],' : ',values[1])
#
# print(df1.head())

# TODO : Make dataset from disease-symptoms table / use df1
# TODO : Make necessary data plots
# TODO : Make Validation set
# TODO : Testing of sets
# TODO : Evaluate algorithms
# TODO : Compare algorithms & choose one
# TODO : Prediction on validation dataset
# TODO : Fit data model
# TODO : Predict on new instance
# TODO : Export data model
# TODO : Predict on new instance by exported model
# TODO : Make Function for prediction by model
# TODO : API for prediction by model





