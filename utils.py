import streamlit as st
import subprocess
import json
from tinydb import TinyDB, Query
import config
from pathlib import Path

db = TinyDB("labs.json")
Labs = Query()


def get_db_labs():
    all_labs = db.all()
    lab_list = []

    for lab in all_labs:
        lab_list.append(lab['name'])

    return lab_list

def db_add_lab(lab_details):
    return db.insert(lab_details)

def db_update_lab():

    return

def db_del_lab():

    return

def search_lab_details(lab_name):
    return db.search(Labs.name == lab_name)

def all_lab_details():
    return db.all()

def clab_function(lab_function, lab_option):
    lab_details = db.search(Labs.name == lab_option)[0]
    labs_parent_dir = config.appRoot + config.labRoot
    lab_full_path = f"{labs_parent_dir}/{lab_details['localLabFolder']}/{lab_details['labFile']}"
    lab_path_check = Path(lab_full_path)
    if lab_path_check.is_file():
        return subprocess.run(['sudo', 'containerlab', lab_function, '-t', lab_full_path], text=True, check=True, capture_output=True)
    else:
        return lab_full_path

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


def connect_to_device(dev_option):

    hostname = dev_option
    port = 22
    user = 'arista'
    passwd = 'arista'

    try:
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=user, password=passwd)
        while True:
            try:
                cmd = input(f'{hostname} - $> ')
                if cmd == 'exit':
                    break
                stdin, stdout, stderr = client.exec_command(cmd)
                return st.code(stdout)
                print(stdout.read().decode())
            except KeyboardInterrupt:
                break
        client.close()
    except Exception as err:
        print(std(err))