# modul yang digunakna
import numpy as np
import pandas as pd
import streamlit as st
from sklearn import svm

@st.cache()
def load_data():

    #load dataset
    df = pd.read_csv('DATASET.csv')

    df.dropna(inplace=True)

    x = df[["sett_70", "sett_75", "sett_80", "sett_85", "sett_90", "sett_95", "sett_100", "Arms"]]
    y = df[['Class']]

    return df, x, y

@st.cache()
def train_model(x, y):
    clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
    model = clf.fit(x, y)
    
    model.fit(x, y)

    score = model.score(x, y)

    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)

    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score
