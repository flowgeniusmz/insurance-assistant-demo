import streamlit as st

def get_pagelinks():

    container_pagelinks = st.container()
    with container_pagelinks:
        st.page_link("pages/1_AI_Assistant.py", label="AI Assistant", icon="🌐")
        st.page_link("pages/2_Insurance_Claim_Prediction.py", label="Page 2", icon="🌐")