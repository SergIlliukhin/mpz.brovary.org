#!/bin/bash

# Script to replace YouTube embeds from HTTP to HTTPS
echo "Starting conversion of YouTube embeds from HTTP to HTTPS..."

# Replace <iframe src="http://www.youtube.com/embed/ with <iframe src="https://www.youtube.com/embed/
find _posts -name "*.md" -type f -exec sed -i '' 's|<iframe src="http://www.youtube.com/embed/|<iframe src="https://www.youtube.com/embed/|g' {} \;
echo "- YouTube iframe embeds updated"

# Replace any other potential problematic URLs with Liquid syntax
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.facebook.com/plugins/likebox.php|https://www.facebook.com/plugins/likebox.php|g' {} \;
echo "- Facebook plugins updated"

echo "Conversion complete!"
echo "GitHub Pages build should now work without Liquid syntax errors." 