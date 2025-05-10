import os
import yaml
import shutil

def load_authors():
    with open('_data/authors.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_author_pages():
    # Create author directory if it doesn't exist
    if not os.path.exists('author'):
        os.makedirs('author')

    # Load authors data
    authors = load_authors()

    # Load template
    with open('author-template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # Generate pages for each author
    for author in authors:
        # Prepare front matter with author login
        front_matter = f"""---\nlayout: default\ntitle: {author['name']}\ndescription: {author.get('description', '')}\nauthor: {author['login']}\n---\n"""
        # Prepare content (skip template's front matter)
        content_body = template.split('---', 2)[-1].strip()
        # Combine front matter and content
        content = front_matter + '\n' + content_body
        # Write author page
        with open(f'author/{author["login"]}.html', 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    generate_author_pages() 