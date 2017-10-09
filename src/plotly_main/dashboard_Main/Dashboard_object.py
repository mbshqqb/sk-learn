import plotly
import plotly.dashboard_objs as dashboard
my_dboard = dashboard.Dashboard()

box_a = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': '0',
    'title': 'scatter-for-dashboard'
}
my_dboard.insert(box_a)

plotly.offline.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')