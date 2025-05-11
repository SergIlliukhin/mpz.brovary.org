#!/usr/bin/env python3

import os
import yaml
from pathlib import Path

SITE_URL = "https://mpz.brovary.org"

def get_author_links():
    """Get links to all author pages"""
    authors = []
    authors_file = Path("_data/authors.yml")
    if authors_file.exists():
        with open(authors_file, 'r', encoding='utf-8') as f:
            authors_data = yaml.safe_load(f)
            for author in authors_data:
                # If the author is a dict, use the 'login' field
                if isinstance(author, dict) and 'login' in author:
                    login = author['login']
                else:
                    login = author if isinstance(author, str) else str(author)
                authors.append(f"{SITE_URL}/author/{login}/")
    return sorted(authors)

def get_pages_links():
    """Get links to all pages in _pages directory"""
    pages = []
    pages_dir = Path("_pages")
    if pages_dir.exists():
        for file in pages_dir.glob("*.md"):
            # Convert filename to URL path
            # Remove date prefix and .md extension
            name = file.stem
            if name.startswith("20"):  # If starts with year
                name = name[11:]  # Remove date prefix (YYYY-MM-DD-)
            pages.append(f"{SITE_URL}/{name}/")
    return sorted(pages)

def get_posts_links():
    """Get links to all posts in _posts directory"""
    posts = []
    posts_dir = Path("_posts")
    if posts_dir.exists():
        for file in posts_dir.glob("*.md"):
            # Convert filename to URL path
            # Remove date prefix and .md extension
            name = file.stem
            if name.startswith("20"):  # If starts with year
                name = name[11:]  # Remove date prefix (YYYY-MM-DD-)
            posts.append(f"{SITE_URL}/{name}/")
    return sorted(posts)

def get_tag_links():
    """Get links to all tag pages"""
    tags = []
    tags_file = Path("_data/wp_tags.yml")
    if tags_file.exists():
        with open(tags_file, 'r', encoding='utf-8') as f:
            tags_data = yaml.safe_load(f)
            for tag in tags_data:
                tags.append(f"{SITE_URL}/tag/{tag['slug']}/")
    return sorted(tags)

def get_category_links():
    """Get links to all category pages"""
    categories = []
    categories_file = Path("_data/wp_categories.yml")
    if categories_file.exists():
        with open(categories_file, 'r', encoding='utf-8') as f:
            categories_data = yaml.safe_load(f)
            for category in categories_data:
                categories.append(f"{SITE_URL}/action/{category['slug']}/")
    return sorted(categories)

def generate_sitemap():
    """Generate sitemap.txt with all required links"""
    # Get all links in specified order
    author_links = get_author_links()
    category_links = get_category_links()
    tag_links = get_tag_links()
    post_links = get_posts_links()
    page_links = get_pages_links()
    
    # Write to sitemap.txt
    with open("sitemap.txt", "w", encoding="utf-8") as f:
        # Write author links
        for link in author_links:
            f.write(f"{link}\n")
        
        # Write category links
        for link in category_links:
            f.write(f"{link}\n")
        
        # Write tag links
        for link in tag_links:
            f.write(f"{link}\n")
        
        # Write post links
        for link in post_links:
            f.write(f"{link}\n")
        
        # Write page links
        for link in page_links:
            f.write(f"{link}\n")
    
    total_links = len(author_links) + len(category_links) + len(tag_links) + len(post_links) + len(page_links)
    print(f"Generated sitemap.txt with {total_links} links")

if __name__ == "__main__":
    generate_sitemap() 