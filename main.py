import streamlit as st
from scrape import scrape_website

st.title("Web Scraper AI")
url = st.text_input("Enter a website URL")

if st.button("Scrape Site"):
    st.write("Button is pressed")
    result = scrape_website(url)
    print(result)
