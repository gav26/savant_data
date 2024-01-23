#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:42:06 2024

@author: grantvurpillat
"""

from pybaseball import statcast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pybaseball import statcast
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
import math
import random


# Load data
st.set_page_config(page_title='Baseball Data Analysis', layout='wide')

# Data Preparation
df1 = statcast(start_dt="2023-08-24", end_dt="2023-08-25")
df_cleaned = df1.dropna(subset=['launch_angle', 'launch_speed', 'estimated_ba_using_speedangle'])
df1 = df_cleaned[['launch_speed', 'launch_angle', 'estimated_ba_using_speedangle']]

df1['launch_speed'] = df1['launch_speed'].astype('float64')
df1['launch_angle'] = df1['launch_angle'].astype('int64')
df1['estimated_ba_using_speedangle'] = df1['estimated_ba_using_speedangle'].astype('float64')

df1.reset_index(drop=True, inplace=True)

# Creating the Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='launch_speed', y='launch_angle', hue='estimated_ba_using_speedangle', data=df1)
plt.title("Launch Speed vs Launch Angle Scatter Plot")

# Display the Plot in Streamlit
st.pyplot(plt)
