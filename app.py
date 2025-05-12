import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import os
import json

class PharmaAIVisibilityAnalyzer:
    def __init__(self, data_path='data/pharma_ai_visibility_mock_data.csv'):
        # Load mock data
        self.visibility_data = self._load_data(data_path)
        
        # Load metadata
        self._load_metadata()
    
    def _load_data(self, data_path):
        """Load mock data from CSV"""
        try:
            return pd.read_csv(data_path)
        except FileNotFoundError:
            st.error(f"Data file not found: {data_path}")
            return pd.DataFrame()  # Return empty DataFrame if file not found
    
    def _load_metadata(self):
        """Load brand and platform metadata"""
        try:
            with open('data/pharma_brands_metadata.json', 'r') as f:
                self.pharma_brands = json.load(f)
            
            with open('data/ai_platforms_metadata.json', 'r') as f:
                self.ai_platforms = json.load(f)
        except FileNotFoundError:
            st.warning("Metadata files not found. Using default configurations.")
            self.pharma_brands = []
            self.ai_platforms = []
    
    def generate_strategic_insights(self):
        """Generate strategic insights from mock data"""
        insights = {}
        
        # Aggregate data by brand
        brand_performance = self.visibility_data.groupby('Brand').agg({
            'Visibility_Score': ['mean', 'max'],
            'Sentiment_Score': 'mean',
            'Innovation_Mentions': 'sum'
        }).reset_index()
        brand_performance.columns = ['Brand', 'Avg_Visibility', 'Max_Visibility', 'Avg_Sentiment', 'Total_Innovations']
        
        # Top performing brand
        top_brand = brand_performance.loc[brand_performance['Avg_Visibility'].idxmax()]
        insights['Top Performing Brand'] = (
            f"{top_brand['Brand']} leads in AI visibility with an average score of "
            f"{top_brand['Avg_Visibility']:.2f} and peak visibility of {top_brand['Max_Visibility']:.2f}"
        )
        
        # Platform analysis
        platform_performance = self.visibility_data.groupby('Platform').agg({
            'Visibility_Score': 'mean',
            'Platform_User_Base_Millions': 'first',
            'Global_Platform_Accessibility': 'first'
        }).reset_index()
        top_platform = platform_performance.loc[platform_performance['Visibility_Score'].idxmax()]
        insights['Strategic Platform'] = (
            f"{top_platform['Platform']} provides the most comprehensive visibility, "
            f"with {top_platform['Platform_User_Base_Millions']} million users and "
            f"{top_platform['Global_Platform_Accessibility']:.2%} global accessibility"
        )
        
        # Innovation insights
        innovation_leaders = brand_performance.sort_values('Total_Innovations', ascending=False)
        top_innovator = innovation_leaders.iloc[0]
        insights['Innovation Leadership'] = (
            f"{top_innovator['Brand']} demonstrates thought leadership with "
            f"{top_innovator['Total_Innovations']} innovation mentions across AI platforms"
        )
        
        return insights
    
    def visualize_ai_visibility(self):
        """Create comprehensive visualizations"""
        # Visibility Trend
        fig1 = px.line(
            self.visibility_data, 
            x='Month', 
            y='Visibility_Score', 
            color='Brand',
            title='Pharma Brand AI Visibility Trends',
            labels={'Visibility_Score': 'Visibility Score'}
        )
        
        # Sentiment Analysis
        fig2 = px.box(
            self.visibility_data, 
            x='Platform', 
            y='Sentiment_Score', 
            color='Brand',
            title='Brand Sentiment Across AI Platforms',
            labels={'Sentiment_Score': 'Sentiment Score'}
        )
        
        # Innovation Mentions Heatmap
        pivot_data = self.visibility_data.pivot_table(
            index='Brand', 
            columns='Platform', 
            values='Innovation_Mentions', 
            aggfunc='mean'
        )
        
        fig3 = px.imshow(
            pivot_data, 
            title='Innovation Mentions Heatmap',
            labels=dict(x='Platform', y='Brand', color='Avg Innovation Mentions'),
            color_continuous_scale='YlGnBu'
        )
        
        return fig1, fig2, fig3

def main():
    st.set_page_config(
        page_title="Pharma AI Visibility Intelligence", 
        page_icon="💊",
        layout="wide"
    )
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Generate mock data if not exists
    if not os.path.exists('data/pharma_ai_visibility_mock_data.csv'):
        from mock_data_generator import PharmaAIMockDataGenerator
        generator = PharmaAIMockDataGenerator()
        generator.save_mock_data()
    
    # Title and Introduction
    st.markdown("""
    # 🧬 Pharmaceutical AI Visibility Intelligence
    ## Strategic Insights for Market Leadership
    """)
    
    # Initialize Analyzer
    analyzer = PharmaAIVisibilityAnalyzer()
    
    # Strategic Insights Section
    st.header("🔍 Strategic Insights")
    insights = analyzer.generate_strategic_insights()
    for title, insight in insights.items():
        st.markdown(f"### {title}")
        st.write(insight)
    
    # Visualization Columns
    st.header("🌐 Comprehensive Performance Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.plotly_chart(analyzer.visualize_ai_visibility()[0], use_container_width=True)
    
    with col2:
        st.plotly_chart(analyzer.visualize_ai_visibility()[1], use_container_width=True)
    
    with col3:
        st.plotly_chart(analyzer.visualize_ai_visibility()[2], use_container_width=True)
    
    # Data Exploration
    if st.checkbox("Explore Detailed Dataset"):
        st.dataframe(analyzer.visibility_data)
    
    # Methodology and Value Proposition
    st.markdown("""
    ## 💡 Why AI Visibility Matters
    
    ### For Pharmaceutical Decision Makers
    - **Strategic Positioning**: Understand your brand's AI presence
    - **Competitive Intelligence**: Track industry visibility trends
    - **Innovation Tracking**: Monitor knowledge dissemination
    - **Sentiment Analysis**: Gauge brand perception
    
    ### Methodology
    - Mock data simulates real-world AI visibility scenarios
    - Multi-platform performance tracking
    - Advanced visibility and sentiment metrics
    """)
    
    # Call to Action
    st.markdown("""
    ### Ready to Elevate Your AI Strategy?
    [Request a Personalized Consultation](#)
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
