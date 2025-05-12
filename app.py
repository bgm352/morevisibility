import streamlit as st
import sys
import os

# Ensure the current directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(current_dir))

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

# Mock data generation (simplified for deployment)
def generate_mock_data():
    """Generate a simplified mock dataset for pharma AI visibility"""
    np.random.seed(42)
    brands = ['Pfizer', 'Moderna', 'Johnson & Johnson', 'AstraZeneca']
    platforms = ['ChatGPT', 'Microsoft Copilot', 'Google Gemini']
    
    data = []
    for _ in range(50):  # Generate 50 data points
        brand = np.random.choice(brands)
        platform = np.random.choice(platforms)
        
        data.append({
            'Brand': brand,
            'Platform': platform,
            'Visibility_Score': np.random.uniform(20, 80),
            'Sentiment_Score': np.random.uniform(-1, 1),
            'Innovation_Mentions': np.random.randint(1, 10)
        })
    
    return pd.DataFrame(data)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Pharma AI Visibility Intelligence", 
        page_icon="💊",
        layout="wide"
    )
    
    # Title
    st.title("🧬 Pharmaceutical AI Visibility Intelligence")
    
    # Generate mock data
    try:
        data = generate_mock_data()
    except Exception as e:
        st.error(f"Error generating mock data: {e}")
        return
    
    # Visualization Sections
    st.header("Brand Visibility Analysis")
    
    # Visibility Score by Brand
    fig1 = px.box(
        data, 
        x='Brand', 
        y='Visibility_Score', 
        title='Visibility Score Distribution'
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Sentiment Analysis
    fig2 = px.scatter(
        data, 
        x='Visibility_Score', 
        y='Sentiment_Score', 
        color='Brand',
        title='Visibility vs Sentiment',
        labels={'Visibility_Score': 'Visibility', 'Sentiment_Score': 'Sentiment'}
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Platform Comparison
    platform_performance = data.groupby('Platform')['Visibility_Score'].mean()
    fig3 = px.bar(
        x=platform_performance.index, 
        y=platform_performance.values,
        title='Average Visibility by Platform',
        labels={'x': 'Platform', 'y': 'Average Visibility Score'}
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    # Key Insights
    st.header("Key Insights")
    
    # Top performing brand
    top_brand = data.groupby('Brand')['Visibility_Score'].mean().idxmax()
    st.metric("Top Performing Brand", top_brand)
    
    # Data Table
    st.header("Raw Data")
    st.dataframe(data)

if __name__ == "__main__":
    main()
