#!/bin/bash

# Script to replace http:// with https:// in all Markdown files across the site
echo "Starting conversion of HTTP to HTTPS links in all Markdown files..."

# Find all Markdown files in the project
MD_FILES=$(find . -name "*.md" -type f -not -path "*/\.*")
echo "Found $(echo "$MD_FILES" | wc -l | xargs) Markdown files to process"

# Replace Google Calendar embeds
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.google.com/calendar|https://www.google.com/calendar|g' {} \;
echo "- Google Calendar embeds updated"

# Replace YouTube embeds
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|<iframe src="http://www.youtube.com/embed/|<iframe src="https://www.youtube.com/embed/|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|<iframe width="[^"]*" height="[^"]*" src="http://www.youtube.com|<iframe width="[^"]*" height="[^"]*" src="https://www.youtube.com|g' {} \;
echo "- YouTube iframe embeds updated"

# Replace Facebook plugins
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.facebook.com/plugins|https://www.facebook.com/plugins|g' {} \;
echo "- Facebook plugins updated"

# Replace common domains
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://vk.com|https://vk.com|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.facebook.com|https://www.facebook.com|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.slideshare.net|https://www.slideshare.net|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.cvk.gov.ua|https://www.cvk.gov.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://president.gov.ua|https://president.gov.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://russia.mfa.gov.ua|https://russia.mfa.gov.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://zakon3.rada.gov.ua|https://zakon3.rada.gov.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://brovary-rada.gov.ua|https://brovary-rada.gov.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.nerc.gov.ua|https://www.nerc.gov.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://www.epravda.com.ua|https://www.epravda.com.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://tsn.ua|https://tsn.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://forbes.ua|https://forbes.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://vstup.info|https://vstup.info|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://bikeportal.org.ua|https://bikeportal.org.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://f.img.com.ua|https://f.img.com.ua|g' {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' 's|http://podrobnosti.ua|https://podrobnosti.ua|g' {} \;
echo "- Common domain links updated"

# Find any remaining HTTP links in Markdown files
echo "Checking for remaining HTTP links in Markdown files..."
find . -name "*.md" -type f -not -path "*/\.*" -not -path "./fix_all_md_links.sh" -exec grep -l "http://" {} \; | xargs -I{} echo "Still contains HTTP: {}"

echo "Conversion complete!"
echo "Check the list above for any files that still contain 'http://' links that need manual review." 