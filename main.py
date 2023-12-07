"""
* Developers: Riley / Emma
* File name: main.py
* Class: COMSC.230
* Prof: Dr. Omar
* Purpose: This file runs a series of tests to analyze aspects of the
*           Predict students' dropout and academic success dataset
"""
# -------------------------------------------------------------------
# INITIAL SETUP

# Import Statements
from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot
import pandas as pd

# fetch dataset
predict_students_dropout_and_academic_success = fetch_ucirepo(id=697)

# data (as pandas dataframes)
X = predict_students_dropout_and_academic_success.data.features
y = predict_students_dropout_and_academic_success.data.targets

# -------------------------------------------------------------------
# SCHOLARSHIPS AND DROPOUTS

dropout_noS = 0
dropout_S = 0
e_G_noS = 0
e_G_S = 0
total_students = 4424.0

df = X[['Scholarship holder']]
df = pd.concat([df, y], axis=1, join="inner")
df = df.reset_index()
for index, row in df.iterrows():
    if row['Scholarship holder'] == 1:
        if row['Target'] == "Dropout":
            dropout_S += 1
        else:
            e_G_S += 1
    else:
        if row['Target'] == "Dropout":
            dropout_noS += 1
        else:
            e_G_noS += 1

print("SCHOLARSHIP INFO")
print("----------------")
print(f"No Scholarship Dropouts: {dropout_noS}  | {(dropout_noS / total_students)*100}%")
print(f"Scholarship Dropouts: {dropout_S}  | {(dropout_S / total_students)*100}%")
print(f"No Scholarship continuing students: {e_G_noS}  | {(e_G_noS / total_students)*100}%")
print(f"Scholarship continuing students: {e_G_S}  | {(e_G_S / total_students)*100}%")
