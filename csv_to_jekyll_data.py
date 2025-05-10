#!/usr/bin/env python3

import csv
import yaml
import os
import sys
from pathlib import Path
import re

class CustomDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, indentless)

def escape_yaml_string(value):
    # Replace any sequence of backslashes before a double quote with a single backslash
    value = re.sub(r'\\+"', r'\"', value)
    # Escape any remaining unescaped double quotes
    value = value.replace('"', '\"')
    return value

def represent_dict_with_quoted_fields(dumper, data):
    items = []
    for key, value in data.items():
        if key in ('name', 'slug'):
            value = escape_yaml_string(str(value))
            node = dumper.represent_scalar('tag:yaml.org,2002:str', value, style='"')
        else:
            node = dumper.represent_data(value)
        items.append((dumper.represent_data(key), node))
    return yaml.nodes.MappingNode('tag:yaml.org,2002:map', items)

CustomDumper.add_representer(dict, represent_dict_with_quoted_fields)

def csv_to_yaml(csv_file, output_dir='_data'):
    """
    Convert a CSV file to a YAML file for Jekyll data.
    
    Args:
        csv_file (str): Path to the input CSV file
        output_dir (str): Directory to store the output YAML file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the base filename without extension
    base_name = Path(csv_file).stem
    
    # Read CSV file
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    # Convert term_id to integer and ensure name and slug are strings
    for record in data:
        if 'term_id' in record:
            record['term_id'] = int(record['term_id'])
        if 'name' in record:
            record['name'] = str(record['name'])
        if 'slug' in record:
            record['slug'] = str(record['slug'])
    
    # Convert to YAML with custom formatting
    output_file = os.path.join(output_dir, f"{base_name}.yml")
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write each record separately with empty lines between them
        for i, record in enumerate(data):
            yaml.dump([record], f, allow_unicode=True, sort_keys=False, Dumper=CustomDumper, default_flow_style=False)
            if i < len(data) - 1:  # Don't add empty line after the last record
                f.write('\n')
    
    print(f"Converted {csv_file} to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python csv_to_jekyll_data.py <csv_file> [output_directory]")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else '_data'
    
    if not os.path.exists(csv_file):
        print(f"Error: File {csv_file} does not exist")
        sys.exit(1)
    
    csv_to_yaml(csv_file, output_dir)

if __name__ == "__main__":
    main() 