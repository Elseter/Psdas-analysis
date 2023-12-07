"""
* Developers: Riley / Emma
* File name: scholarshipHypothesis.py
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

# Variables
# ---------
dropout_noS = 0  # num of students with no Scholarship who drop out
dropout_S = 0  # num of students with Scholarship that drop out
e_G_noS = 0  # num of students with no Scholarship that are enrolled / graduate
e_G_S = 0  # num of students with Scholarship that are enrolled / graduate
total_students = 4424.0

# Formatting the dataframe
# ------------------------
df = X[['Scholarship holder']]  # grab scholarship column from X
df = pd.concat([df, y], axis=1, join="inner")  # combine S column with Y column
df = df.reset_index()  # Set the pointer to first value in dataframe

# Iterating through new dataframe
# -------------------------------
for index, row in df.iterrows():
    if row['Scholarship holder'] == 1:
        if row['Target'] == "Dropout":
            # If got scholarship and Dropout
            dropout_S += 1
        else:
            # If got scholarship and Graduate
            e_G_S += 1
    else:
        if row['Target'] == "Dropout":
            # If no scholarship and Dropout
            dropout_noS += 1
        else:
            # If no scholarship and Graduate
            e_G_noS += 1

# Print Data
# -----------
print("SCHOLARSHIP INFO")
print("----------------")
print(f"No Scholarship Dropouts: {dropout_noS}  | "
      f"{(dropout_noS / total_students) * 100}%")
print(f"Scholarship Dropouts: {dropout_S}  | "
      f"{(dropout_S / total_students) * 100}%")
print(f"No Scholarship continuing students: {e_G_noS}  | "
      f"{(e_G_noS / total_students) * 100}%")
print(f"Scholarship continuing students: {e_G_S}  | "
      f"{(e_G_S / total_students) * 100}%")
