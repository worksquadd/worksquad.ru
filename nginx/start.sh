#!/bin/sh
set -e

TARGET="/usr/share/nginx/html/index.html"
echo "Nginx startup: waiting for $TARGET to appear..."

# Wait up to ~60s for the frontend-build to populate the volume.
for i in $(seq 1 60); do
  if [ -f "$TARGET" ]; then
    echo "Found $TARGET"
    break
  fi
  sleep 1
done

exec nginx -g 'daemon off;'
