#!/usr/bin/env python3

import yaml
import csv
import re

def read_csv_users():
    """Read users from wp_users_info.csv with proper encoding"""
    users = []
    try:
        with open('wp_users_info.csv', 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert user_login to lowercase
                row['user_login'] = row['user_login'].lower()
                users.append(row)
        print(f"Successfully read {len(users)} users from CSV")
        return users
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return []

def read_existing_authors():
    """Read existing authors from _data/authors.yml"""
    try:
        with open('_data/authors.yml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading authors.yml: {str(e)}")
        return []

def create_author_entry(user_data):
    """Create a new author entry from CSV data"""
    return {
        'name': user_data['display_name'],
        'login': user_data['user_login'],
        'avatarUrl': user_data['avatar'] if user_data['avatar'] else '/avatars/v3-avatar.jpg',
        'description': user_data['description'] if user_data['description'] else f"Автор публікацій МПЗ Бровари {user_data['user_login']}"
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
    print("Reading users from CSV...")
    csv_users = read_csv_users()
    
    if not csv_users:
        print("No users found in CSV. Exiting.")
        return
    
    print("Reading existing authors...")
    existing_authors = read_existing_authors()
    print(f"Found {len(existing_authors)} existing authors")
    
    # Create a dictionary of existing authors for easier lookup
    existing_authors_dict = {author['login'].lower(): author for author in existing_authors}
    
    # Track statistics
    updated_count = 0
    added_count = 0
    removed_count = 0
    
    # List of users to exclude
    excluded_users = ['serhij batuk', 'admin']
    
    print("Processing users...")
    # First, remove excluded users
    existing_authors = [author for author in existing_authors if author['login'].lower() not in excluded_users]
    removed_count = len(excluded_users)
    
    for user in csv_users:
        login = user['user_login'].lower()
        if login in excluded_users:
            continue
            
        if login in existing_authors_dict:
            # Update existing author
            existing_author = existing_authors_dict[login]
            # Update only if there are differences
            if (existing_author['name'] != user['display_name'] or 
                existing_author['login'] != login or
                existing_author['avatarUrl'] != user['avatar'] or
                existing_author['description'] != user['description']):
                existing_author['name'] = user['display_name']
                existing_author['login'] = login
                existing_author['avatarUrl'] = user['avatar'] if user['avatar'] else '/avatars/v3-avatar.jpg'
                existing_author['description'] = user['description'] if user['description'] else f"Автор публікацій МПЗ Бровари {login}"
                updated_count += 1
        else:
            # Add new author
            new_author = create_author_entry(user)
            existing_authors.append(new_author)
            added_count += 1
    
    print(f"Removed {removed_count} excluded authors")
    print(f"Updated {updated_count} existing authors")
    print(f"Added {added_count} new authors")
    
    print("Saving updated authors.yml...")
    save_authors_with_spacing(existing_authors, '_data/authors.yml')
    
    print("Done! Authors have been updated in _data/authors.yml")

if __name__ == "__main__":
    main() 