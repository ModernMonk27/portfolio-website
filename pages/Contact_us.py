import streamlit as st

from Send_mail import send_email

import pandas

df = pandas.read_csv("topics.csv")



st.header("Contact Me")

with st.form(key="mail_form"):

    mail = st.text_input("Your Email Address :")
    options = st.selectbox("What is your Topic About :",df["topic"])
    raw_messege = st.text_area("Message :")
    message = f"""\
Subject : New message from {mail}

From : {mail}
{raw_messege}
"""
    btn = st.form_submit_button("Submit")

    if btn:
        send_email(message)
        st.info("Your message is sent succesfully..!!")