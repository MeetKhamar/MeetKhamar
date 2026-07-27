#!/usr/bin/env python3
"""
CyberSOC Profile Dashboard — Asset Generation Script

Currently validates SVG assets and reports file sizes.
Extensible for future dynamic content generation (CVE feeds, activity widgets, etc.).
"""

import os
import sys
from pathlib import Path

# Repository root
REPO_ROOT = Path(__file__).parent.parent
ASSETS_DIR = REPO_ROOT / "assets" / "svg"
GENERATED_DIR = REPO_ROOT / "generated"

# Expected SVG components
EXPECTED_SVGS = [
    "hero-portrait.svg",
    "mission-briefing.svg",
    "pipeline-flow.svg",
    "section-divider.svg",
    "skills-radar.svg",
    "system-status.svg",
    "terminal-init.svg",
    "timeline.svg",
]

def validate_assets():
    """Validate all expected SVG files exist and report sizes."""
    print("=" * 60)
    print("  CyberSOC Dashboard — Asset Validation")
    print("=" * 60)
    print()

    all_valid = True
    total_size = 0

    for svg_name in EXPECTED_SVGS:
        svg_path = ASSETS_DIR / svg_name
        if svg_path.exists():
            size = svg_path.stat().st_size
            total_size += size
            size_kb = size / 1024
            status = "✅" if size_kb < 10 else "⚠️  (>10KB)"
            print(f"  {status}  {svg_name:<25}  {size_kb:.1f} KB")
        else:
            print(f"  ❌  {svg_name:<25}  MISSING")
            all_valid = False

    print()
    print(f"  Total asset size: {total_size / 1024:.1f} KB")
    print()

    if all_valid:
        print("  ✅  All assets validated successfully.")
    else:
        print("  ❌  Some assets are missing!")
        sys.exit(1)

    print()
    print("=" * 60)


def ensure_generated_dir():
    """Create generated/ directory if it doesn't exist."""
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def main():
    ensure_generated_dir()
    validate_assets()

    # Future: Add dynamic SVG generation here
    # Examples:
    #   - generate_contribution_heatmap()
    #   - generate_cve_feed()
    #   - generate_currently_working_on()


if __name__ == "__main__":
    main()
