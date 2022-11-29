import streamlit as st
from tinydb import TinyDB, Query
import utils

db = TinyDB("labs.json")
Labs = Query()

def get_db_labs():
    all_labs = db.all()
    lab_list = []

    for lab in all_labs:
        lab_list.append(lab['name'])

    return lab_list

def search_lab_details(lab_name):
    return db.search(Labs.name == lab_name)

def load_page():
    st.title("Labs List")

    option = st.selectbox(
        'Currently installed labs',
        get_db_labs()
    )

    st.write("Select a lab to view it's details, or use the checkbox below to see all labs")

    all_labs = st.checkbox('Get All Labs')

    if st.button('Get Lab Details'):
        if all_labs == True:
            lab_details = db.all()
        else:
            lab_details = db.search(Labs.name == option)
        
        for lab in lab_details:
            with st.container():
                lab_table = f"""
                | **Field** | Value |
                | --- |--- |
                | **Lab Name** | {lab['name']} |
                | **Description** | {lab['description']} |
                | **Author** | {lab['author']} |
                | **Git Enabled** | {lab['git']} |
                | **Local Folder** | {lab['localLabFolder']} |
                | **Git Repo** | {lab['gitRepo']} |
                """
                st.markdown(utils.format_md_table(), unsafe_allow_html=True)
                st.markdown(lab_table)
                st.write("---")

                

if __name__ == "__main__":
    load_page()