import streamlit as st
import numpy as np
import plotly.graph_objects as go

def create_visualization():
    st.title("Population Parameter vs Sample Statistics")
    
    # Sidebar controls
    st.sidebar.subheader("Settings")
    population_mean = st.sidebar.number_input("Population Mean", value=100)
    sample_size = st.sidebar.number_input("Sample Size", value=30, min_value=5)
    
    if st.button("Generate New Samples"):
        # Generate data
        samples = 20
        sample_means = [np.mean(np.random.normal(population_mean, 5, sample_size)) 
                       for _ in range(samples)]
        
        # Create figure
        fig = go.Figure()
        
        # Add sample means
        fig.add_trace(go.Scatter(
            x=list(range(1, samples + 1)),
            y=sample_means,
            mode='lines+markers',
            name='Sample Means',
            hovertemplate='Sample %{x}<br>Mean: %{y:.2f}<extra></extra>'
        ))
        
        # Add population mean line
        fig.add_hline(y=population_mean, 
                     line_dash="dash", 
                     line_color="red",
                     annotation_text=f"Population Mean (μ={population_mean})")
        
        # Update layout for mobile responsiveness
        fig.update_layout(
            title='Parameter vs Statistics Visualization',
            xaxis_title='Sample Number',
            yaxis_title='Value',
            hovermode='x unified',
            showlegend=True,
            # Make it mobile responsive
            autosize=True,
            margin=dict(l=20, r=20, t=40, b=20),
            height=500  # Fixed height for mobile
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    # Add explanatory text
    st.markdown("""
    ### Key Observations:
    - Red line: Population parameter (fixed)
    - Blue points: Sample statistics (varying)
    - Hover over points to see exact values
    """)

if __name__ == "__main__":
    create_visualization()