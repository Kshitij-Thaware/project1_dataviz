import streamlit as st
import pandas 

st.title('My first python data visualization website')

from services.barchart import display_barchart
from services.hist import display_histogram

upload_file = st.file_uploader("Upload your CSV file", type=["csv"])

if upload_file is not None:

    data = pandas.read_csv(upload_file)
    st.write(data)

    all_col = data.columns.to_list()
    selected_col = st.selectbox("Select columns to visualize", all_col)

    if pandas.api.types.is_numeric_dtype(data[selected_col]):
        st.write('selected columns', selected_col, 'is numeric type')


        display_histogram(data[selected_col])


    else:
        st.write('selected columns', selected_col, 'is nominal type')

        display_barchart(data[selected_col])

         