import os
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match YouTube links in brackets
    # Handles youtube.com, m.youtube.com, and youtu.be formats
    pattern = r'\((https?://(?:www\.|m\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^)]+)\)'
    
    # Replace with URL surrounded by spaces (replacing brackets with spaces)
    new_content = re.sub(pattern, r' \1 ', content)
    
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

def main():
    # Walk through all directories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    main() 