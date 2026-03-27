#!/usr/bin/env bash
# install.sh — Install primer-quest (TUI + web mode)
#
# Usage:
#   bash install.sh
#   curl -sSL https://raw.githubusercontent.com/thorski1/primer/main/install.sh | bash

set -e

PACKAGE="primer-quest"

echo ""
echo "  Installing $PACKAGE..."
echo ""

# Prefer uv — fast, handles macOS system Python restrictions automatically
if command -v uv &>/dev/null; then
    echo "  Using uv (recommended)"
    uv tool install "$PACKAGE" --upgrade
    echo ""
    echo "  Done! Commands available:"
    echo "    primer                        # full adventure (terminal)"
    echo "    math-advanced-quest --web     # browser mode → http://localhost:8080"
    echo "    coding-basics-quest --web     # browser mode → http://localhost:8080"
    echo ""

# Fall back to pipx
elif command -v pipx &>/dev/null; then
    echo "  Using pipx"
    pipx install "$PACKAGE" --force
    echo ""
    echo "  Done! Run: math-advanced-quest --web"
    echo ""

# Last resort: pip with --user
elif command -v pip3 &>/dev/null; then
    echo "  Using pip3 --user"
    pip3 install --user --upgrade "$PACKAGE"
    echo ""
    echo "  Done! Run: math-advanced-quest --web"
    echo "  (You may need to add ~/.local/bin to your PATH)"
    echo ""

else
    echo "  ERROR: No package manager found."
    echo "  Install uv first:  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi
