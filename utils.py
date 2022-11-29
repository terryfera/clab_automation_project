import streamlit as st
import subprocess
import json

def load_lab(lab_option):
    if lab_option == 'Arista':
        return subprocess.run(['sudo', 'containerlab', 'deploy', '-t', 'arista.labtest.yml'], text=True, check=True, capture_output=True)

def check_run(lab_option):
    if lab_option == 'Arista':
        return subprocess.run(['sudo', 'containerlab', 'inspect', '-t', 'arista.labtest.yml'], text=True, check=True, capture_output=True)

def destroy_lab(lab_option):
    if lab_option == 'Arista':
        return subprocess.run(['sudo', 'containerlab', 'destroy', '-t', 'arista.labtest.yml'], text=True, check=True, capture_output=True)

def get_running_labs():
    output = subprocess.run(['sudo', 'containerlab', 'inspect', '--all', '-f', 'json'], text=True, check=True, capture_output=True)
    running_labs = json.loads(output.stdout)
    return running_labs

def format_md_table():
    table_style = """
    <style>
    table:nth-of-type(1) {
        display:table;
        width:100%;
    }
    table:nth-of-type(1) th:nth-of-type(2) {
        width:65%;
    }
    </style>
    """
    return table_style


def running_lab_status(status):
    if status.lower() == "running":
        status_markdown = f"""<span style="color:green">{status}</span>"""
    else:
        status_markdown = f"""<span style="color:red">{status}</span>"""
    
    return status_markdown