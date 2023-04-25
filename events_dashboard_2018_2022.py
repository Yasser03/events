import pandas as pd
import plotly.express as px
import streamlit as st

import warnings

warnings.filterwarnings("ignore")

# Load data from CSV file
data = pd.read_csv(r"2018-2022__modified_preprocessed_data.csv")

def total_participants_by_year(data):
    yearly_data = data.groupby('year').size().reset_index(name='count')
    fig = px.bar(yearly_data, x='year', y='count', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def participants_by_gender_and_year(data):
    gender_yearly_data = data.groupby(['year', 'gender']).size().reset_index(name='count')
    fig = px.bar(gender_yearly_data, x='year', y='count', text='count', color='gender', barmode='group')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def unique_events_by_year(data):
    events_yearly_data = data.groupby('year')['event'].nunique().reset_index(name='count')
    fig = px.bar(events_yearly_data, x='year', y='count', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def cities_by_year(data):
    cities_yearly_data = data.groupby('year')['city'].nunique().reset_index(name='count')
    fig = px.bar(cities_yearly_data, x='year', y='count', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def nationalities_by_year(data):
    nationalities_yearly_data = data.groupby('year')['nationality'].nunique().reset_index(name='count')
    fig = px.bar(nationalities_yearly_data, x='year', y='count', text='count')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig)

def participants_map(data):
    # You'll need to adjust this code to match the actual structure and content of your dataset
    # Replace 'latitude' and 'longitude' with the actual column names containing the coordinates
    fig = px.scatter_geo(data, lat='latitude', lon='longitude', color='nationality', hover_name='city', size='count', projection='natural earth')
    st.plotly_chart(fig)

def age_histogram(data):
    fig = px.histogram(data, x='age', nbins=60, histnorm='percent', color='year', title='Age Distribution')
    fig.update_xaxes(range=[0, data['age'].max()])
    st.plotly_chart(fig)

def top_events_by_year(data):
    events_data = data.groupby(['year', 'event']).size().reset_index(name='count')
    events_data = events_data.sort_values(by=['year', 'count'], ascending=[True, False])
    top_events_data = pd.DataFrame(columns=['year', 'event', 'count'])
    for year in data['year'].unique():
        top_events_data = top_events_data.append(events_data[events_data['year'] == year].head(10))
    fig = px.bar(top_events_data, x='event', y='count', color='year', barmode='group')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title='Top 10 events per year')
    st.plotly_chart(fig)

def top_cities_by_year(data):
    cities_data = data.groupby(['year', 'city']).size().reset_index(name='count')
    cities_data = cities_data.sort_values(by=['year', 'count'], ascending=[True, False])
    top_cities_data = pd.DataFrame(columns=['year', 'city', 'count'])
    for year in data['year'].unique():
        top_cities_data = top_cities_data.append(cities_data[cities_data['year'] == year].head(10))
    fig = px.bar(top_cities_data, x='city', y='count', color='year', barmode='group')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title='Top 10 cities per year')
    st.plotly_chart(fig)

def top_nationalities_by_year(data):
    nationalities_data = data.groupby(['year', 'nationality']).size().reset_index(name='count')
    nationalities_data = nationalities_data.sort_values(by=['year', 'count'], ascending=[True, False])
    top_nationalities_data = pd.DataFrame(columns=['year', 'nationality', 'count'])
    for year in data['year'].unique():
        top_nationalities_data = top_nationalities_data.append(nationalities_data[nationalities_data['year'] == year].head(10))
    fig = px.bar(top_nationalities_data, x='nationality', y='count', color='year', barmode='group')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', title='Top 10 nationalities per year')
    st.plotly_chart(fig)

st.set_page_config(page_title="ADSC Events Dashboard", layout="wide")

st.title("ADSC Community Events Dashboard")

# Add a year filter to the dashboard
# year = st.sidebar.selectbox('Select a year', data['year'].unique())

# Display the answers to each question using the functions you've created
st.header("1. Total number of participants from 2018 to 2022")
st.write("Total Participants: ", data.shape[0])
total_participants_by_year(data)

st.header("2. Total number of participants by gender from 2018 to 2022")
participants_by_gender_and_year(data)

st.header("3. Total number of unique events from 2018 to 2022")
unique_events_by_year(data)

st.header("4. Total number of cities from 2018 to 2022")
cities_by_year(data)

st.header("5. Total number of nationalities from 2018 to 2022")
nationalities_by_year(data)

st.header("6. Age distribution histogram from 2018 to 2022")
age_histogram(data)

st.header("7. Top 10 cities per year")
top_cities_by_year(data)

st.header("8. Top 10 nationalities per year")
top_nationalities_by_year(data)

st.header("9. Top 10 events per year")
top_events_by_year(data)

# st.header("10. Map of participants per city, nationality, and event from 2018 to 2022")
# participants_map(data)
