import streamlit as st



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