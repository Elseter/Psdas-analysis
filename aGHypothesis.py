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
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# fetch dataset
predict_students_dropout_and_academic_success = fetch_ucirepo(id=697)

# data (as pandas dataframes)
X = predict_students_dropout_and_academic_success.data.features
y = predict_students_dropout_and_academic_success.data.targets

# -------------------------------------------------------------------
# AGE, GENDER, AND DROPOUTS

# General Background on Target Column
d = y.query('Target == "Dropout"').Target.count()
print("Target Background")
print("-----------------")
print(d)

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
        # count of male students
        totalm += 1
        # if 1 is male
        if column['Age at enrollment'] >= 17 and column['Age at enrollment'] <= 21:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m17_21d += 1
            else:
                # If got scholarship and Graduate
                m17_21e += 1
        elif column['Age at enrollment'] >= 22 and column['Age at enrollment'] <= 25:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m22_25d += 1
            else:
                # If got scholarship and Graduate
                m22_25e += 1
        elif column['Age at enrollment'] >= 26 and column['Age at enrollment'] <= 30:
            # check if dropout
            if column['Target'] == "Dropout":
                # If got scholarship and Dropout
                m26_30d += 1
            else:
                # If got scholarship and Graduate
                m26_30e += 1
        elif column['Age at enrollment'] >= 31 and column['Age at enrollment'] <= 40:
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
        if column['Age at enrollment'] >= 17 and column['Age at enrollment'] <= 21:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f17_21d += 1
            else:
                # If got scholarship and Graduate
                f17_21e += 1
        elif column['Age at enrollment'] >= 22 and column['Age at enrollment'] <= 25:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f22_25d += 1
            else:
                # If got scholarship and Graduate
                f22_25e += 1
        elif column['Age at enrollment'] >= 26 and column['Age at enrollment'] <= 30:
            # check if dropout
            if column['Target'] == "Dropout":
                # If female drop out
                f26_30d += 1
            else:
                # If got scholarship and Graduate
                f26_30e += 1
        elif column['Age at enrollment'] >= 31 and column['Age at enrollment'] <= 40:
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
print("Gender Information")
print("------------------")
print(f"Total number of Female Students: {totalf}")
print(f"Total number of Male Students: {totalm}")
print(f"Total number of Male dropout Students: {m17_21d + m22_25d + m26_30d + m31_40d + m41plusd}")
print(f"Total number of Male enrolled Students: {m17_21e + m22_25e + m26_30e + m31_40e + m41pluse}")
print(f"Total number of Female dropout Students: {f17_21d + f22_25d + f26_30d + f31_40d + f41plusd}")
print(f"Total number of Female enrolled Students: {f17_21e + f22_25e + f26_30e + f31_40e + f41pluse}")

print("Age & Dropout Information (Females)")
print("-------------------------")
print(f"Females between 17 - 21: {f17_21d}")
print(f"Females between 22 - 25: {f22_25d}")
print(f"Females between 26 - 30: {f26_30d}")
print(f"Females between 31 - 40: {f31_40d}")
print(f"Females 41+: {f41plusd}")

print("Age & Dropout Information (Males)")
print("-------------------------")
print(f"Males between 17 - 21: {m17_21d}")
print(f"Males between 22 - 25: {m22_25d}")
print(f"Males between 26 - 30: {m26_30d}")
print(f"Males between 31 - 40: {m31_40d}")
print(f"Males 41+: {m41plusd}")

# Bar Graph
# Saved as .jpg in images folder
# __________________________________
index = ['17 - 21', '22 - 25', '26 - 30', '31 - 40', '41+']
mdrop = [m17_21d , m22_25d , m26_30d , m31_40d , m41plusd]
fdrop = [f17_21d , f22_25d , f26_30d , f31_40d , f41plusd]
bar_ft = pd.DataFrame({'Male Dropouts': mdrop, 'Female Dropouts': fdrop}, index = index)
ew = bar_ft.plot.bar(rot=0)
plt.savefig('images/AgeGenderBarGraph.jpg', dpi=300)
plt.clf()

# Pie Chart Variables
totalmd = (m17_21d + m22_25d + m26_30d + m31_40d + m41plusd)
totalfd = (f17_21d + f22_25d + f26_30d + f31_40d + f41plusd)
# Pie Chart  1 Percentages
# male percentages (dropout)
m17_21 = round(((m17_21d / totalmd) * 100), 2)
m22_25 = round(((m22_25d / totalmd) * 100), 2)
m26_30 = round(((m26_30d / totalmd) * 100), 2)
m31_40 = round(((m31_40d / totalmd) * 100), 2)
m41plus = round(((m41plusd / totalmd) * 100), 2)

# Pie Chart 1
# Saved as .jpg in images folder
# __________________________________
y = np.array([m17_21, m22_25, m26_30, m31_40, m41plus])
labels = ["17-21", "22-25", "26-30", "31-40", "41+"]

# Function to add percentage values to Pie Chart
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%'.format(pct, v=val)
    return my_format

plt.pie(y, labels = labels, autopct = autopct_format(y))
plt.legend(bbox_to_anchor=(-0.40, -0.15), loc="lower left")
plt.savefig('images/MaleDropoutPIEchart.jpg', dpi=300)
plt.clf()

# Pie Chart  2 Percentages
# female percentages (dropout)
f17_21 = round(((f17_21d / totalfd) * 100), 2)
f22_25 = round(((f22_25d / totalfd) * 100), 2)
f26_30 = round(((f26_30d / totalfd) * 100), 2)
f31_40 = round(((f31_40d / totalfd) * 100), 2)
f41plus = round(((f41plusd / totalfd) * 100), 2)

# Pie Chart 1
# Saved as .jpg in images folder
# __________________________________
y = np.array([f17_21, f22_25, f26_30, f31_40, f41plus])
labels = ["17-21", "22-25", "26-30", "31-40", "41+"]

# Function to add percentage values to Pie Chart
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%'.format(pct, v=val)
    return my_format

plt.pie(y, labels = labels, autopct = autopct_format(y))
plt.legend(bbox_to_anchor=(-0.40, -0.15), loc="lower left")
plt.savefig('images/FemaleDropoutPIEchart.jpg', dpi=300)
plt.clf()