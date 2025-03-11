import matplotlib.pyplot as plt
from typing import Dict

class Visualizer:
    """Creates visualizations of frequency data."""
    
    def create_bar_chart(self, frequencies: Dict, output_file: str = 'proper_nouns_visualization.png') -> None:
        """Creates a bar chart of top 10 proper nouns."""
        top_10 = dict(list(frequencies.items())[:10])
        
        plt.figure(figsize=(12, 6))
        plt.bar(top_10.keys(), top_10.values())
        plt.xticks(rotation=45)
        plt.xlabel('Proper Nouns')
        plt.ylabel('Frequency')
        plt.title('Top 10 Proper Nouns Across All Books')
        plt.tight_layout()
        plt.savefig(f'reports/{output_file}')
        plt.close()