import streamlit as st
import os
import subprocess
#import requests

"""
# WELCOME TO LAB GENERATOR

The very fisrt dynamic Lab generator

The tool provides 2 options:

* Spin up pre-defined labs
* Spin up an on demand custom lab

Supported Vendors so far

* Cisco (IOS-XE and IOS-XR)
* Arista cEOS
* Nokia SRL

"""

pre_defined_total = 0

name = st.text_input('Enter your name: ')

option = st.selectbox(
    'What would like to do:', ('', 'Use a pre-defined Lab', 'Create a new custom Lab', 'Other')
)



def take_action(opt):
    #lab_spinup_cmd = f'containerlab deploy -t {lab_file}'
    #lab_cmd_temp = subprocess.Popen([lab_spinup_cmd], stdout= subprocess.PIPE)
    if opt == 'Use a pre-defined Lab':
        lab_option = st.selectbox(
        'Which lab would you like to use?', ('OSPF Lab', 'BGP Lab', 'Failover Lab'))
        return opt
    elif opt == 'Create a new custom Lab':
        lab_option = st.selectbox(
        'What Type of lab would you like to create?', ('Routing', 'Switching', 'Topology Map'))
        return opt
    elif opt == 'Other':
        return opt
    else:
        return 'Please Select one Option'





st.write('You have selected:', take_action(option))



