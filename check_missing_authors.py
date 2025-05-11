#!/usr/bin/env python3

import os
import yaml
import re
from pathlib import Path

def load_authors():
    """Load authors from _data/authors.yml as a set of logins"""
    try:
        with open('_data/authors.yml', 'r', encoding='utf-8') as f:
            authors_data = yaml.safe_load(f)
            # authors_data is a list of dicts, each with a 'login' key
            return set(a['login'] for a in authors_data if 'login' in a)
    except Exception as e:
        print(f"Error loading authors.yml: {str(e)}")
        return set()

def extract_author_from_front_matter(content):
    """Extract author.username from YAML front matter (robust, supports nested)"""
    # Only look at the YAML front matter (between ---)
    fm_match = re.match(r'^---\s*([\s\S]+?)---', content)
    if not fm_match:
        return None
    front_matter = fm_match.group(1)
    try:
        data = yaml.safe_load(front_matter)
        if isinstance(data, dict) and 'author' in data:
            author = data['author']
            if isinstance(author, dict) and 'username' in author:
                return str(author['username'])
    except Exception as e:
        pass
    return None

def scan_markdown_files():
    """Scan all markdown files for author usernames"""
    found_authors = set()
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        author = extract_author_from_front_matter(content)
                        if author:
                            found_authors.add(author)
                except Exception as e:
                    print(f"Error reading {file_path}: {str(e)}")
    return found_authors

def find_missing_authors(found_authors, existing_logins):
    """Find authors that are in markdown files but not in authors.yml"""
    return found_authors - existing_logins

def save_missing_authors(missing_authors):
    """Save missing authors to a text file"""
    if missing_authors:
        with open('missing_authors.txt', 'w', encoding='utf-8') as f:
            f.write("Authors found in markdown files but missing from _data/authors.yml:\n\n")
            for author in sorted(missing_authors):
                f.write(f"- {author}\n")
        print(f"\nFound {len(missing_authors)} missing authors. See missing_authors.txt for details.")
    else:
        print("\nNo missing authors found!")

def save_existing_authors(existing_authors):
    """Save existing authors to a text file"""
    if existing_authors:
        with open('existing_authors.txt', 'w', encoding='utf-8') as f:
            f.write("Authors found in markdown files and present in _data/authors.yml:\n\n")
            for author in sorted(existing_authors):
                f.write(f"- {author}\n")
        print(f"Found {len(existing_authors)} existing authors. See existing_authors.txt for details.")
    else:
        print("No existing authors found!")

def main():
    print("Loading authors from _data/authors.yml...")
    existing_logins = load_authors()
    print(f"Found {len(existing_logins)} authors in authors.yml")
    print("Scanning markdown files for author usernames...")
    found_authors = scan_markdown_files()
    print(f"Found {len(found_authors)} unique authors in markdown files")
    missing_authors = find_missing_authors(found_authors, existing_logins)
    existing_authors = found_authors & existing_logins
    save_missing_authors(missing_authors)
    save_existing_authors(existing_authors)

if __name__ == "__main__":
    main() 