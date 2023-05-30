from Graph import view
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
from NB_Accuracy import GNB
from DT_Accuracy import DecisionTree
from sklearn.preprocessing import LabelEncoder
def performace():
    student_data = pd.read_csv("../DropoutPrediction/dataset/student-data.csv")
    feature_cols = list(student_data.columns[:-1])

    # Extract target column 'dropout'
    target_col = student_data.columns[-1]

    # Separate the data into feature data and target data (X_train and y_train, respectively)
    X_train = student_data[feature_cols]
    X_train = preprocess_features(X_train)
    y_train = student_data[target_col]

    x_train, x_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)
    nb_accuracy, data_gnb = GNB(x_train, x_test, y_train, y_test)
    dt_accuracy,data_dt = DecisionTree(x_train, x_test, y_train, y_test)


    list1 = []
    list1.clear()
    list1.append(nb_accuracy)
    list1.append(dt_accuracy)
    view(list1)

    data = []
    data.append(data_gnb)
    data.append(data_dt)
    return data
def preprocess_features(x_test):
    # Testing Dataset
    # For each feature, encode to categorical values
    class_le = LabelEncoder()
    for column in x_test[
        ["school", "sex", "address", "famsize", "Pstatus", "Mjob", "Fjob", "reason", "guardian",
         "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic"]].columns:
        x_test[column] = class_le.fit_transform(x_test[column].values)
    return x_test


