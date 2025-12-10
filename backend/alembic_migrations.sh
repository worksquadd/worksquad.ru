#!/bin/sh
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 \"migration message\""
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Load local env vars if present
if [ -f ".env.local" ]; then
  # shellcheck disable=SC2046
  export $(grep -v '^#' .env.local | xargs)
fi

# Autogenerate a new migration based on the SQLAlchemy models
uv run alembic revision --autogenerate -m "$*"
