# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import json
import requests


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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.title("Scanlah Database")

    api_urls = [];

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

        """"""
        inventory_api_key = st.secrets["CALL_INVENTORY_ID"]

        response = requests.get(inventory_api_key)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON (assuming it's a JSON response)
            data = response.json()

            """"""
            for i in range(1, len(data)):
                st.write(data[i]["value"])

        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
