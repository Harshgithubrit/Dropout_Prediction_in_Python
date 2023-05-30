import numpy as np
import pandas as pd
import os
from time import time
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import pickle
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.metrics import f1_score,precision_score,recall_score
def build_model():
    try:

        student_data = pd.read_csv("../DropoutPrediction/dataset/student-data.csv")
        feature_cols = list(student_data.columns[:-1])

        # Extract target column 'dropout'
        target_col = student_data.columns[-1]

        # Separate the data into feature data and target data (X_train and y_train, respectively)
        X_train = student_data[feature_cols]
        X_train = preprocess_features(X_train)
        y_train = student_data[target_col]

        ##For Model DecisionTreeClassifier
        clf_dts = DecisionTreeClassifier()
        clf_dts.fit(X_train, y_train)
        with open('../DropoutPrediction/model/DT.model', 'wb') as f:
            pickle.dump(clf_dts, f)


        # For Model Gaussian Naive Bayes
        clf_NB = GaussianNB()
        clf_NB.fit(X_train, y_train)
        with open('../DropoutPrediction/model/NB.model', 'wb') as f:
            pickle.dump(clf_NB, f)



    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print("LINE NO: ",tb.tb_lineno)

def preprocess_features(X_train):
        # Training Dataset
        # For each feature, encode to categorical values
        class_le = LabelEncoder()
        for column in X_train[
            ["school", "sex", "address", "famsize", "Pstatus", "Mjob", "Fjob", "reason", "guardian",
             "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic"]].columns:
            X_train[column] = class_le.fit_transform(X_train[column].values)
        return X_train
# build_model()


