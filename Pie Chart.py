import plotly.express as px
import pandas as pd

df = pd.read_csv('sz_fig.csv')
fig = px.pie(df, values='loc_frequency', names='fcode', title='Räumliche Ebenen SZ')
fig.show()
fig.write_html("sz_piechart.html")