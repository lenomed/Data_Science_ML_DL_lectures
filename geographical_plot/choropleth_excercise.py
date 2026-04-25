import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

 #   Country  Power Consumption KWH                        Text
#0          China           5.523000e+12     China 5,523,000,000,000
#1  United States           3.832000e+12    United 3,832,000,000,000
#2       European           2.771000e+12  European 2,771,000,000,000
#3         Russia           1.065000e+12    Russia 1,065,000,000,000
#4          Japan           9.210000e+11       Japan 921,000,000,000
#Press any key to continue . . .

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\geographical_plot\2014_World_Power_Consumption')

data = dict(type = 'choropleth',
            locations = df['Country'],
            locationmode = 'country names',
            colorscale= 'portland',
            text = df[['Text']],
            z = df['Power Consumption KWH'],
            colorbar = dict(title = '2014 World Power Consumption')
            )
layout = dict(
    title='Power Consumption World Wide',
    geo=dict(scope='world', projection={"type": 'kavrayskiy7'}), 
)


choromap = go.Figure(data=[go.Choropleth(**data)], layout=layout)
choromap.show()
