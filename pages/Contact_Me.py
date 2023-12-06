import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv('topics.csv')

st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Your email address')
    option = st.selectbox(
        'What topic would you like to discuss?',
        df["topic"])
    raw_message = st.text_area('Your message')
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
topic {option}
{raw_message}
 """
    button = st.form_submit_button('Submit')
    print(button)
    if button:
        send_email(message)
        st.info('Your email was sent successfully')