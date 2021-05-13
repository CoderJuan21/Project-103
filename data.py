import pandas as pd 
import plotly.express as px 

df = pd.read_csv("datastuff.csv") 

fig = px.scatter(df, x="date", y="cases",color="country", size_max=50) 
fig.show()