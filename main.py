import streamlit as st
from scrape import scrape_website, extract_body, clean_body, split_dom_content
from parse import parse_with_ollama

st.title("AI Website Scraper")
url = st.text_input("Enter the Website URL to scrape")

if st.button("Scrape Website"):
    st.write("Scraping Website...")

    result = scrape_website(url)
    body_content = extract_body(result)
    cleaned_content = clean_body(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Enter the description of the content you want to parse?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing Content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_content = parse_with_ollama(dom_chunks, parse_description)

            st.write(parsed_content)
