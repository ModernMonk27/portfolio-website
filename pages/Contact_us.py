import streamlit as st

st.header("Contact Me")

with st.form(key="mail_form"):

    mail = st.text_input("Your Email Address :")
    messege = st.text_area("Message :")
    btn = st.form_submit_button("Submit")

    if btn:
        print("I'am pressed ..!1")