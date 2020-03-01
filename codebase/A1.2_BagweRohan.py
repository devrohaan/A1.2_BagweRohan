#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS7DS4 – MT2019 - ASSIGNMENT 1.2 (42%)
Created on Sun Mar  1 03:02:18 2020

@author: Rohan Dilip Bagwe
@ID: 19314431



Requirements: Python Libraries
!pip install plotly
!pip install
!pip install wkhtmltopdf
!pip install altair
!pip install vega_datasets



"""

import plotly.graph_objects as go
import imgkit
import plotly
import pandas as pd
import numpy as np
import altair as alt
import io
import requests
import warnings
#%matplotlib inline
warnings.filterwarnings('ignore')

#PART A. NIGHTINGALE’S ROSE CHART

nightingale_dataset = pd.read_excel("data/nightingale-data.xlsx")

#Data Pre-processing:

nightingale_dataset.Month = nightingale_dataset.Month.replace(' ', '-', regex=True)

#DIAGRAM OF THE CAUSES OF MORTALITY IN THE ARMY IN THE EAST

nightingale_dataset_1=nightingale_dataset.iloc[0:12]
fig = go.Figure()
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_1['Zymotic diseases'],
    theta=nightingale_dataset_1['Month'],
    name='Deaths Due to Zymotic disease',
    marker=dict(color='rgb(52, 169, 247)')
))
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_1['Wounds & injuries'],
    theta=nightingale_dataset_1['Month'],
    name='Deaths Due to Wounds & injuries',
    marker=dict(color='rgb(247, 94, 52)')))

fig.add_trace(go.Barpolar(
    r=nightingale_dataset_1['All other causes'],
    theta=nightingale_dataset_1['Month'],
    name='Deaths Due to All other causes',
    marker=dict(color='rgb(153,5,153)')))

fig.update_layout(
    title='Florence Nightingale’s visualization: April 1854 - Mar 1855',
    font_size=12,
    showlegend=True,
    legend_title='<b> Causes of Mortality </b>',
    legend=dict(
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="#a5f2a5",
        bordercolor="Black",
        borderwidth=1),
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,

)
plotly.offline.plot(fig, filename='1a.html', auto_open=False)
#fig.show()

# Florence Nightingale’s visualization: April 1855 - Mar 1856


nightingale_dataset_2=nightingale_dataset.iloc[12:]
fig = go.Figure()
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_2['Zymotic diseases'],
    theta=nightingale_dataset_2['Month'],
    name='Due to Zymotic diseases',
    marker=dict(color='rgb(52, 169, 247)')
))
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_2['Wounds & injuries'],
    theta=nightingale_dataset_2['Month'],
    name='Due to Wounds & injuries',
    marker=dict(color='rgb(247, 94, 52)')))

fig.add_trace(go.Barpolar(
    r=nightingale_dataset_2['All other causes'],
    theta=nightingale_dataset_2['Month'],
    name='Due to All other causes',
    marker=dict(color='rgb(153,5,153)')))

fig.update_layout(
    title='Florence Nightingale’s visualization: April 1855 - Mar 1856',
    font_size=12,
    legend_font_size=12,
    showlegend=True,
    legend_title='<b> Causes of Mortality </b>',
    legend=dict(
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="#a5f2a5",
        bordercolor="Black",
        borderwidth=1),
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,

)
plotly.offline.plot(fig, filename='1b.html', auto_open=False)
#fig.show()


#Florence Nightingale’s visualization: April 1855 - Mar 1856: Rotated 180° and Zoomed¶


nightingale_dataset_2=nightingale_dataset.iloc[12:]
fig = go.Figure()
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_2['Zymotic diseases'],
    theta=nightingale_dataset_2['Month'],
    name='Deaths due to Zymotic diseases',
    marker=dict(color='rgb(52, 169, 247)')
))
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_2['Wounds & injuries'],
    theta=nightingale_dataset_2['Month'],
    name='Due to Wounds & injuries',
    marker=dict(color='rgb(247, 94, 52)')))

fig.add_trace(go.Barpolar(
    r=nightingale_dataset_2['All other causes'],
    theta=nightingale_dataset_2['Month'],
    name='Due toAll other causes',
    marker=dict(color='rgb(153,5,153)')))

fig.update_layout(
    title='Florence Nightingale’s visualization: April 1855 - Mar 1856 Roated 180° and Zoomed',
    font_size=12,
    legend_font_size=12,
    showlegend=True,
    legend_title='<b> Causes of Mortality </b>',
    legend=dict(
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="#a5f2a5",
        bordercolor="Black",
        borderwidth=1),
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=180,

)
plotly.offline.plot(fig, filename='1c.html', auto_open=False)
#fig.show(config={'scrollZoom': True})


#Florence Nightingale’s visualization Annual Rates of Mortality per 1000: April 1854 - Mar 1855

nightingale_dataset_1=nightingale_dataset.iloc[0:12]
nightingale_dataset_1['Zymotic diseases'] = (nightingale_dataset_1['Zymotic diseases']/nightingale_dataset_1['Average size of army'])*12*1000
nightingale_dataset_1['Wounds & injuries'] = (nightingale_dataset_1['Wounds & injuries']/nightingale_dataset_1['Average size of army'])*12*1000
nightingale_dataset_1['All other causes'] = (nightingale_dataset_1['All other causes']/nightingale_dataset_1['Average size of army'])*12*1000

#Prepare Data Using Formula

fig = go.Figure()
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_1['Zymotic diseases'],
    theta=nightingale_dataset_1['Month'],
    name='Deaths due to Zymotic diseases',
    marker=dict(color='rgb(255,153,153)')
))
fig.add_trace(go.Barpolar(
    r=nightingale_dataset_1['Wounds & injuries'],
    theta=nightingale_dataset_1['Month'],
    name='Deaths due to Wounds & injuries',
    marker=dict(color='rgb(13,255,13)')))

fig.add_trace(go.Barpolar(
    r=nightingale_dataset_1['All other causes'],
    theta=nightingale_dataset_1['Month'],
    name='Deaths due to All other causes',
    marker=dict(color='rgb(153,5,153)')))
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=1.25, z=1.25)
)
fig.update_layout(
    title='Florence Nightingale’s visualization Annual Rates of Mortality per 1000: April 1854 - Mar 1855',
    font_size=12,
    legend_font_size=12,
    showlegend=True,
    legend_title='<b> Causes of Mortality </b>',
    legend=dict(
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="#a5f2a5",
        bordercolor="Black",
        borderwidth=1),
    scene_camera=camera,
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,

)
plotly.offline.plot(fig, filename='1d.html', auto_open=False)
#fig.show()

'''
PART B. MINARD’S MAP
Datasets: Histdata_R_minard


https://forge.scilab.org/index.php/p/rdataset/source/tree/master/csv/HistData/Minard.cities.csv
https://forge.scilab.org/index.php/p/rdataset/source/tree/master/csv/HistData/Minard.troops.csv
https://forge.scilab.org/index.php/p/rdataset/source/tree/master/csv/HistData/Minard.temp.csv


'''

#Data Pre-processing:

histdata_R_minard_cities_dataset = pd.read_csv("data/Minard.cities.csv") # To plot cities
histdata_R_minard_troops_dataset = pd.read_csv("data/Minard.troops.csv") # To plot troops movement
histdata_R_minard_temp_dataset = pd.read_csv("data/Minard.temp.csv") #  To plot Temperature



# Removing Null and Formatting data
histdata_R_minard_cities_dataset.fillna('', inplace=True)
histdata_R_minard_troops_dataset.fillna('', inplace=True)
histdata_R_minard_cities_dataset.city = histdata_R_minard_cities_dataset['city'].str.upper()



#CITY
city_plot = alt.Chart(histdata_R_minard_cities_dataset).mark_text(
    font='Roboto', fontSize=9,).encode(
    longitude='long', latitude='lat', text='city',).properties(
        title='Cities')

#TROOPS MOVEMENT
troop_movement_plot = alt.Chart(histdata_R_minard_troops_dataset).mark_trail().encode(
    longitude='long',latitude='lat',size=alt.Size('survivors',
    scale=alt.Scale(range=[1, 70]), legend=None),
    detail='group', color=alt.Color('direction',
        scale=alt.Scale(domain=['A', 'R'], range=['#0000004d', '#d666667d']),legend=alt.Legend(title='Army Direction:',symbolType='circle')),).properties(
        title='MINARD MAP', )


troop_movement_plot.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24).save("troopsPlot.html")
troop_movement_plot.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24)

# ARMY GROUPS
troop_group_movement_plot = alt.Chart(histdata_R_minard_troops_dataset).mark_trail().encode(
    longitude='long',latitude='lat',size=alt.Size('survivors',
    scale=alt.Scale(range=[1, 70]), legend=None),
    detail='direction', color=alt.Color('group',
        scale=alt.Scale(domain=[1,2,3], range=['#0000004d', 'green','blue']),legend=alt.Legend(title='Group:', symbolType='square')),).properties(
        title='ARMY GROUPS', )

troop_group_movement_plot.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24).save("troop_group_movement_plot.html")
troop_group_movement_plot.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24)


#SURVIVORS
troops_count_plot = alt.Chart(histdata_R_minard_troops_dataset).mark_text(
    font='Arial', fontSize=7, fontStyle='italic', dx=30, angle=40).encode(
    longitude='long', latitude='lat', text='survivors').properties(
        title='Survivors Count')


troops_count_plot.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24).save("SurvivorsPlot.html")
troops_count_plot.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24)


#MINARD'S MAP
minard_map = troop_movement_plot + troops_count_plot + city_plot
minard_map.configure_view(width=900, height=500, strokeWidth=0).configure_title(fontSize=24)


#TEMPERATURE
histdata_R_minard_temp_dataset["days"] = histdata_R_minard_temp_dataset["days"].astype(str)
histdata_R_minard_temp_dataset["temp"] = histdata_R_minard_temp_dataset["temp"].astype(int)
histdata_R_minard_temp_dataset.fillna('YYYY', inplace=True)
histdata_R_minard_temp_dataset


histdata_R_minard_temp_dataset["text"] = histdata_R_minard_temp_dataset.apply(axis=1, func=lambda row: "{}° on {}".format(row[2], row[4])
)


x_axis_config = alt.X(
    'long',
    scale=alt.Scale(
        domain=[histdata_R_minard_temp_dataset.long.min(), histdata_R_minard_temp_dataset.long.max()]
    ),axis=None)
y_axis_config = alt.Y(
    'temp',
    axis=alt.Axis(
        title="Temperature during Retreat in °C",
        grid=True,
        orient='right'))
temperatures_chart_axes_config = alt.Chart(histdata_R_minard_temp_dataset).mark_line(
    color="blue").encode(
    x=x_axis_config,
    y=y_axis_config)
temperatures_chart_data = alt.Chart(histdata_R_minard_temp_dataset).mark_text(
    dx=5, dy=20,  fontSize=12).encode(
    x=x_axis_config,
    y=y_axis_config,
    text='text'
).properties(title='TEMPERATURE DURING RETREAT IN °C')

temperatures_chart = temperatures_chart_axes_config + temperatures_chart_data
temperatures_chart.configure_view(width=800, height=500, strokeWidth=0).configure_title(fontSize=24).save("temperature.html")



final_chart = alt.vconcat(minard_map, temperatures_chart).configure_view(width=900, height=400, strokeWidth=0).configure_title(fontSize=24)
final_chart.save("minard_map.html")