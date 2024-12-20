import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .user_activity_tracker import UserActivityTracker
from .performance_metrics import PerformanceMetrics

class DashboardGenerator:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1('Telegram Auto Forwarder Bot Dashboard'),
            dcc.Tabs([
                dcc.Tab(label='User Activity', children=[
                    dcc.Graph(id='user-activity-graph'),
                    dcc.Dropdown(
                        id='user-activity-dropdown',
                        options=[
                            {'label': 'Last 7 days', 'value': 7},
                            {'label': 'Last 30 days', 'value': 30},
                            {'label': 'Last 90 days', 'value': 90}
                        ],
                        value=30
                    )
                ]),
                dcc.Tab(label='Performance Metrics', children=[
                    dcc.Graph(id='performance-metrics-graph'),
                    dcc.Dropdown(
                        id='performance-metrics-dropdown',
                        options=[
                            {'label': 'Last 7 days', 'value': 7},
                            {'label': 'Last 30 days', 'value': 30},
                            {'label': 'Last 90 days', 'value': 90}
                        ],
                        value=30
                    )
                ])
            ])
        ])

    def setup_callbacks(self):
        @self.app.callback(
            Output('user-activity-graph', 'figure'),
            Input('user-activity-dropdown', 'value')
        )
        def update_user_activity_graph(days):
            activity_summary = UserActivityTracker.get_activity_summary(days)
            df = pd.DataFrame(activity_summary)
            fig = px.pie(df, values='count', names='activity_type', title=f'User Activity Summary (Last {days} days)')
            return fig

        @self.app.callback(
            Output('performance-metrics-graph', 'figure'),
            Input('performance-metrics-dropdown', 'value')
        )
        def update_performance_metrics_graph(days):
            success_rate = PerformanceMetrics.get_forwarding_success_rate(days)
            error_rate = PerformanceMetrics.get_error_rate(days)
            avg_time = PerformanceMetrics.get_average_forwarding_time(days)
            
            df = pd.DataFrame({
                'Metric': ['Success Rate', 'Error Rate', 'Avg Forwarding Time (s)'],
                'Value': [success_rate, error_rate, avg_time]
            })
            
            fig = px.bar(df, x='Metric', y='Value', title=f'Performance Metrics (Last {days} days)')
            return fig

    def run_server(self, debug=False, port=8050):
        self.app.run_server(debug=debug, port=port)

