# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import json


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

    # Predefined usernames and passwords (for demonstration purposes)
    USER_CREDENTIALS = {
        "user1": "password1",
        "user2": "password2",
        "admin": "admin123",
    }

    # Login function
    def login(username, password):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return True
        return False

    # Initialize session state for authentication
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False  # Not authenticated by default
        st.session_state["username"] = ""  # To store the username

    # Authentication flow
    if not st.session_state["authenticated"]:
        st.title("Login")

        # Input fields for username and password
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Login button
        if st.button("Login"):
            if login(username, password):
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success("Login successful!")
                st.experimental_rerun()  # Refresh the page to show the authenticated state
            else:
                st.error("Invalid username or password")
    else:
        st.title(f"Welcome, {st.session_state['username']}!")
        st.write("You are logged in.")

        # Logout button
        if st.button("Logout"):
            st.session_state["authenticated"] = False
            st.session_state["username"] = ""
            st.experimental_rerun()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
