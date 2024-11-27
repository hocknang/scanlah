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

    st.subheader("Table with Borders for Each Cell")

    # Configure Ag-Grid options
    gb = GridOptionsBuilder.from_dataframe(df)

    # Enable filtering for all columns
    gb.configure_default_column(filter=True)  # Add filter capability
    gb.configure_grid_options(domLayout="autoHeight")  # Dynamic table height

    # Build grid options
    grid_options = gb.build()

    # Render Ag-Grid with a theme that adds borders
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=False,
        update_mode="value_changed",
        fit_columns_on_grid_load=True,  # Adjust column width
        height=300,  # Fixed height
        theme="streamlit",  # Theme that applies borders to cells
    )

    # Extract filtered data
    filtered_data = grid_response["data"]

    st.subheader("Filtered Data Output:")
    st.dataframe(filtered_data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
