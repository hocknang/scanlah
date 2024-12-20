# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import json
import requests
import uuid
import schedule
import time


def test():
    json_data = '''
        [
          {"Name": "Alice", "Age": 25, "Country": "USA", "Profession": "Engineer"},
          {"Name": "Bob", "Age": 30, "Country": "UK", "Profession": "Doctor"},
          {"Name": "Charlie", "Age": 35, "Country": "Canada", "Profession": "Artist"},
          {"Name": "Diana", "Age": 40, "Country": "Australia", "Profession": "Scientist"}
        ]
        '''

    # Convert JSON string to Python list of dictionaries
    data = json.loads(json_data)

    df = pd.DataFrame(data)

    st.subheader("Table with Scrollable View and No Whitespace")

    # Configure Ag-Grid options
    gb = GridOptionsBuilder.from_dataframe(df)

    # Enable filtering for all columns
    gb.configure_default_column(filter=True)  # Add filter capability
    gb.configure_grid_options(domLayout="normal")  # Use normal layout for scrolling

    # Manually configure column definitions with customized filter alignment
    column_defs = [
        {
            "headerName": col,
            "field": col,
            "filter": "agTextColumnFilter" if col != "Age" else "agNumberColumnFilter",
            "filterParams": {
                "buttons": ["reset", "apply"],
            },
            "cellStyle": {
                "textAlign": "left",  # Ensure text columns are aligned to the left
            },
        }
        for col in df.columns
    ]

    # Align the "Age" filter to the right (filter alignment)
    column_defs[1]["filterParams"] = {
        "textAlign": "right"  # Align Age filter to the right
    }

    # Apply the custom column definitions
    grid_options = gb.build()
    grid_options["columnDefs"] = column_defs  # Set custom columnDefs

    # Custom CSS to remove whitespace (padding/margin) from the table
    custom_css = """
            .ag-theme-material .ag-cell,
            .ag-theme-material .ag-header-cell {
                border: 1px solid black !important;  /* Border for each cell */
                padding: 0px !important;  /* Remove cell padding */
                margin: 0px !important;  /* Remove margin */
            }
            .ag-theme-material .ag-header {
                margin: 0px !important;  /* Remove header margin */
            }
            .ag-theme-material .ag-row {
                border-bottom: 1px solid #ddd !important;  /* Optional: add row borders */
            }
            .ag-theme-material .ag-body-viewport {
                padding: 0px !important;  /* Remove padding from viewport */
            }
        """

    # Apply custom CSS to the grid container
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

    # Render Ag-Grid with a fixed height and scrollbar
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=False,
        update_mode="value_changed",
        fit_columns_on_grid_load=True,  # Adjust column width
        theme="material",  # Theme that applies borders to cells
    )


def call_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"API Response from {url}: {response.json()}")
        else:
            print(f"API Call Failed for {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with {url}: {e}")

#Schedule
def call_api_status():
    global counter, exit_flag
    st.write("hello world" + str(counter))

    counter = counter + 1

def call_multiple_apis(urls):
    # Call each API one after the other
    for url in urls:
        call_api(url)

def print_hi(name):
    st.title("Scanlah Database")

    data_records = []

    uuid_records = []

    status_records = []

    # Flag to control the scheduler
    exit_flag = False

    counter = 0

    # Check if the user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

        # Login button
    if st.button("Login"):
        # Update the session state to show that the user is logged in
        st.session_state['logged_in'] = True

        # Display a welcome message if logged in
        if st.session_state['logged_in']:
            st.success("Welcome! You are now logged in.")

            response = requests.get("https://script.google.com/macros/s/"
                                    "AKfycbzy1rIffd9zFVr1z9IkbRoQi71vSdRT2yKfswT4mRAoW0JwF8R_26cwSuPCvbfgWF9L/"
                                    "exec?pageAction=retrieveAllUniqueID_Inventory")

            if response.status_code == 200:
                # Parse the response JSON (assuming it's a JSON response)
                data = response.json()

                for i in range(1, len(data)):

                    random_uuid = uuid.uuid4()
                    uuid_records.append(random_uuid)

                    callURL = "https://script.google.com/macros/s/" \
                              "AKfycbzy1rIffd9zFVr1z9IkbRoQi71vSdRT2yKfswT4mRAoW0JwF8R_26cwSuPCvbfgWF9L/exec?" \
                              "pageAction=retrieveSingleRecord&databaseName=INVENTORY&uniqueId=" + data[i]["value"] + \
                              "&identifyID=" + str(random_uuid)

                    data_records.append(callURL)

                    callStatus = "https://script.google.com/macros/s/" \
                                 "AKfycbzy1rIffd9zFVr1z9IkbRoQi71vSdRT2yKfswT4mRAoW0JwF8R_26cwSuPCvbfgWF9L/exec?" \
                                 "pageAction=getUniqueStatus&uniqueId=" + str(random_uuid)

                    status_records.append(callStatus)

                    if i == len(data) - 1:  # Check if `i` is the last index
                        st.write("last data: " + data[i]["value"])

                for m in range(0, len(data_records)):
                    st.write("url: " + data_records[m])

                for o in range(0, len(status_records)):
                    st.write("status: " + data_records[m])

                st.write("Calling APIs...")

                call_multiple_apis(data_records)

                # Schedule the API call every 2 minutes
                schedule.every(2).minutes.do(call_api_status)

                while True:
                    schedule.run_pending()
                    if exit_flag:  # Stop the loop if all APIs are called
                        print("Exiting scheduler loop.")
                        break
                    time.sleep(1)  # Sleep to reduce CPU usage

            else:
                st.error(f"Failed to fetch data. Status code: {response.status_code}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("hello world")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
