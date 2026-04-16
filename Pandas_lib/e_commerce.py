import numpy as np
import pandas as pd
from pandas import DataFrame, to_numeric

df= pd.read_csv('Ecommerce Purchases')
ecom = DataFrame((df))
print(ecom)
cols= len(ecom['Address'])
headers = ecom.columns
print('-'*50)
print(cols)
print('-'*50)
print(list(headers))
print('-'*50)
ave_purchase_price = ecom['Purchase Price'].mean()
print(ave_purchase_price)
print('-'*50)

print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())
print('-'*50)

def lang(eng):
    if 'en' in eng.lower().split():
        return True
    else:
        return False
lang('en')

list_lang = ecom[ecom['Language'].apply(lambda x: lang(x))]
print(len(list_lang))
print('-'*50)

def get_law(law):
    if 'lawyer' in law.lower().split():
        return True
    else:
        return False
list_law = ecom[ecom['Job'].apply(lambda x: get_law(x))]
print(len(list_law))

print(ecom['AM or PM'].value_counts())

top_5 = ecom['Job'].value_counts().head(5)
print(top_5)
print('*'*50)

get_lot = ecom.loc[ecom['Lot'] == "90 WT", 'Purchase Price']
print(get_lot.iloc[0])
print('*'*50)
get_email = ecom.loc[ecom['Credit Card']==4926535242672853, 'Email'].iloc[0] # you can actually use ["Email"] to get the emial instead of the iloc(0)
print(get_email)
print('*'*50)
#** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**
american = ecom.loc[(ecom['CC Provider']== 'American Express') & (ecom['Purchase Price']>95)]
print(len(american))
#** Hard: How many people have a credit card that expires in 2025? **
print('*'*50)
exp_cred = ecom[ecom['CC Exp Date'].str.endswith('25')]
print(len(exp_cred))

#** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

email_providers = ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
print(email_providers)