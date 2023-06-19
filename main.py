import streamlit as st
import pandas as pd
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np

st.header("Oculous")
name = st.text_input("Enter your Name: ", key="name")

if name:
    with open("name.txt", "w") as file:
        file.write(name)
        st.success("Name stored successfully!")

st.header("write the path to your dataset")
dataset = st.text_input("Path: ", key="dataset")




