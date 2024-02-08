import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

# ユーザー情報の設定
users = ["kikagaku"]
passwords = ["kikagaku"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(users, users, hashed_passwords, "leaderboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.write(f'Welcome *{name}*')
    st.title("Leaderboard")
elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")

