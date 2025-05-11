import csv
import os
import re
from pathlib import Path

def extract_youtube_id(url):
    """Extract YouTube video ID from various URL formats."""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?]+)',
        r'youtube\.com\/embed\/([^&\n?]+)',
        r'youtube\.com\/v\/([^&\n?]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def process_posts():
    # Read the CSV file
    with open('wp_postmeta.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        youtube_links = {row['post_name']: row['meta_value'] for row in reader}
    
    print(f"Total YouTube links in CSV: {len(youtube_links)}")
    
    # Get all post filenames
    posts_dir = Path('_posts')
    post_files = list(posts_dir.glob('*.md'))
    print(f"Total posts found: {len(post_files)}")
    
    # Track statistics
    already_has_link = 0
    not_found = 0
    updated = 0
    
    # Process each post
    for post_file in post_files:
        # Extract post name from filename (remove date and .md extension)
        post_name = post_file.stem.split('-', 3)[-1]
        
        if post_name in youtube_links:
            # Read the post content
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if the post already has the YouTube link
            if youtube_links[post_name] not in content:
                # Add the YouTube link at the end of the content
                content = content.rstrip() + f"\n\n{youtube_links[post_name]}\n"
                
                # Write the updated content back to the file
                with open(post_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {post_file.name} with YouTube link")
                updated += 1
            else:
                print(f"Skipped {post_file.name} - already has YouTube link")
                already_has_link += 1
        else:
            print(f"Warning: No YouTube link found for {post_file.name}")
            not_found += 1
    
    print("\nSummary:")
    print(f"Total YouTube links in CSV: {len(youtube_links)}")
    print(f"Total posts found: {len(post_files)}")
    print(f"Posts updated: {updated}")
    print(f"Posts already had link: {already_has_link}")
    print(f"Posts without matching YouTube link: {not_found}")

if __name__ == '__main__':
    process_posts() 