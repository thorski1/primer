#!/usr/bin/env bash
# The Young Lady's Illustrated Primer — Installer
# Usage: curl -sSL https://raw.githubusercontent.com/thorski1/primer/main/install.sh | bash

set -e

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${CYAN}    *  .  .    *  . * .    *  .    *  .  .  *  .${NC}"
echo ""
echo -e "${CYAN}____________ ________  ___ ___________${NC}"
echo -e "${CYAN}| ___ \\ ___ \\_   _|  \\/  ||  ___| ___ \\${NC}"
echo -e "${CYAN}| |_/ / |_/ / | | | .  . || |__ | |_/ /${NC}"
echo -e "${CYAN}|  __/|    /  | | | |\\/| ||  __||    /${NC}"
echo -e "${CYAN}| |   | |\\ \\ _| |_| |  | || |___| |\\ \\${NC}"
echo -e "${CYAN}\\_|   \\_| \\_|\\___/\\_|  |_/\\____/\\_| \\_|${NC}"
echo ""
echo -e "${CYAN}    *  .  .    *  . * .    *  .    *  .  .  *  .${NC}"
echo ""
echo -e "  ${CYAN}The Primer — Installer${NC}"
echo ""

# ── Detect Python 3.10+ ───────────────────────────────────────────────────────
PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VER=$("$cmd" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "0.0")
        MAJ=$(echo "$VER" | cut -d. -f1)
        MIN=$(echo "$VER" | cut -d. -f2)
        if [ "$MAJ" -gt 3 ] || { [ "$MAJ" -eq 3 ] && [ "$MIN" -ge 10 ]; }; then
            PYTHON="$cmd"
            echo -e "  ${GREEN}OK${NC}  Python $VER"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo -e "  ${RED}ERROR:${NC} Python 3.10+ not found."
    echo "  Download from: https://python.org/downloads"
    exit 1
fi

# ── Install via pipx (preferred) or pip ───────────────────────────────────────
if command -v pipx &>/dev/null; then
    echo "  Installing with pipx..."
    pipx install primer 2>/dev/null || pipx upgrade primer
    echo -e "  ${GREEN}OK${NC}  Installed!"
else
    echo "  Installing with pip..."
    "$PYTHON" -m pip install --user --quiet primer
    echo -e "  ${GREEN}OK${NC}  Installed!"

    # Warn if ~/.local/bin is not in PATH
    LOCAL_BIN="$HOME/.local/bin"
    if [[ ":$PATH:" != *":$LOCAL_BIN:"* ]]; then
        PROFILE="~/.zshrc"
        [[ "$SHELL" == *"bash"* ]] && PROFILE="~/.bash_profile"
        echo ""
        echo -e "  ${YELLOW}NOTE:${NC} Run this to add pip's bin directory to your PATH:"
        echo -e "  ${CYAN}echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> $PROFILE && source $PROFILE${NC}"
    fi
fi

# ── Done ───────────────────────────────────────────────────────────────────────
echo ""
echo -e "  ${GREEN}Installation complete!${NC}"
echo ""
echo -e "  Run the full adventure:  ${CYAN}primer${NC}"
echo ""
echo "  Standalone chapters:"
echo -e "    ${CYAN}letters-quest${NC}        The Letter Garden"
echo -e "    ${CYAN}numbers-quest${NC}        The Counting Kingdom"
echo -e "    ${CYAN}science-quest${NC}        The World of Wondering"
echo -e "    ${CYAN}kindness-quest${NC}       The Art of Being Kind"
echo -e "    ${CYAN}geography-quest${NC}      The Atlas of Wonders"
echo -e "    ${CYAN}math-advanced-quest${NC}  The Math Academy"
echo -e "    ${CYAN}history-quest${NC}        The Time Traveler's Primer"
echo -e "    ${CYAN}art-quest${NC}            The Art Studio"
echo -e "    ${CYAN}coding-basics-quest${NC}  The Code Garden"
echo ""
echo -e "  Updates install automatically when you run the game."
echo ""
