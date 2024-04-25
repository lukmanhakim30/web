import streamlit as st

username = "admin"
password = "admin"

def main() :
    st.title("halaman login")

    username = st.text_input("username")
    password = st.text_input("password", type="password")

if __name__ == "__main__" :
   main()