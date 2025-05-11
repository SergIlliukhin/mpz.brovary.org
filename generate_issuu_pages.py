#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse, unquote

def create_issuu_folder():
    """Create issuu folder if it doesn't exist"""
    if not os.path.exists('issuu'):
        os.makedirs('issuu')
        print("Created 'issuu' folder")

def get_publication_links(url):
    """Get all publication links from a single page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '/docs/' in href and not href.endswith('/docs/'):
                full_url = f"https://issuu.com{href}" if href.startswith('/') else href
                links.append(full_url)
        
        return links
    except Exception as e:
        print(f"Error fetching page {url}: {str(e)}")
        return []

def generate_html_content(doc_url, title):
    """Generate HTML content with embedded Issuu document"""
    # Extract the username and document ID from the URL
    parsed_url = urlparse(doc_url)
    path_parts = parsed_url.path.split('/')
    username = path_parts[1]  # The username is the first part after the domain
    doc_id = path_parts[-1] if path_parts[-1] else path_parts[-2]
    
    # Construct the correct embed URL
    embed_url = f"https://e.issuu.com/embed.html?u={username}&d={doc_id}"
    
    return f'''<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f5f5;
        }}
        .container {{
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        iframe {{
            border: none;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <iframe src="{embed_url}" 
                width="100%" 
                height="800" 
                frameborder="0" 
                allowfullscreen>
        </iframe>
    </div>
</body>
</html>'''

def save_html_file(doc_url, output_folder):
    """Save HTML file with embedded Issuu document"""
    try:
        # Extract document name from URL
        parsed_url = urlparse(doc_url)
        path_parts = parsed_url.path.split('/')
        doc_name = path_parts[-1] if path_parts[-1] else path_parts[-2]
        doc_name = unquote(doc_name)  # Decode URL-encoded characters
        
        # Generate HTML content
        html_content = generate_html_content(doc_url, doc_name)
        
        # Save to file
        output_path = os.path.join(output_folder, f"{doc_name}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Created: {output_path}")
        return True
    except Exception as e:
        print(f"Error creating HTML for {doc_url}: {str(e)}")
        return False

def main():
    base_url = "https://issuu.com/livoberezhna"
    max_pages = 3
    output_folder = "issuu"
    
    print(f"Starting to process Issuu publications from {base_url}")
    print(f"Will process {max_pages} pages...")
    
    # Create output folder
    create_issuu_folder()
    
    # Process each page
    total_processed = 0
    for page in range(1, max_pages + 1):
        page_url = f"{base_url}/{page}"
        print(f"\nProcessing page {page}...")
        
        # Get publication links
        links = get_publication_links(page_url)
        print(f"Found {len(links)} publications on page {page}")
        
        # Generate HTML files
        for link in links:
            if save_html_file(link, output_folder):
                total_processed += 1
        
        # Be nice to the server
        if page < max_pages:
            time.sleep(2)
    
    print(f"\nCompleted! Generated {total_processed} HTML files in the '{output_folder}' folder")

if __name__ == "__main__":
    main() 