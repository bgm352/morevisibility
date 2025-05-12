import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class PharmaAIVisibilityAnalysis:
    def __init__(self, data_path='data/pharma_ai_visibility_mock_data.csv'):
        """
        Initialize the analysis with mock pharma AI visibility data
        
        Args:
            data_path (str): Path to the CSV file containing mock data
        """
        self.data = pd.read_csv(data_path)
    
    def brand_platform_performance_analysis(self):
        """
        Comprehensive analysis of brand performance across AI platforms
        
        Returns:
            dict: Detailed performance metrics and insights
        """
        # Group by Brand and Platform
        performance_metrics = self.data.groupby(['Brand', 'Platform']).agg({
            'Visibility_Score': ['mean', 'std'],
            'Sentiment_Score': ['mean', 'std'],
            'Innovation_Mentions': ['sum', 'mean']
        }).reset_index()
        
        # Flatten multi-level column names
        performance_metrics.columns = [
            'Brand', 'Platform', 
            'Avg_Visibility', 'Visibility_Std', 
            'Avg_Sentiment', 'Sentiment_Std', 
            'Total_Innovations', 'Avg_Innovations'
        ]
        
        return performance_metrics
    
    def temporal_trend_analysis(self):
        """
        Analyze visibility and sentiment trends over time
        
        Returns:
            pd.DataFrame: Monthly trends for brands
        """
        monthly_trends = self.data.groupby(['Brand', 'Month']).agg({
            'Visibility_Score': 'mean',
            'Sentiment_Score': 'mean',
            'Innovation_Mentions': 'sum'
        }).reset_index()
        
        return monthly_trends
    
    def generate_advanced_visualization(self):
        """
        Create advanced visualizations for comprehensive insights
        """
        # Prepare figure with multiple subplots
        plt.figure(figsize=(20, 15))
        
        # 1. Visibility Score Distribution
        plt.subplot(2, 2, 1)
        sns.boxplot(x='Brand', y='Visibility_Score', data=self.data)
        plt.title('Brand Visibility Score Distribution')
        plt.xticks(rotation=45)
        
        # 2. Sentiment Score Heatmap
        plt.subplot(2, 2, 2)
        sentiment_pivot = self.data.pivot_table(
            index='Brand', 
            columns='Platform', 
            values='Sentiment_Score', 
            aggfunc='mean'
        )
        sns.heatmap(sentiment_pivot, annot=True, cmap='coolwarm', center=0)
        plt.title('Brand Sentiment Across Platforms')
        
        # 3. Innovation Mentions Trend
        plt.subplot(2, 2, 3)
        innovation_trend = self.temporal_trend_analysis()
        for brand in innovation_trend['Brand'].unique():
            brand_data = innovation_trend[innovation_trend['Brand'] == brand]
            plt.plot(brand_data['Month'], brand_data['Innovation_Mentions'], label=brand)
        plt.title('Innovation Mentions Over Time')
        plt.xlabel('Month')
        plt.ylabel('Innovation Mentions')
        plt.legend()
        
        # 4. Visibility vs Sentiment Scatter
        plt.subplot(2, 2, 4)
        performance_analysis = self.brand_platform_performance_analysis()
        plt.scatter(
            performance_analysis['Avg_Visibility'], 
            performance_analysis['Avg_Sentiment'], 
            c=performance_analysis['Total_Innovations'], 
            cmap='viridis'
        )
        plt.title('Visibility vs Sentiment')
        plt.xlabel('Average Visibility Score')
        plt.ylabel('Average Sentiment Score')
        plt.colorbar(label='Total Innovations')
        
        plt.tight_layout()
        plt.savefig('data/pharma_ai_visibility_analysis.png')
        plt.close()
    
    def export_insights_report(self):
        """
        Generate a comprehensive insights report
        
        Returns:
            dict: Comprehensive analysis insights
        """
        insights = {
            'Performance_Metrics': self.brand_platform_performance_analysis().to_dict(orient='records'),
            'Temporal_Trends': self.temporal_trend_analysis().to_dict(orient='records'),
            'Overall_Insights': {
                'Top_Performing_Brand': self.data.groupby('Brand')['Visibility_Score'].mean().idxmax(),
                'Most_Innovative_Platform': self.data.groupby('Platform')['Innovation_Mentions'].sum().idxmax(),
                'Sentiment_Leaders': self.data.groupby('Brand')['Sentiment_Score'].mean().nlargest(2).to_dict()
            }
        }
        
        # Export insights to JSON
        import json
        with open('data/pharma_ai_visibility_insights.json', 'w') as f:
            json.dump(insights, f, indent=2)
        
        return insights

def main():
    # Initialize analysis
    analyzer = PharmaAIVisibilityAnalysis()
    
    # Generate visualization
    analyzer.generate_advanced_visualization()
    
    # Export insights report
    insights = analyzer.export_insights_report()
    
    # Print key insights
    print("Pharma AI Visibility Insights:")
    print(f"Top Performing Brand: {insights['Overall_Insights']['Top_Performing_Brand']}")
    print(f"Most Innovative Platform: {insights['Overall_Insights']['Most_Innovative_Platform']}")
    print("Sentiment Leaders:", insights['Overall_Insights']['Sentiment_Leaders'])

if __name__ == "__main__":
    main()
