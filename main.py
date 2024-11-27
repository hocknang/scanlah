# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.title("Title")

    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [25, 30, 35, 40],
        "Country": ["USA", "UK", "Canada", "Australia"],
        "Profession": ["Engineer", "Doctor", "Artist", "Scientist"]
    }

    df = pd.DataFrame(data)

    st.subheader("Interactive Table with Filters for All Columns")

    # Configure Ag-Grid options
    gb = GridOptionsBuilder.from_dataframe(df)

    # Enable filtering on all columns
    gb.configure_default_column(filter=True)  # Enables filters for all columns
    gb.configure_grid_options(domLayout='normal')  # Makes the table responsive

    # Build the grid options
    grid_options = gb.build()

    # Render Ag-Grid table
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=False,
        update_mode="value_changed",
        fit_columns_on_grid_load=True,
    )

    # Get filtered and displayed data
    filtered_data = grid_response['data']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
