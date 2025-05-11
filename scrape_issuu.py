#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import re

def get_page_links(url):
    """Get all publication links from a single page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all publication links
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Look for publication links that match the pattern
            if '/docs/' in href and not href.endswith('/docs/'):
                full_url = f"https://issuu.com{href}" if href.startswith('/') else href
                links.append(full_url)
        
        return links
    except Exception as e:
        print(f"Error fetching page {url}: {str(e)}")
        return []

def scrape_issuu_profile(base_url, max_pages):
    """Scrape all publication links from an Issuu profile, grouped by page"""
    all_links_by_page = []
    seen_links = set()
    
    for page in range(1, max_pages + 1):
        page_url = f"{base_url}/{page}"
        print(f"Scraping page {page}...")
        page_links = get_page_links(page_url)
        # Only add links that haven't been seen yet, but keep order
        unique_links = []
        for link in page_links:
            if link not in seen_links:
                unique_links.append(link)
                seen_links.add(link)
        all_links_by_page.append((page, unique_links))
        time.sleep(2)
    return all_links_by_page

def save_links_to_file_grouped(links_by_page, filename):
    """Save links to a text file, grouped by page with header and empty line"""
    with open(filename, 'w', encoding='utf-8') as f:
        for page, links in links_by_page:
            f.write(f"# Page {page}\n")
            for link in links:
                f.write(f"{link}\n")
            f.write("\n")

def main():
    base_url = "https://issuu.com/livoberezhna"
    max_pages = 3  # Testing with just 3 pages
    output_file = "issuu_links.txt"
    
    print(f"Starting to scrape {base_url}")
    print(f"Will process {max_pages} pages...")
    
    links_by_page = scrape_issuu_profile(base_url, max_pages)
    total_links = sum(len(links) for _, links in links_by_page)
    print(f"\nFound {total_links} unique publication links")
    save_links_to_file_grouped(links_by_page, output_file)
    print(f"Links have been saved to {output_file}")

if __name__ == "__main__":
    main() 