from re import split
import numpy as np
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

   #      lat        lng  ...                        addr  e
#0  40.297876 -75.581294  ...      REINDEER CT & DEAD END  1
#1  40.258061 -75.264680  ...  BRIAR PATH & WHITEMARSH LN  1
##2  40.121182 -75.351975  ...                    HAWS AVE 1
#3  40.116153 -75.343513  ...          AIRY ST & SWEDE ST  1
#4  40.251492 -75.603350  ...    CHERRYWOOD CT & DEAD END  1
 

df = pd.read_csv(r'C:\Users\megam\source\repos\Data_Science_ML_DL_lectures\Data_Capstone_Project\911.csv')
#print(df.info())
#print(df.head())
counter = df['zip'].value_counts()
#print(counter.head())

counter2 = df['twp'].value_counts()
#print(counter2.head())

counter3 = df['title'].nunique()
#print(counter3)

df['Reasons'] = df['title'].apply(lambda x: x.split(': ')[0])
#print(split_reasons)
most_reasons = df['Reasons'].unique()
#print(most_reasons.max())


sns.countplot(x =  df['Reasons'])
plt.show()

tP = type(df['timeStamp'].iloc[0])
#print(tP)

conv_datetime= df['timeStamp'] = pd.to_datetime(df['timeStamp'])
#print(conv_datetime)

time = df['timeStamp'].iloc[0]
#print(time.hour)

show_hour = df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Day Of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
show_month = df['Month'] = df['timeStamp'].apply(lambda time: time.month)
#print(show_month)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
mapper = df['Day Of Week'].map(dmap)
#print(mapper)
dmap2 = {
    0: 'jan',
    1: 'feb',
    2: 'mar',
    3: 'apr',
    4: 'may',
    5: 'jun',
    6: 'jul',
    7: 'aug',
    8: 'sep',
    9: 'oct',
    10: 'nov',
    11: 'dec'
}
mapper2 = show_month.map(dmap2)

sns.countplot(x=mapper, hue=df['Reasons'])
plt.show()

sns.countplot(x=mapper2, hue=df['Reasons'])
plt.legend(loc = 'best')
plt.show()

byMonth = df.groupby('Month').count()
print(byMonth.head())

group_month = byMonth['twp']
sns.lineplot(group_month)
plt.show()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())
plt.show()
df['Date'] = df['timeStamp'].apply(lambda time: time.date())
group_date = df.groupby('Date').count()

sns.kdeplot(group_date)
plt.show()

df[df['Reasons'] == 'Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
plt.show()

df[df['Reasons']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
plt.show()


df[df['Reasons']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
plt.show()

dayHour = df.groupby(by=['Day Of Week','Hour']).count()['Reasons'].unstack()
print(dayHour.head())

plt.figure(figsize=(12,6))
sns.heatmap(dayHour, cmap='viridis')
plt.show()

sns.clustermap(dayHour,cmap='viridis')
plt.show()

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')
plt.show()

sns.clustermap(dayMonth,cmap='viridis')
plt.show()


