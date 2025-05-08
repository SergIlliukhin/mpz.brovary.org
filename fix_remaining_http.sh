#!/bin/bash

# Script to replace remaining common HTTP links with HTTPS in Markdown files
echo "Starting conversion of remaining HTTP links to HTTPS in Markdown files..."

# Common domains to replace
domains=(
  "www.google.com/calendar"
  "revisor.org.ua"
  "brovary.org.ua"
  "mpz.brovary.org"
  "unian.ua"
  "unian.net"
  "ukranews.com"
  "pravda.com.ua"
  "ukrainska.pravda.com.ua"
  "zn.ua"
  "ictv.ua"
  "ua-reporter.com"
  "obozrevatel.com"
  "korrespondent.net"
  "segodnya.ua"
  "liga.net"
  "liga.ua"
  "inshe.tv"
  "comments.ua"
  "gazeta.ua"
  "novyny.live"
  "nv.ua"
  "online.ua"
  "tyzhden.ua"
  "dt.ua"
  "focus.ua"
  "bbc.com"
  "radiosvoboda.org"
  "interfax.com.ua"
  "interfax.ua"
  "rbc.ua"
  "espreso.tv"
  "fakty.ua"
  "fakty.com.ua"
  "lb.ua"
  "glavcom.ua"
  "censor.net"
  "censor.net.ua"
  "unn.com.ua"
  "kp.ua"
  "1plus1.ua"
  "ictv.ua"
  "inter.ua"
  "5.ua"
  "stb.ua"
  "youtube.com"
  "facebook.com"
  "twitter.com"
  "instagram.com"
  "google.com"
  "ukr.net"
  "i.ua"
  "gov.ua"
  "rada.gov.ua"
  "president.gov.ua"
  "kmu.gov.ua"
  "mfa.gov.ua"
  "moz.gov.ua"
  "mon.gov.ua"
  "minagro.gov.ua"
  "me.gov.ua"
  "minjust.gov.ua"
  "mvs.gov.ua"
  "mil.gov.ua"
  "forbes.ua"
  "liga.net"
)

# Replace each domain
for domain in "${domains[@]}"; do
  echo "Replacing http://$domain with https://$domain"
  find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' "s|http://$domain|https://$domain|g" {} \;
done

# Replace general Facebook links
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' "s|http://www.facebook.com|https://www.facebook.com|g" {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' "s|http://facebook.com|https://facebook.com|g" {} \;

# Replace YouTube iframes and links
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' "s|<iframe[^>]*src=\"http://|<iframe src=\"https://|g" {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' "s|http://youtube.com|https://youtube.com|g" {} \;
find . -name "*.md" -type f -not -path "*/\.*" -exec sed -i '' "s|http://www.youtube.com|https://www.youtube.com|g" {} \;

echo "Checking for remaining HTTP links in Markdown files..."
find . -name "*.md" -type f -not -path "*/\.*" -exec grep -l "http://" {} \; | xargs -I{} echo "Still contains HTTP: {}"

echo "Conversion complete!"
echo "The above list shows files that still contain 'http://' links that might need manual review." 