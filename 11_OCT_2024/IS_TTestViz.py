import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from scipy import stats

# Initialize the Dash app
app = dash.Dash(__name__)

# Function to generate sample data
def generate_sample_data(mean, std, size):
    return np.random.normal(mean, std, size)

# Layout
app.layout = html.Div([
    html.H1("T-Test Visualization", style={'textAlign': 'center'}),
    
    # Test Type Selection
    html.Div([
        html.Label("Select T-Test Type:"),
        dcc.Dropdown(
            id='test-type',
            options=[
                {'label': 'One Sample T-Test', 'value': 'one'},
                {'label': 'Independent (Two Sample) T-Test', 'value': 'two'},
                {'label': 'Paired T-Test', 'value': 'paired'}
            ],
            value='one'
        )
    ], style={'width': '50%', 'margin': '20px auto'}),
    
    # Parameter Controls
    html.Div([
        html.Div([
            html.Label("Sample Size:"),
            dcc.Slider(
                id='sample-size',
                min=10,
                max=100,
                step=10,
                value=30,
                marks={i: str(i) for i in range(10, 101, 10)}
            )
        ], style={'margin': '20px 0'}),
        
        html.Div([
            html.Label("Effect Size:"),
            dcc.Slider(
                id='effect-size',
                min=0,
                max=2,
                step=0.1,
                value=0.5,
                marks={i/10: str(i/10) for i in range(0, 21, 2)}
            )
        ], style={'margin': '20px 0'})
    ], style={'width': '50%', 'margin': '0 auto'}),
    
    # Graphs
    html.Div([
        dcc.Graph(id='distribution-plot'),
        html.Div(id='test-results', style={'margin': '20px', 'textAlign': 'center'})
    ]),
    
    # Generate New Data Button
    html.Button('Generate New Data', id='generate-button', 
                style={'margin': '20px auto', 'display': 'block'})
])

# Callback for updating the plots
@app.callback(
    [Output('distribution-plot', 'figure'),
     Output('test-results', 'children')],
    [Input('test-type', 'value'),
     Input('sample-size', 'value'),
     Input('effect-size', 'value'),
     Input('generate-button', 'n_clicks')]
)
def update_graph(test_type, sample_size, effect_size, n_clicks):
    # Base parameters
    population_mean = 100
    std_dev = 15
    
    if test_type == 'one':
        # One Sample T-Test
        sample = generate_sample_data(population_mean + effect_size * std_dev, 
                                    std_dev, sample_size)
        
        t_stat, p_value = stats.ttest_1samp(sample, population_mean)
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=sample, name='Sample Data', 
                                 nbinsx=20, opacity=0.7))
        fig.add_vline(x=population_mean, line_dash="dash", 
                     line_color="red", annotation_text="Population Mean")
        
        results = f"One Sample T-Test Results: t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}"
        
    elif test_type == 'two':
        # Two Sample T-Test
        group1 = generate_sample_data(population_mean, std_dev, sample_size)
        group2 = generate_sample_data(population_mean + effect_size * std_dev, 
                                    std_dev, sample_size)
        
        t_stat, p_value = stats.ttest_ind(group1, group2)
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=group1, name='Group 1', 
                                 nbinsx=20, opacity=0.7))
        fig.add_trace(go.Histogram(x=group2, name='Group 2', 
                                 nbinsx=20, opacity=0.7))
        
        results = f"Independent T-Test Results: t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}"
        
    else:  # paired
        # Paired T-Test
        baseline = generate_sample_data(population_mean, std_dev, sample_size)
        follow_up = baseline + effect_size * std_dev + \
                   generate_sample_data(0, std_dev/4, sample_size)
        
        t_stat, p_value = stats.ttest_rel(baseline, follow_up)
        
        fig = go.Figure()
        fig.add_trace(go.Box(y=baseline, name='Before', boxpoints='all', 
                           jitter=0.3, pointpos=-1.8))
        fig.add_trace(go.Box(y=follow_up, name='After', boxpoints='all', 
                           jitter=0.3, pointpos=-1.8))
        
        results = f"Paired T-Test Results: t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}"
    
    # Update layout
    fig.update_layout(
        title='Data Distribution by Test Type',
        xaxis_title='Values',
        yaxis_title='Frequency',
        showlegend=True,
        height=600,
        barmode='overlay'
    )
    
    return fig, results

# Add explanation text based on test type
@app.callback(
    Output('test-explanation', 'children'),
    [Input('test-type', 'value')]
)
def update_explanation(test_type):
    explanations = {
        'one': """
            One Sample T-Test:
            - Compares one sample mean to a known population mean
            - Used when population standard deviation is unknown
            - Assumes normal distribution of data
            - Example: Are student test scores different from the historical average?
        """,
        'two': """
            Independent (Two Sample) T-Test:
            - Compares means of two independent groups
            - Groups are not related to each other
            - Assumes normal distribution and equal variances
            - Example: Comparing test scores between two different schools
        """,
        'paired': """
            Paired T-Test:
            - Compares means of before/after measurements
            - Same subjects measured twice
            - Accounts for individual differences
            - Example: Comparing weights before and after a diet program
        """
    }
    return html.Div([
        html.H3("Test Description"),
        html.Pre(explanations[test_type])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)