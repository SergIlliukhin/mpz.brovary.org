import os
import re
from pathlib import Path

def process_caption(match):
    content = match.group(1).strip()
    # Regex to match an optional link-wrapped image markdown at the start
    img_link_pattern = r'^(\[!\[.*?\]\(.*?\)\]\(.*?\)|!\[.*?\]\(.*?\))\s*(.*)$'
    img_link_match = re.match(img_link_pattern, content)
    if img_link_match:
        image_markdown = img_link_match.group(1).strip()
        caption_text = img_link_match.group(2).strip()
        return f'{image_markdown} `{caption_text}`'
    else:
        # fallback: just wrap the whole content in backticks
        return f'`{content}`'

def process_file(file_path):
    print(f"\nProcessing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match [caption] tags with their content, handling escaped brackets
    pattern = r'\\\[caption[^\]]*\\\](.*?)\\\[/caption\\\]'
    
    # Find all matches first to debug
    matches = re.finditer(pattern, content, re.DOTALL)
    found = False
    for match in matches:
        found = True
        print(f"Found caption in {file_path}:")
        print(f"Original: {match.group(0)}")
        print(f"Content: {match.group(1)}")
    
    if not found:
        print(f"No captions found in {file_path}")
        return
    
    # Replace all matches
    new_content = re.sub(pattern, process_caption, content, flags=re.DOTALL)
    
    # Write back only if changes were made
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes made to {file_path}")

def main():
    # Process files in _posts directory
    posts_dir = Path('_posts')
    if posts_dir.exists():
        print(f"\nProcessing files in {posts_dir}")
        for file in posts_dir.glob('*.md'):
            process_file(file)
    else:
        print(f"Directory not found: {posts_dir}")
    
    # Process files in _pages directory
    pages_dir = Path('_pages')
    if pages_dir.exists():
        print(f"\nProcessing files in {pages_dir}")
        for file in pages_dir.glob('*.md'):
            process_file(file)
    else:
        print(f"Directory not found: {pages_dir}")

if __name__ == '__main__':
    main() 