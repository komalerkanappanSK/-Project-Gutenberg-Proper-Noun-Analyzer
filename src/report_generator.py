from collections import Counter
from typing import Dict, List
import json
import time

class ReportGenerator:
    """Generates and saves frequency reports."""
    
    def __init__(self):
        self.reporting_time = 0.0
        self.total_frequencies = Counter()
    
    def generate_book_report(self, book_id: str, frequencies: Counter) -> Dict:
        """Generates a sorted report for a single book."""
        start_time = time.time()
        report = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
        self.total_frequencies.update(frequencies)
        self.reporting_time += time.time() - start_time
        return {book_id: report}
    
    def generate_total_report(self) -> Dict:
        """Generates a sorted total frequency report."""
        start_time = time.time()
        report = dict(sorted(self.total_frequencies.items(), key=lambda x: x[1], reverse=True))
        self.reporting_time += time.time() - start_time
        return report
    
    def save_report(self, report: Dict, filename: str) -> None:
        """Saves a report to a JSON file."""
        with open(f"reports/{filename}", 'w') as f:
            json.dump(report, f, indent=4)