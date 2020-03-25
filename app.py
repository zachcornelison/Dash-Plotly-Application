#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jupyter_plotly_dash import JupyterDash

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# In[2]:


app = JupyterDash('SimpleExample')

app.layout = html.Div(children=[
    html.H1('tutorial'),
    dcc.Graph(id='example', 
             figure = {
                 'data': [{'x': [1,2,3,4], 'y': [3,1,6,4], 
                           'type':'line', 'name': 'boats'},
                          {'x': [1,2,3,4], 'y': [2,9,3,6], 
                           'type':'bar', 'name': 'cars'}
                         ],
                 'layout': {
                     'title': 'Example'
                 }
             })
])


# In[3]:


app


# In[ ]:




