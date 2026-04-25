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

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\geographical_plot\2011_US_AGRI_Exports.csv')

data2 = dict(type='choropleth',
             locations=df['code'],
             locationmode='USA-states',        # was 'USA-state' (missing s)
             colorscale='portland',
             text=df['text'],
             z=df['total exports'],             # z should be a numeric column
             colorbar=dict(title='2011 Agricultural Exports in USA')  # lowercase colorbar, dict() not {}
             )

layout = dict(geo={'scope': 'usa'})

choromap2 = go.Figure(dict (title='Agro Us', data=[go.Choropleth(data2)]), geo = dict(layout=layout))
choromap2.show()
