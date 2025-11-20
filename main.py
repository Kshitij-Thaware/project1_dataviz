import streamlit as st
import pandas 

st.title('My first python data visualization website')


upload_file = st.file_uploader("Upload your CSV file", type=["csv"])

if upload_file is not None:

    data = pandas.read_csv(upload_file)
    st.write(data)

    all_columns = data.columns.to_list()
    selected_col = st.selectbox("Select columns to visualize", all_columns)

    if pandas.api.types.is_numeric_dtype(data[selected_col]):
        st.write('selected columns', selected_col, 'is numeric type')


    else:
        st.write('selected columns', selected_col, 'is nominal type')

        