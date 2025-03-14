
"""Contains Project Gutenberg book URLs."""

def get_book_urls() -> list[str]:
    """Returns a list of Project Gutenberg book URLs."""
    base_url = "https://www.gutenberg.org/cache/epub/"
    sample_books = [
         "75584/pg75584-images.html",    
        "75583/pg75583-images.html",   
        "75582/pg75582-images.html",   
        "75580/pg75580-images.html", 
        "75579/pg75579-images.html", 
        "75578/pg75578-images.html", 
        "75577/pg75577-images.html", 
        "75576/pg75576-images.html", 
        "17764/pg17764-images.html", 
        "17863/pg17863-images.html", 
        "18837/pg18837-images.html", 
        "17635/pg17635-images.html", 
        "17635/pg17635-images.html", 
        "17732/pg17732-images.html", 
        "75584/pg75584-images.html",    
        "75579/pg75579-images.html",   
        "75585/pg75585-images.html",   
        "17635/pg17635-images.html", 
        "75580/pg75580-images.html", 
        "75578/pg75578-images.html", 
        "75586/pg75586-images.html", 
        "59345/pg59345-images.html", 
        "203/pg203-images.html", 
        "75577/pg75577-images.html", 
        "75543/pg75543-images.html", 
        "75385/pg75385-images.html", 
        "462/pg462-images.html", 
        "75359/pg75359-images.html", 
         "75289/pg75289-images.html",    
        "4107/pg4107-images.html",   
        "75356/pg75356-images.html",   
        "75343/pg75343-images.html", 
        "75381/pg75381-images.html", 
        "75376/pg75376-images.html", 
        "75542/pg75542-images.html", 
        "75533/pg75533-images.html", 
        "75361/pg75361-images.html", 
        "75523/pg75523-images.html", 
        "23060/pg23060-images.html", 
        "1443/pg1443-images.html", 
        "1639/pg1639-images.html", 
        "1559/pg1559-images.html", 
         "1856/pg1856-images.html",    
        "14100/pg14100.html",   
        "75540/pg75540-images.html",   
        "75538/pg75538-images.html", 
        "13322/pg13322-images.html", 
        "75487/pg75487-images.html", 
        "75534/pg75534-images.html", 
        "75370/pg75370-images.html", 
    ]
    return [base_url + book_id for book_id in sample_books][:50]