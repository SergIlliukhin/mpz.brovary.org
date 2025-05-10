import os
import re

def update_author_username_in_md_files(directory='_posts'):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Use regex to find and replace author.username with lowercase version
            updated_content = re.sub(r'(author:\s*username:\s*)([^\n]+)', lambda m: m.group(1) + m.group(2).lower(), content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)

if __name__ == '__main__':
    update_author_username_in_md_files() 