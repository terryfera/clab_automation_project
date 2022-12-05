import streamlit as st
import utils


def load_page():
    host_dict = {
        "172.20.20.2":"show ip route",
        "172.20.20.3":"show ip route",
    }
    with st.form("ssh connection"):
        st.write("Lab Devices")
        option = st.selectbox(
            'Select a Device:', list(host_dict.keys())
        )


if __name__ == "__main__":
    load_page()