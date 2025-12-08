import json
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback
import os 
import pandas as pd 
import sys 

class Dataset: 
    def __init__(self, folder_path:str, metrics:list): 
        self.folder_path = folder_path 
        self.metrics = metrics 
    
    def get_trace(self, file_name:str) -> dict: 
        with open(file_name, 'r') as f: 
            data = json.load(f)

        result = {}
        for idx, metric in enumerate(data):
            for key, value in metric.items():
                if key=='name' and value in self.metrics: 
                    result[value] = data[idx]['value']
        trace_id = file_name.split('_')[-1].split('.')[0]
        return trace_id, result 
    
    def get_data(self):
        files = os.listdir(self.folder_path)
        traces = filter(lambda x: x.endswith('.json'), files) 
        collated_metrics = {}
        for trace in traces: 
            trace_id, result = self.get_trace(os.path.join(self.folder_path, trace))
            collated_metrics[trace_id] = result

        dataframe_data = []
        for trace_id, metrics in collated_metrics.items():
            for metric_name, metric_value in metrics.items():
                dataframe_data.append({
                    'trace_id': trace_id,
                    'metric': metric_name,
                    'value': metric_value
                })
        return dataframe_data 



if __name__ == "__main__": 
    dataset = Dataset('traces', ['context_relevance', 'answer_relevance', 'faithfulness'])
    result = dataset.get_data() 
    df = pd.DataFrame(result)
    
    fig = go.Figure(data=px.line_polar(
        df, 
        r='value', 
        theta='metric', 
        color='trace_id',
        line_close=True,
        template="plotly_dark")
        )

    fig.update_layout(height=960)


    app = Dash()
    app.layout = html.Div([
        dcc.Graph(figure=fig, id='radar-graph'), 
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])

    @callback(Output('radar-graph', 'figure'), Input('interval-component','n_intervals'))
    def update_radar(n): 
        result = dataset.get_data() 
        df = pd.DataFrame(result)

        fig = go.Figure(data=px.line_polar(
            df, 
            r='value', 
            theta='metric', 
            color='trace_id',
            line_close=True,
            template="plotly_dark")
            )

        fig.update_layout(height=960)
        return fig


    app.run(debug=True, use_reloader=False)


    