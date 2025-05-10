#!/usr/bin/env python3

import yaml
import os
from pathlib import Path

def generate_category_pages(categories_file='_data/wp_categories.yml', output_dir='action'):
    """
    Generate category pages from categories YAML data.
    
    Args:
        categories_file (str): Path to the categories YAML file
        output_dir (str): Directory to store the generated category pages
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read categories data
    with open(categories_file, 'r', encoding='utf-8') as f:
        categories = yaml.safe_load(f)
    
    # Read template
    with open('category-template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Generate a page for each category
    for category in categories:
        # Create category directory
        category_dir = os.path.join(output_dir, category['slug'])
        os.makedirs(category_dir, exist_ok=True)
        
        # Create index.html in the category directory
        output_file = os.path.join(category_dir, 'index.html')
        
        # Replace placeholders in template
        content = template.replace('{{ page.title }}', category['name'])
        content = content.replace('{{ page.category }}', category['slug'])
        
        # Write the file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Generated category page: {output_file}")

if __name__ == "__main__":
    generate_category_pages() 