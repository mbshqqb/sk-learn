import plotly.offline as py
import plotly.graph_objs as go

trace1=go.Scatter(
    x=[1,2],
    y=[1,2],
mode='markers'
)
trace2=go.Scatter(
    x=[0,2],
    y=[2,1]
)
py.plot([trace1, trace2],filename='temp.html',auto_open=False)