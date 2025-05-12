import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pharma_ai_visibility.mock_data_generator import PharmaAIMockDataGenerator
from pharma_ai_visibility.data_analysis import PharmaAIVisibilityAnalysis

def ensure_data_exists():
    """Ensure mock data is generated"""
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    data_file = os.path.join(data_dir, 'pharma_ai_visibility_mock_data.csv')
    
    if not os.path.exists(data_file):
        generator = PharmaAIMockDataGenerator()
        generator.save_mock_data(data_dir)

def main():
    # Ensure data is generated before running the app
    ensure_data_exists()
    
    # Set page configuration
    st.set_page_config(
        page_title="Pharma AI Visibility Intelligence", 
        page_icon="💊",
        layout="wide"
    )
    
    # Title and Introduction
    st.markdown("""
    # 🧬 Pharmaceutical AI Visibility Intelligence
    ## Strategic Insights for Market Leadership
    """)
    
    # Initialize Analyzer
    try:
        analyzer = PharmaAIVisibilityAnalysis()
    except Exception as e:
        st.error(f"Error initializing analyzer: {e}")
        return
    
    # Strategic Insights Section
    st.header("🔍 Strategic Insights")
    try:
        insights = analyzer.export_insights_report()
        
        # Display key insights
        for key, value in insights['Overall_Insights'].items():
            st.markdown(f"### {key.replace('_', ' ')}")
            st.write(str(value))
    except Exception as e:
        st.error(f"Error generating insights: {e}")
    
    # Visualizations
    st.header("🌐 Comprehensive Performance Metrics")
    
    # Try to generate and display visualizations
    try:
        # Generate visualizations
        analyzer.generate_advanced_visualization()
        
        # Display the generated image
        st.image('data/pharma_ai_visibility_analysis.png', 
                 caption='Comprehensive Pharma AI Visibility Analysis')
    except Exception as e:
        st.error(f"Error generating visualizations: {e}")
    
    # Data Exploration
    if st.checkbox("Explore Detailed Dataset"):
        st.dataframe(analyzer.data)
    
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

if __name__ == "__main__":
    main()
