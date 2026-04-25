import plotly.graph_objects as go
import plotly as px
import pandas as pd

data = dict(type='choropleth',
			locations=['AZ', 'CA', 'LA'],
			locationmode = 'USA-states',
			colorscale= 'portland',
			text = ['Arizona', 'California', 'los Angeles'],
			z =[1.0,2.0,3.0],
			colorbar = {'title': 'colorbar title goes here'}
			)

layout = dict(geo={'scope': 'usa'})
choromap = go.Figure(data = [data], layout = layout)
#choromap.show()

df = pd.read_csv('2011_US_AGRI_Exports.csv')
print(df.head())