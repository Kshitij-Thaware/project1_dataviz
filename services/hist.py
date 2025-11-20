import matplotlib.pyplot as plt
import streamlit as st

def display_histogram(column):
    """
    column : dataframe column
    """


    figure = plt.figure()
    plt.hist(column, bins=4, edgecolor='black')
    st.pyplot(figure)

    # final version