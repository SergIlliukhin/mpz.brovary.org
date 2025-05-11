#!/usr/bin/env python3

import yaml
import re

def read_missing_authors():
    """Read missing authors from missing_authors.txt"""
    authors = []
    with open('missing_authors.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract author names from the list
        matches = re.findall(r'- ([^\n]+)', content)
        return [m.strip() for m in matches if m.strip()]

def read_existing_authors():
    """Read existing authors from _data/authors.yml"""
    try:
        with open('_data/authors.yml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading authors.yml: {str(e)}")
        return []

def create_author_entry(login):
    """Create a new author entry with the specified format"""
    return {
        'name': login,
        'login': login,
        'avatarUrl': '/avatars/v3-avatar.jpg',
        'description': f"Автор публікацій МПЗ Бровари {login}"
    }

def save_authors_with_spacing(authors, filename):
    """Save authors to YAML file with empty lines between records and proper quoting"""
    # Custom YAML dumper to ensure proper quoting
    class QuotedString(str): pass
    
    def quoted_presenter(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
    
    yaml.add_representer(QuotedString, quoted_presenter)
    
    # Convert all string values to QuotedString
    def quote_strings(obj):
        if isinstance(obj, dict):
            return {k: quote_strings(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [quote_strings(item) for item in obj]
        elif isinstance(obj, str):
            return QuotedString(obj)
        return obj
    
    # Quote all string values
    quoted_authors = quote_strings(authors)
    
    # Dump to string with proper formatting
    yaml_str = yaml.dump(quoted_authors, 
                        allow_unicode=True, 
                        sort_keys=False,
                        default_flow_style=False,
                        width=float("inf"))
    
    # Add empty line between records
    yaml_str = re.sub(r'\n- ', '\n\n- ', yaml_str)
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(yaml_str)

def main():
    print("Reading missing authors...")
    missing_authors = read_missing_authors()
    print(f"Found {len(missing_authors)} missing authors")
    
    print("Reading existing authors...")
    existing_authors = read_existing_authors()
    print(f"Found {len(existing_authors)} existing authors")
    
    print("Adding new authors...")
    for login in missing_authors:
        new_author = create_author_entry(login)
        existing_authors.append(new_author)
        print(f"Added: {login}")
    
    print("Saving updated authors.yml...")
    save_authors_with_spacing(existing_authors, '_data/authors.yml')
    
    print("Done! Authors have been added to _data/authors.yml")

if __name__ == "__main__":
    main() 