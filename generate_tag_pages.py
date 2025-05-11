#!/usr/bin/env python3

import yaml
import os
from pathlib import Path

def generate_tag_pages(tags_file='_data/wp_tags.yml', output_dir='tag'):
    """
    Generate tag pages from tags YAML data.
    
    Args:
        tags_file (str): Path to the tags YAML file
        output_dir (str): Directory to store the generated tag pages
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read tags data
    with open(tags_file, 'r', encoding='utf-8') as f:
        tags = yaml.safe_load(f)
    
    # Read template
    with open('tag-template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Generate a page for each tag
    for tag in tags:
        # Create direct HTML file for the tag
        output_file = os.path.join(output_dir, f"{tag['slug']}.html")
        
        # Escape quotes in the title for YAML front matter
        safe_title = tag['name'].replace('"', '\\"')
        
        # Create front matter with tag and escaped title
        front_matter = f'''---
layout: default
title: "{safe_title}"
tag: "{tag['slug']}"
---

'''
        # Get the content part of the template (everything after the front matter)
        content = template.split('---', 2)[-1].strip()
        
        # Combine front matter and content
        final_content = front_matter + content
        
        # Write the file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"Generated tag page: {output_file}")

if __name__ == "__main__":
    generate_tag_pages() 