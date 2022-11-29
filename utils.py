import streamlit as st
import subprocess
import json
from tinydb import TinyDB, Query

db = TinyDB("labs.json")
Labs = Query()

def get_db_labs():
    all_labs = db.all()
    lab_list = []

    for lab in all_labs:
        lab_list.append(lab['name'])

    return lab_list

def db_add_lab():

    return

def db_update_lab():

    return

def db_del_lab():

    return

def search_lab_details(lab_name):
    return db.search(Labs.name == lab_name)

def load_lab(lab_option):
    if lab_option == 'Arista':
        return subprocess.run(['sudo', 'containerlab', 'deploy', '-t', 'arista.labtest.yml'], text=True, check=True, capture_output=True)

def check_run(lab_option):
    if lab_option == 'Arista Lab':
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