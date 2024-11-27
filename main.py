# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.


    # Sample Data
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "Country": ["USA", "UK", "Canada"],
        "Profession": ["Engineer", "Doctor", "Artist"]
    }

    df = pd.DataFrame(data)

    st.subheader("Interactive Table with Column Filtering")

    # Configure Ag-Grid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(filter=True, editable=True)  # Enable column filtering
    gb.configure_grid_options(domLayout='normal')  # Make table responsive

    grid_options = gb.build()

    # Display the table
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        update_mode="value_changed",
        enable_enterprise_modules=False,
        fit_columns_on_grid_load=True,
    )

    # Extract filtered data from the table
    filtered_data = grid_response['data']

    st.write("Filtered Data:")
    st.dataframe(filtered_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
