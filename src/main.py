import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
from data_retriever import DataRetriever
from book_urls import get_book_urls  
from text_processor import TextProcessor
from report_generator import ReportGenerator
from visualizer import Visualizer
import os

def main():
    """Main execution function for the Gutenberg Analyzer."""
    
    # Initialize components
    retriever = DataRetriever(max_workers=5)
    processor = TextProcessor()
    reporter = ReportGenerator()
    visualizer = Visualizer()
    
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    
    # Get and process books
    urls = get_book_urls()  # Call the imported function directly
    book_data = retriever.fetch_books_parallel(urls)
    
    # Generate individual reports
    reports = {}
    for url, text in book_data:
        if text:
            book_id = url.split('/')[-1].replace('.txt', '')
            frequencies = processor.extract_proper_nouns(text)
            report = reporter.generate_book_report(book_id, frequencies)
            reports.update(report)
            reporter.save_report(report, f'report_{book_id}.json')
    
    # Generate and save total report
    total_report = reporter.generate_total_report()
    reporter.save_report(total_report, 'total_frequency_report.json')
    
    # Create visualization
    visualizer.create_bar_chart(total_report)
    
    # Print performance metrics
    print("\nPerformance Metrics:")
    print(f"Data Retrieval: {retriever.retrieval_time:.2f} seconds")
    print(f"Text Processing: {processor.processing_time:.2f} seconds")
    print(f"Report Generation: {reporter.reporting_time:.2f} seconds")

if __name__ == "__main__":
    main()