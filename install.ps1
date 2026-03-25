# The Young Lady's Illustrated Primer — Windows Installer
# Run from PowerShell with:
#   powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/thorski1/primer/main/install.ps1 | iex"

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "  The Young Lady's Illustrated Primer" -ForegroundColor Cyan
Write-Host "  =====================================" -ForegroundColor Cyan
Write-Host ""

# ── Find Python 3.10+ ──────────────────────────────────────────────────────────
$pythonCmd = $null
foreach ($cmd in @("python", "py", "python3")) {
    try {
        $ver = & $cmd --version 2>&1
        if ($ver -match "Python (\d+)\.(\d+)") {
            $major = [int]$Matches[1]
            $minor = [int]$Matches[2]
            if ($major -gt 3 -or ($major -eq 3 -and $minor -ge 10)) {
                $pythonCmd = $cmd
                Write-Host "  OK  Python $major.$minor (via '$cmd')" -ForegroundColor Green
                break
            } else {
                Write-Host "  WARN  Found Python $major.$minor via '$cmd' — need 3.10+" -ForegroundColor Yellow
            }
        }
    } catch { }
}

if (-not $pythonCmd) {
    Write-Host ""
    Write-Host "  ERROR: Python 3.10+ not found." -ForegroundColor Red
    Write-Host "  Download from: https://python.org/downloads" -ForegroundColor Red
    Write-Host "  During install, check 'Add Python to PATH'" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

# ── Install via pip ────────────────────────────────────────────────────────────
Write-Host "  Installing primer..." -ForegroundColor White
& $pythonCmd -m pip install --user --quiet primer
Write-Host "  OK  Installed!" -ForegroundColor Green

# ── Ensure Scripts directory is in PATH ───────────────────────────────────────
$scriptsDir = & $pythonCmd -c "import sysconfig; print(sysconfig.get_path('scripts'))"
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($userPath -notlike "*$scriptsDir*") {
    $newPath = if ($userPath) { "$userPath;$scriptsDir" } else { $scriptsDir }
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "  OK  Added Python Scripts to PATH" -ForegroundColor Green
    Write-Host "  NOTE: Open a new terminal window for PATH to take effect" -ForegroundColor Yellow
} else {
    Write-Host "  OK  Scripts directory already in PATH" -ForegroundColor Green
}

# ── Done ───────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "  Open a NEW terminal window, then run:" -ForegroundColor White
Write-Host "    primer" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Standalone chapters:" -ForegroundColor White
Write-Host "    letters-quest        The Letter Garden" -ForegroundColor DarkCyan
Write-Host "    numbers-quest        The Counting Kingdom" -ForegroundColor DarkCyan
Write-Host "    science-quest        The World of Wondering" -ForegroundColor DarkCyan
Write-Host "    kindness-quest       The Art of Being Kind" -ForegroundColor DarkCyan
Write-Host "    geography-quest      The Atlas of Wonders" -ForegroundColor DarkCyan
Write-Host "    math-advanced-quest  The Math Academy" -ForegroundColor DarkCyan
Write-Host "    history-quest        The Time Traveler's Primer" -ForegroundColor DarkCyan
Write-Host "    art-quest            The Art Studio" -ForegroundColor DarkCyan
Write-Host "    coding-basics-quest  The Code Garden" -ForegroundColor DarkCyan
Write-Host ""
Write-Host "  TIP: Use Windows Terminal for best display." -ForegroundColor Yellow
Write-Host "  Updates install automatically when you run the game." -ForegroundColor Yellow
Write-Host ""
