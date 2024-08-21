import streamlit as st
import pandas as pd
import plotly.express as px
# import os

# # Set the working directory
# os.chdir('h:\\My Drive\\IBM Data Science G2\\02- Data Visualization\\DV_03\\03- Assignments')

# Load data
df = pd.read_csv('canadian_immegration_data.csv')

# Title of the app
st.title('Canadian Immigration Data')

# Horizontal rule
st.markdown('---')

# Radio buttons for selection
option = st.radio('Select a Category', ['Continents', 'Top10Regions', 'Top10Countries'])

# Plotting based on selection
if option == 'Continents':
    fig = px.histogram(df, x='Continent', y='Total', title='Immigration to Canada by Region', histfunc='avg', 
                       category_orders={'Continent': ['Northern America', 'Asia', 'Europe', 'Latin America and the Caribbean', 'Africa', 'Oceania']})
elif option == 'Top10Regions':
    top10regions = df.groupby('Region')['Total'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top10regions, x='Region', y='Total', title='Immigration to Canada by Region')
else:
    top10countries = df.nlargest(10, 'Total').reset_index()[['Country', 'Total']]
    top10countries.loc[2, 'Country'] = 'United Kingdom'
    fig = px.bar(top10countries, x='Country', y='Total', title='Immigration to Canada by Country')

# Display the plot
st.plotly_chart(fig)

