# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CTqmFl47Qn5I07XD5UlvDVwS8j9Us8F8
"""

What is Plotly ?
Python Plotly Library is an open-source library that can be used for data visualization and understanding 
data simply and easily. Plotly supports various types of plots like line charts, scatter plots, histograms, cox plots, etc.

Where it is used ?
 plotly is used in any of the Python scripts like  top of the Plotly JavaScript library (plotly. js)
 plotly enables Python users to create beautiful interactive web-based visualizations.

#pie chart: plot a Pie Chart of Indian Car companies market share % values
import plotly.graph_objects as go

labels = ['Maruti Suzuki','Hyundai','TATA','Kia', 'Mahindra', 'Renault']
values = [56, 21, 10.6, 6.1, 4.8, 1.5]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

#bar chart: Plot a Bar Chart with India's covid-19 Active cases ( Max 10 States )
import plotly.graph_objects as go

States = ['Maharashtra', 'Kerala', 'Karnataka', 'Tamil Nadu', 'Andhra Pradesh', 'Uttar Pradesh', 'West Bengal', 'Delhi', 'Chhattisgarh', 'Rajasthan']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=States,
    y=[112231, 113120, 38729, 33224, 30300, 1789, 15690, 798, 4914, 815 ],
    name='Primary Product',
    marker_color='indianred'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

# line chart: Plot a Line Chat with India's active covid-19 case recovery (maximum 12 Months)
 import numpy as np
import plotly.graph_objects as go

Months = ['August2020', 'September2020', 'October2020', 'November2020', 'December2020', 'January2021', 'February2021', 'March2021', 'April2021', 'May2021', 'June2021', 'July2021']
Recovery = [51232, 78169 , 78646, 53702, 43203, 20143, 13462, 11990, 50390, 308769, 231488, 54565]
fig = go.Figure(data=go.Scatter(x = Months, y = Recovery))
fig.show()