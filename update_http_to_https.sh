#!/bin/bash

# Script to replace http:// with https:// in all Markdown files
echo "Starting conversion of HTTP to HTTPS links in Markdown files..."

# Replace http://www.youtube.com with https://www.youtube.com
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.youtube.com|https://www.youtube.com|g' {} \;
echo "- YouTube links updated"

# Replace http://vk.com with https://vk.com
find _posts -name "*.md" -type f -exec sed -i '' 's|http://vk.com|https://vk.com|g' {} \;
echo "- VK links updated"

# Replace http://www.facebook.com with https://www.facebook.com
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.facebook.com|https://www.facebook.com|g' {} \;
echo "- Facebook links updated"

# Replace http://www.slideshare.net with https://www.slideshare.net
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.slideshare.net|https://www.slideshare.net|g' {} \;
echo "- SlideShare links updated"

# Replace http://www.cvk.gov.ua with https://www.cvk.gov.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.cvk.gov.ua|https://www.cvk.gov.ua|g' {} \;
echo "- CVK gov links updated"

# Replace http://president.gov.ua with https://president.gov.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://president.gov.ua|https://president.gov.ua|g' {} \;
echo "- President gov links updated"

# Replace http://russia.mfa.gov.ua with https://russia.mfa.gov.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://russia.mfa.gov.ua|https://russia.mfa.gov.ua|g' {} \;
echo "- MFA gov links updated"

# Replace http://zakon3.rada.gov.ua with https://zakon3.rada.gov.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://zakon3.rada.gov.ua|https://zakon3.rada.gov.ua|g' {} \;
echo "- Rada gov links updated"

# Replace http://brovary-rada.gov.ua with https://brovary-rada.gov.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://brovary-rada.gov.ua|https://brovary-rada.gov.ua|g' {} \;
echo "- Brovary rada links updated"

# Replace http://www.nerc.gov.ua with https://www.nerc.gov.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.nerc.gov.ua|https://www.nerc.gov.ua|g' {} \;
echo "- NERC gov links updated"

# Replace http://www.epravda.com.ua with https://www.epravda.com.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://www.epravda.com.ua|https://www.epravda.com.ua|g' {} \;
echo "- Epravda links updated"

# Replace http://tsn.ua with https://tsn.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://tsn.ua|https://tsn.ua|g' {} \;
echo "- TSN links updated"

# Replace http://forbes.ua with https://forbes.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://forbes.ua|https://forbes.ua|g' {} \;
echo "- Forbes UA links updated"

# Replace http://vstup.info with https://vstup.info
find _posts -name "*.md" -type f -exec sed -i '' 's|http://vstup.info|https://vstup.info|g' {} \;
echo "- Vstup info links updated"

# Replace http://bikeportal.org.ua with https://bikeportal.org.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://bikeportal.org.ua|https://bikeportal.org.ua|g' {} \;
echo "- Bikeportal links updated"

# Replace http://f.img.com.ua with https://f.img.com.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://f.img.com.ua|https://f.img.com.ua|g' {} \;
echo "- Image links updated"

# Replace http://podrobnosti.ua with https://podrobnosti.ua
find _posts -name "*.md" -type f -exec sed -i '' 's|http://podrobnosti.ua|https://podrobnosti.ua|g' {} \;
echo "- Podrobnosti links updated"

# Replace generic http:// with https:// for remaining sites
# This is a bit more dangerous, so we'll do it last
find _posts -name "*.md" -type f -exec grep -l "http://" {} \; | xargs -I{} echo "Still contains HTTP: {}"

echo "Conversion complete!"
echo "Check the list above for any files that still contain 'http://' links that need manual review." 