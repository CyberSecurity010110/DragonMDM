# DragonMDM Dashboard

## Overview

DragonMDM is a Mobile Device Management (MDM) dashboard built using Streamlit. It allows administrators to manage and monitor mobile devices, enforce policies, track device locations, and generate compliance reports.

## Features

- Device Enrollment
- Remote Management
- Policy Enforcement
- Security Monitoring
- Device Inventory
- Geolocation Tracking
- Compliance Reporting

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cybersecurity010110/DragonMDM.git
   cd DragonMDM
assistant Avatar

Abbye

Let's add a feature for Compliance Reporting to the MDM app. This feature will allow administrators to generate compliance reports for enrolled devices, ensuring that they adhere to the organization's security policies.

Here's the updated project structure and code:

DragonMDM/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── devices.db
├── static/
│   └── css/
│       └── style.css
└── scripts/
    └── device_management.py
    └── geolocation_tracking.py
    └── inventory_management.py
    └── compliance_reporting.py

1. app.py

This is the main Streamlit app that integrates all the features, including the new Compliance Reporting feature.

python

import streamlit as st
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import sqlite3
import folium
from streamlit_folium import folium_static
from scripts.device_management import enroll_device, lock_device, wipe_device
from scripts.inventory_management import get_device_inventory
from scripts.geolocation_tracking import get_device_locations
from scripts.compliance_reporting import generate_compliance_report

# Set page configuration
st.set_page_config(page_title="DragonMDM Dashboard", layout="wide")
st.title("DragonMDM Dashboard")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Home", "Device Enrollment", "Remote Management", "Policy Enforcement", "Security Monitoring", "Compliance Reporting"],
        icons=["house", "person-plus", "tools", "shield-lock", "shield-check", "file-earmark-check"],
        menu_icon="cast",
        default_index=0,
    )

# Home page
if selected == "Home":
    st.header("Welcome to the DragonMDM Dashboard")
    st.write("Use the sidebar to navigate through the different sections.")

# Device Enrollment page
elif selected == "Device Enrollment":
    st.header("Device Enrollment")
    st.write("Enroll new devices here.")

    with st.form(key='enrollment_form'):
        device_id = st.text_input("Device ID")
        user_name = st.text_input("User Name")
        submit_button = st.form_submit_button(label='Enroll Device')

    if submit_button:
        enroll_device(device_id, user_name)
        st.success("Device enrolled successfully!")

# Remote Management page
elif selected == "Remote Management":
    st.header("Remote Management")
    st.write("Manage devices remotely here.")

    device_id = st.text_input("Enter Device ID")

    if st.button("Lock Device"):
        lock_device(device_id)
        st.success("Device locked successfully!")

    if st.button("Wipe Device"):
        wipe_device(device_id)
        st.success("Device wiped successfully!")

# Policy Enforcement page
elif selected == "Policy Enforcement":
    st.header("Policy Enforcement")
    st.write("Enforce policies on devices here.")

    device_id = st.text_input("Enter Device ID")

    password_quality = st.selectbox("Password Quality", ["Low", "Medium", "High"])
    min_password_length = st.slider("Minimum Password Length", 4, 16)

    if st.button("Enforce Policy"):
        st.write(f"Enforcing policy on device {device_id}...")
        st.write(f"Password Quality: {password_quality}")
        st.write(f"Minimum Password Length: {min_password_length}")
        # Add your code to enforce policy here
        st.success("Policy enforced successfully!")

# Security Monitoring page
elif selected == "Security Monitoring":
    st.header("Security Monitoring")
    st.write("Monitor device security here.")

    device_id = st.text_input("Enter Device ID")

    if st.button("Check Security Status"):
        st.write(f"Checking security status for device {device_id}...")
        # Add your code to check security status here
        st.success("Security status checked successfully!")

    # Display device locations on a map
    st.subheader("Device Locations")
    device_locations = get_device_locations()
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=5)
    for device in device_locations:
        folium.Marker(
            location=[device["latitude"], device["longitude"]],
            popup=device["device_id"],
            icon=folium.Icon(icon="info-sign")
        ).add_to(m)
    folium_static(m)

    # Display device inventory
    st.subheader("Device Inventory")
    df = get_device_inventory()
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()
    gb.configure_side_bar()
    grid_options = gb.build()
    AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        fit_columns_on_grid_load=True,
    )

# Compliance Reporting page
elif selected == "Compliance Reporting":
    st.header("Compliance Reporting")
    st.write("Generate compliance reports for enrolled devices.")

    if st.button("Generate Report"):
        report = generate_compliance_report()
        st.write(report)
        st.success("Compliance report generated successfully!")

2. requirements.txt

List of dependencies for the project.

streamlit
streamlit-option-menu
streamlit-aggrid
streamlit-folium
pandas
sqlite3
folium

3. README.md

Project documentation.

markdown

# DragonMDM Dashboard

## Overview

DragonMDM is a Mobile Device Management (MDM) dashboard built using Streamlit. It allows administrators to manage and monitor mobile devices, enforce policies, track device locations, and generate compliance reports.

## Features

- Device Enrollment
- Remote Management
- Policy Enforcement
- Security Monitoring
- Device Inventory
- Geolocation Tracking
- Compliance Reporting

## Installation

1. Clone the repository:
   git clone https://github.com/Cybersecurity010110/DragonMDM.git
   cd DragonMDM


2. Install the dependencies:

    pip install -r requirements.txt

3.  Run the Streamlit app:

    streamlit run app.py

     use the sidebar to navigate through the different sections of the dashboard. Each section provides specific functionality for managing and monitoring mobile devices.
    
   ### contributing
    
      Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


