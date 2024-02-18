#!/usr/bin/env python
# coding: utf-8

# # User Funnel Analysis using Python
# 
# ##  Importing the Dataset

# In[4]:


import pandas as pd
data = pd.read_csv("C:/Users/sengu/OneDrive/Desktop/user_funnel.csv")
print(data.head())


# The stage column contains the stages of the flow of the users.

# In[5]:


print(data["stage"].value_counts())


# ## Funnel Analysis
# The user funnel stages of the website are homepage >> product_page >> cart >> checkout >> purchase.

# In[6]:


import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

#define the funnel stages
funnel_stages = ['homepage', 'product_page', 'cart', 'checkout', 'purchase']

#calculate the number of users and conversions for each stage
num_users = []
num_conversions = []

for stage in funnel_stages:
    stage_users = data[data['stage'] == stage]
    num_users.append(len(stage_users))
    num_conversions.append(stage_users['conversion'].sum())

#create a funnel chart
fig = go.Figure(go.Funnel(
    y=funnel_stages,
    x=num_users,
    textposition='inside',
    textinfo='value',
    name='Users'
))

fig.add_trace(go.Funnel(
    y=funnel_stages,
    x=num_conversions,
    textposition='inside',
    textinfo='value',
    name='Conversions'
))

fig.update_layout(
    title='Funnel Analysis',
    funnelmode='stack'
)

fig.show()


# In[7]:


print(num_users)


# In[8]:


print(num_conversions)


# 
# ## Conversion rate calculation

# In[27]:


p=[]
for i in range(0,5):
    perc=(num_conversions[i]/num_users[i])*100
    p.append(perc)
    print(funnel_stages[i],":",perc,"%")


# In[31]:


import matplotlib.pyplot as plt
plt.plot(funnel_stages,p)
plt.xlabel("FUNNEL STAGES")
plt.ylabel("CONVERSION RATES")
plt.title("Line Graph of Conversion rate")
plt.show()


# In[34]:


plt.bar(funnel_stages,p,color="orange")
plt.xlabel("FUNNEL STAGES")
plt.ylabel("CONVERSION RATES")
plt.title("Bar Graph of Conversion rate")
plt.show()


# The conversion rate has a steep fall as a user moves through the different funnel stages homepage >> product_page >> cart >> checkout >> purchase.
