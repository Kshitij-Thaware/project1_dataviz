import matplotlib.pyplot as plt
import streamlit as st

def display_barchart(column):
    """
    column: dataframe column
    """
    figure = plt.figure()
    column.value_counts().plot(kind='bar')
    st.pyplot(figure)