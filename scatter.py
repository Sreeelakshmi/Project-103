import plotly.express as px
import pandas as pd
df=pd.read_csv("C:/Users/dell/Desktop/Python/folderA/txt/data.csv")
fig=px.scatter(df,x="date",y="cases",color="country")
fig.show()