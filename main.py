import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("Web Scraper AI")
url = st.text_input("Enter a website URL")

if st.button("Scrape Site"):
    st.write("Button is pressed")
    
    result = scrape_website(url)
    body_content =  extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content",  cleaned_content, height=300)
