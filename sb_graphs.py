""" Some data visualization with seaborn. """
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from query_a import pm10_day_wielk as pm, params_in_w as pa_c, day_wielk as dw, quality_in_prov as qp

""" Bar chart showing the number of a given parameter sensors in Wielkopolska. """
sns.barplot(x='sensors_count',
            y='parameter',
            data=pa_c)
plt.show()

""" Box plots showing two parameters values from one day, form all sensors in Wielkopolska. """

chart = sns.catplot(data=dw[(dw['parameter'] == 'dwutlenek azotu') | (dw['parameter'] == 'pył zawieszony PM10') ],
                    x='address',
                    y='value',
                    aspect=1.5,
                    kind='box',
                    col='parameter')
chart.set_xticklabels(rotation=40, horizontalalignment='right')
plt.show()

""" Line graph showing changes in PM10 concentration over one day at all measuring points in Wielkopolska. """

chart = sns.relplot(data=pm,
                    x='date',
                    y='value',
                    aspect=1.5,
                    kind='line',
                    hue='address')
chart.set_xticklabels(rotation=40, horizontalalignment='right')
plt.show()

""" Scatter plot showing air quality in provinces. """
chart = sns.relplot(data=qp,
                    x='province',
                    y='air_quality',
                    size='city_quant',
                    kind='scatter',
                    hue='province')
chart.set_xticklabels(rotation=40, horizontalalignment='right')
plt.show()