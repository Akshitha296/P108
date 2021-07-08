import plotly.express as pd
import plotly.figure_factory as ff
import csv 
import pandas as pd

df = pd.read_csv("phone.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist = False)
fig.show()