import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Function to create normal distribution data
def get_normal_distribution(mean, std, x_range):
    x = np.linspace(mean - x_range, mean + x_range, 100)
    y = (1/(std * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mean)/std)**2)
    return x, y

# Create figure with subplots for each scenario
fig = make_subplots(rows=3, cols=1,
                   subplot_titles=("Scenario 1: Bolt Manufacturing (H₀: μ = 60)",
                                 "Scenario 2: Virus Testing Kit (H₀: μd = 20)",
                                 "Scenario 3: Apple Performance (H₀: μ = 13.5%)"))

# Scenario 1: Bolt Manufacturing
mean1, std1 = 60, 5
x1, y1 = get_normal_distribution(mean1, std1, 15)
critical_left1 = mean1 - 1.96*std1
critical_right1 = mean1 + 1.96*std1

fig.add_trace(
    go.Scatter(x=x1, y=y1, fill='tozeroy', name='Distribution',
               line=dict(color='blue'), showlegend=False),
    row=1, col=1
)

# Add vertical lines for critical values and null hypothesis
fig.add_vline(x=critical_left1, line_dash="dash", line_color="red",
              annotation_text="Lower Critical", row=1, col=1)
fig.add_vline(x=critical_right1, line_dash="dash", line_color="red",
              annotation_text="Upper Critical", row=1, col=1)
fig.add_vline(x=mean1, line_color="green",
              annotation_text="H₀: μ = 60", row=1, col=1)

# Scenario 2: Virus Testing Kit
mean2, std2 = 20, 2
x2, y2 = get_normal_distribution(mean2, std2, 6)
critical_left2 = mean2 - 1.96*std2
critical_right2 = mean2 + 1.96*std2

fig.add_trace(
    go.Scatter(x=x2, y=y2, fill='tozeroy', name='Distribution',
               line=dict(color='blue'), showlegend=False),
    row=2, col=1
)

fig.add_vline(x=critical_left2, line_dash="dash", line_color="red",
              annotation_text="Lower Critical", row=2, col=1)
fig.add_vline(x=critical_right2, line_dash="dash", line_color="red",
              annotation_text="Upper Critical", row=2, col=1)
fig.add_vline(x=mean2, line_color="green",
              annotation_text="H₀: μd = 20", row=2, col=1)

# Scenario 3: Apple Performance
mean3, std3 = 13.5, 1
x3, y3 = get_normal_distribution(mean3, std3, 3)
critical_left3 = mean3 - 1.96*std3
critical_right3 = mean3 + 1.96*std3

fig.add_trace(
    go.Scatter(x=x3, y=y3, fill='tozeroy', name='Distribution',
               line=dict(color='blue'), showlegend=False),
    row=3, col=1
)

fig.add_vline(x=critical_left3, line_dash="dash", line_color="red",
              annotation_text="Lower Critical", row=3, col=1)
fig.add_vline(x=critical_right3, line_dash="dash", line_color="red",
              annotation_text="Upper Critical", row=3, col=1)
fig.add_vline(x=mean3, line_color="green",
              annotation_text="H₀: μ = 13.5%", row=3, col=1)

# Update layout
fig.update_layout(
    height=900,
    width=800,
    showlegend=False,
    title_text="Two-Tailed Hypothesis Tests for All Scenarios",
    annotations=[
        dict(x=0.5, y=-0.15, xref="paper", yref="paper",
             text="Rejection Region: Reject H₀ if test statistic falls outside critical values",
             showarrow=False)
    ]
)

# Update axes labels
fig.update_xaxes(title_text="Number of Bolts", row=1, col=1)
fig.update_xaxes(title_text="Time Difference (hours)", row=2, col=1)
fig.update_xaxes(title_text="Performance Increase (%)", row=3, col=1)

fig.update_yaxes(title_text="Probability Density", row=1, col=1)
fig.update_yaxes(title_text="Probability Density", row=2, col=1)
fig.update_yaxes(title_text="Probability Density", row=3, col=1)

# Add colored rejection regions
for i, (x, y, cl, cr) in enumerate([(x1, y1, critical_left1, critical_right1),
                                  (x2, y2, critical_left2, critical_right2),
                                  (x3, y3, critical_left3, critical_right3)]):
    # Left rejection region
    mask_left = x <= cl
    fig.add_trace(
        go.Scatter(x=x[mask_left], y=y[mask_left], 
                  fill='tozeroy', fillcolor='rgba(255,0,0,0.2)',
                  line=dict(width=0), name='Rejection Region',
                  showlegend=False),
        row=i+1, col=1
    )
    
    # Right rejection region
    mask_right = x >= cr
    fig.add_trace(
        go.Scatter(x=x[mask_right], y=y[mask_right],
                  fill='tozeroy', fillcolor='rgba(255,0,0,0.2)',
                  line=dict(width=0), name='Rejection Region',
                  showlegend=False),
        row=i+1, col=1
    )

fig.show()