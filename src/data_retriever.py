import urllib.request
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional
import time
from book_urls import get_book_urls  

class DataRetriever:
    """Handles retrieval of text data from Project Gutenberg."""
    
    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers
        self.retrieval_time = 0.0
        
    def fetch_book_text(self, url: str) -> Optional[str]:
        """Fetches text content from a given URL."""
        start_time = time.time()
        try:
            with urllib.request.urlopen(url) as response:
                text = response.read().decode('utf-8')
            self.retrieval_time += time.time() - start_time
            return text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def fetch_books_parallel(self, urls: List[str]) -> List[tuple[str, Optional[str]]]:
        """Fetches multiple books in parallel using ThreadPoolExecutor."""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(
                lambda url: (url, self.fetch_book_text(url)), 
                urls
            ))
        return results

# Example usage
if __name__ == "__main__":
    retriever = DataRetriever()
    book_urls = get_book_urls()  # Get URLs from the imported function
    books = retriever.fetch_books_parallel(book_urls)