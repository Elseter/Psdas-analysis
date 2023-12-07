"""
* Developers: Riley / Emma
* File name: aGHypothesis.py
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
# AGE, GENDER, AND DROPOUTS

# variables
# ---------------------------------------------------------------------------
f17_21d = 0  # female students between the ages 17 - 21 that dropped out
f17_21e = 0  # female students between the ages 17 - 21 that are enrolled
f22_25d = 0  # female students between the ages 22 - 25 that dropped out
f22_25e = 0  # female students between the ages 22 - 25 that are enrolled
f26_30d = 0  # female students between the ages 26 - 30 that dropped out
f26_30e = 0  # female students between the ages 26 - 30 that are enrolled
f31_40d = 0  # female students between the ages 31 - 40 that dropped out
f31_40e = 0  # female students between the ages 31 - 40 that are enrolled
f41plusd = 0  # female students 41+ that dropped out
f41pluse = 0  # female students 41+ that are enrolled
totalf = 0  # female student count

m17_21d = 0  # male students between the ages 17 - 21 that dropped out
m17_21e = 0  # male students between the ages 17 - 21 that are enrolled
m22_25d = 0  # male students between the ages 22 - 25 that dropped out
m22_25e = 0  # male students between the ages 22 - 25 that are enrolled
m26_30d = 0  # male students between the ages 26 - 30 that dropped out
m26_30e = 0  # male students between the ages 26 - 30 that are enrolled
m31_40d = 0  # male students between the ages 31 - 40 that dropped out
m31_40e = 0  # male students between the ages 31 - 40 that are enrolled
m41plusd = 0  # male students 41+ that dropped out
m41pluse = 0  # male students 41+ that are enrolled
totalm = 0  # male student count
# -----------------------------------------------------------------------------

# Format the dataframe
ft = X[['Gender','Age at enrollment']]  # grab Gender column from dataset
ft = pd.concat([ft, y], axis=1, join="inner")  # combine columns with Y column
ft = ft.reset_index()   # Set the pointer to first value in dataframe
# -----------------------------------------------------------------------------

# Iterating through the new dataframe
for index, column in ft.iterrows():
    if column['Gender'] == 1:
        #count of male students
        totalm += 1
        # if 1 is male
        if column['Age at enrollment'] >= 17 or column['Age at enrollment'] <= 21:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m17_21d += 1
            else:
                # If got scholarship and Graduate
                m17_21e += 1
        elif column['Age at enrollment'] >= 22 or column['Age at enrollment'] <= 25:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m22_25d += 1
            else:
                # If got scholarship and Graduate
                m22_25e += 1
        elif column['Age at enrollment'] >= 26 or column['Age at enrollment'] <= 30:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m26_30d += 1
            else:
                # If got scholarship and Graduate
                m26_30e += 1
        elif column['Age at enrollment'] >= 31 or column['Age at enrollment'] <= 40:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m31_40d += 1
            else:
                # If got scholarship and Graduate
                m31_40e += 1
        elif column['Age at enrollment'] >= 41:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m41plusd += 1
            else:
                # If got scholarship and Graduate
                m41pluse += 1
    else:
        # count of female students
        totalf += 1
        # if 1 is female
        if column['Age at enrollment'] >= 17 or column['Age at enrollment'] <= 21:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f17_21d += 1
            else:
                # If got scholarship and Graduate
                f17_21e += 1
        elif column['Age at enrollment'] >= 22 or column['Age at enrollment'] <= 25:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f22_25d += 1
            else:
                # If got scholarship and Graduate
                f22_25e += 1
        elif column['Age at enrollment'] >= 26 or column['Age at enrollment'] <= 30:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f26_30d += 1
            else:
                # If got scholarship and Graduate
                f26_30e += 1
        elif column['Age at enrollment'] >= 31 or column['Age at enrollment'] <= 40:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f31_40d += 1
            else:
                # If got scholarship and Graduate
                f31_40e += 1
        elif column['Age at enrollment'] >= 41:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f41plusd += 1
            else:
                # If female student is enrolled
                f41pluse += 1
# -------------------------------------------------------------------------
# print statements

# total female students
print(totalf)
# total male students
print(totalm)
# total male students that dropped out
print(m17_21d + m22_25d + m26_30d + m31_40d + m41plusd)
# total male students are enrolled
print(m17_21e + m22_25e + m26_30e + m31_40e + m41pluse)
# total female students that dropped out
print(f17_21d + f22_25d + f26_30d + f31_40d + f41plusd)
# total female students are enrolled
print(f17_21e + f22_25e + f26_30e + f31_40e + f41pluse)


