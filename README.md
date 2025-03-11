# Project Gutenberg Proper Noun Analyzer

## Overview
This project analyzes text from Project Gutenberg ebooks to extract and count proper nouns, generating frequency reports and visualizations. It uses parallel processing to fetch book data efficiently and leverages NLTK for natural language processing. The output includes individual book reports, a total frequency report, and a bar chart of the top proper nouns.

## Features
1. Fetches ebook text from Project Gutenberg in parallel.
2. Extracts proper nouns using NLTK's part-of-speech tagging.
3. Generates JSON reports for individual books and a cumulative report.
4. Creates a bar chart visualizing the top proper nouns.
5. Tracks and displays performance metrics (retrieval, processing, and reporting times).

## Prerequisites
* Python 3.7+
* Required libraries:
* nltk (for text processing)
* matplotlib (for visualization)
* Standard Python libraries ( os, json, time)


## Installation
1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt

## Usage
Run the Script: From the src directory, execute
python main.py