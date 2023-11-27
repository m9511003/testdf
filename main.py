import util
import streamlit as st

file = './data/boston.csv'
df1 = util.getData(file)
st.header('github test')
st.write(df1)
