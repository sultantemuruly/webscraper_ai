import streamlit as st

st.title("Web Scraper AI")
url = st.text_input("Enter a website URL")

if st.button("Scrape Site"):
    st.write("Button is pressed")
