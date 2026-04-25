import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

 #        COUNTRY  GDP (BILLIONS) CODE
#0     Afghanistan           21.71  AFG
#1         Albania           13.40  ALB
#2         Algeria          227.80  DZA
#3  American Samoa            0.75  ASM
#4         Andorra            4.80  AND

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\geographical_plot\2014_World_GDP')

data = dict(type = 'choropleth',
            locations = df['CODE'],
            locationmode = 'ISO-3',
            colorscale= 'portland',
            text = df[['COUNTRY']],
            z = df['GDP (BILLIONS)'],
            colorbar = dict(title = 'World GDP')
            )
layout = dict(
    title='GDP Values in Billions',
    geo=dict(scope='world', projection={"type": 'kavrayskiy7'}), 
)

choromap = go.Figure(data=[go.Choropleth(**data)], layout=layout)
choromap.show()
