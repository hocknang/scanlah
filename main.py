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

    st.subheader("Table with Borders Around Every Cell")

    # Configure Ag-Grid options
    gb = GridOptionsBuilder.from_dataframe(df)

    # Enable filtering for all columns
    gb.configure_default_column(filter=True)  # Add filter capability
    gb.configure_grid_options(domLayout="autoHeight")  # Dynamic table height

    # Add custom CSS for borders in each cell
    custom_css = """
        .ag-theme-material .ag-cell,
        .ag-theme-material .ag-header-cell {
            border: 1px solid black !important;  /* Border for each cell */
            padding: 8px;  /* Optional: control the cell padding */
        }
        .ag-theme-material .ag-header-cell {
            font-weight: bold;  /* Optional: Make header text bold */
            text-align: center;  /* Optional: Center-align header text */
        }
        .ag-theme-material .ag-row {
            border-bottom: 1px solid #ddd;  /* Optional: add row borders */
        }
    """

    # Set the CSS to apply to the grid container
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

    # Build grid options
    grid_options = gb.build()

    # Render Ag-Grid with the custom style
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=False,
        update_mode="value_changed",
        fit_columns_on_grid_load=True,  # Adjust column width
        height=300,  # Fixed height
        theme="material",  # Base theme
    )



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
