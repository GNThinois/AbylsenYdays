import streamlit as st
import pandas as pd
import config
import wamp
import ftp_to_wamp
from sqlalchemy import create_engine
from datetime import datetime

user = config.WAMP_username
pw = config.WAMP_password
db = config.WAMP_database

def main():
    """
    Streamlit application to display job offers from the WAMP database with filters.
    """
    # Set the title of the Streamlit app
    st.title("Job Offers")

    # Write a subtitle for the data section
    st.write("### Data from WAMP server")

    # Fetch the data from the WAMP server
    df = wamp.fetch_data_from_wamp()

    # Convert "Date fin" column to datetime format
    df['Date fin'] = pd.to_datetime(df['Date fin'])

    # Add filters for Lieu, Expérience, Contrat, and Secteur using Streamlit's sidebar
    st.sidebar.header("Filters")

    # Get unique values for each filter and create multiselects in the sidebar
    unique_values_lieu = sorted(df['Lieu'].unique())
    selected_values_lieu = st.sidebar.multiselect("Select values for Lieu", unique_values_lieu, unique_values_lieu, key="filter1")

    unique_values_experience = sorted(df['Expérience'].unique())
    selected_values_experience = st.sidebar.multiselect("Select values for Expérience", unique_values_experience, unique_values_experience, key="filter2")

    unique_values_contrat = sorted(df['Contrat'].unique())
    selected_values_contrat = st.sidebar.multiselect("Select values for Contrat", unique_values_contrat, unique_values_contrat, key="filter3")

    unique_values_secteur = sorted(df['Secteur'].unique())
    selected_values_secteur = st.sidebar.multiselect("Select values for Secteur", unique_values_secteur, unique_values_secteur, key="filter4")

    # Filter the DataFrame based on the selected values
    filtered_df = df[(df['Lieu'].isin(selected_values_lieu)) &
                     (df['Expérience'].isin(selected_values_experience)) &
                     (df['Contrat'].isin(selected_values_contrat)) &
                     (df['Secteur'].isin(selected_values_secteur))]

    # Filter the DataFrame to only display rows where "Date fin" is not a passed date
    current_date = datetime.now()
    filtered_df = filtered_df[filtered_df['Date fin'] >= current_date]

    # Display the filtered DataFrame, centered horizontally
    st.dataframe(filtered_df.style.set_properties(**{'margin': '0 auto'}))

    # Add the "Actualiser les offres" button
    refresh_button = st.button("Actualiser les offres")

    # Execute the ftp_to_wamp function when the button is clicked
    if refresh_button:
        ftp_to_wamp.main()
        st.experimental_rerun()

if __name__ == "__main__":
    main()
