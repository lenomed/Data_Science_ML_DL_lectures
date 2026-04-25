import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import numpy as np
import pandas as pd

df= pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
fig = px.scatter(df, x='A', y='B', size_max=45)
fig.update_traces(marker=dict(size=12, color='red'))
#fig.show()



df2 = pd.DataFrame({'Categories':['A','B','C'],'Values': [32,43,50]})
fig_b = px.bar(df2, x='Categories', y='Values')
fig_b.update_traces(width=0.2)
fig_b.show()

print(df2.head())
#titanic = sns.load_dataset('titanic')
#fig = px.histogram(titanic, x='fare', nbins=30)
#fig.show()
df['A'].sum()
fig_c = px.scatter(df, x='A', y='B')
fig_c.update_traces(marker=dict(size=15))
fig_c.show()
df3 = pd.DataFrame({
    'A': ['Group1', 'Group1', 'Group1', 'Group2', 'Group2', 'Group2'],
    'B': [2, 5, 6, 7, 8, 9]
})
fig_d = px.box(df3, x='A', y='B')
fig_d.show()

df_4 = pd.DataFrame({'A':[1,2,3,4,5], 'B':[10,20,30,40,50], 'C':[500,400,300,200,100]})
fig_e = go.Figure(data=[go.Surface(z=df_4.values)])
fig_e.update_layout(
        scene=dict(
            xaxis_title = 'column',
            yaxis_title = 'Row Index',
            zaxis_title = 'Value'
                )
    )
fig_e.show()

dfdf = df[['A', 'B']]

spread = dfdf['B'] - dfdf['A']

fig_f = make_subplots(rows=2, cols=1, shared_xaxes=True,
                      row_heights=[0.7, 0.3])

# Top: line plot for A and B
fig_f.add_trace(go.Scatter(x=dfdf.index, y=dfdf['A'], name='A', line=dict(color='orange')), row=1, col=1)
fig_f.add_trace(go.Scatter(x=dfdf.index, y=dfdf['B'], name='B', line=dict(color='blue')), row=1, col=1)

# Bottom: spread as filled area
fig_f.add_trace(go.Scatter(
    x=dfdf.index, y=spread,
    fill='tozeroy',
    name='Spread',
    line=dict(color='green'),
    fillcolor='rgba(255,0,0,0.3)'
), row=2, col=1)

fig_f.update_yaxes(title_text='Spread', row=2, col=1)

fig_f.show()


fig = px.scatter(df_4, 
                 x='A',        # x axis
                 y='B',        # y axis
                 size='C',     # controls bubble size
                 color='A',    # color by column
                 hover_name='A')  # tooltip

fig.show()

fig_g = px.scatter_matrix(df_4,
                        dimensions=['A', 'B', 'C'],  # which columns to include
                        color='A',                    # color by a column
                        title='Scatter Matrix')
fig_g.show()


