import streamlit as st

import pandas




st.set_page_config(layout="wide")



col1, col2 = st.columns(2)

with col1:
    st.image("images/aravind.jpg")

with col2:

    st.title("Lakshmi Aravind")

    content = """ Hi myself Lakshmi Aravind..Iam a spiritual come science lover .I wish to use technology as a
    tool to connect spiritual and science . Scispi is my future technological project to make all human souls to 
    get enlighted and
    move to next stage in our spiritual path...!! 
    
    """

    st.info(content)

content2 ="""Below you can find some of the apps I built in python.
Feel free to contact me anytime..! Thats how I work with python.

"""
st.write(content2)

col3,col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])