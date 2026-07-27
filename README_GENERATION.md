# Generation Pipeline — CyberSOC Profile Dashboard

> How dynamic assets are created and maintained.

---

## Overview

The profile uses a combination of:
1. **Static SVGs** — Hand-crafted, committed to repo (hero, radar, pipeline, timeline, divider)
2. **External APIs** — GitHub stats cards from third-party services
3. **GitHub Actions** — Automated regeneration of dynamic content

---

## External Services

### GitHub Stats Cards
| Service | URL Pattern | Theme |
|---|---|---|
| Stats | `github-readme-stats-fast.vercel.app/api?username=MeetKhamar` | Custom (tokyonight base) |
| Top Languages | `github-readme-stats-fast.vercel.app/api/top-langs/?username=MeetKhamar` | Custom |
| Streak | `github-readme-streak-stats.herokuapp.com/?user=MeetKhamar` | Custom |
| Activity Graph | `github-readme-activity-graph.vercel.app/graph?username=MeetKhamar` | Custom |

### Capsule Render
| Service | Usage |
|---|---|
| `capsule-render.vercel.app` | Header banner generation |

---

## GitHub Action: `update-readme.yml`

**Trigger**: Daily schedule (midnight UTC) + on push to main

**Steps**:
1. Checkout repository
2. Run `scripts/generate-stats.py` to update any generated SVGs
3. Commit and push if changes exist

**Configuration**: `.github/workflows/update-readme.yml`

---

## Generation Script: `generate-stats.py`

**Purpose**: Placeholder script for future dynamic SVG generation.

**Current capabilities**:
- Validates all SVG files exist
- Reports file sizes
- Extensible for future dynamic content generation

**Future capabilities**:
- Generate contribution heatmap SVG
- Fetch and render recent CVEs
- Update "Currently Working On" widget
- Generate blog feed widget

---

## Asset Pipeline

```
Static SVGs (hand-crafted)     → Committed to assets/svg/
External API images            → Referenced via URL in README.md
Generated SVGs (future)        → Output to generated/ directory
GitHub Action                  → Orchestrates generation + commit
```

---

## Adding Dynamic Content

1. Add generation logic to `scripts/generate-stats.py`
2. Output SVG to `generated/` directory
3. Reference in README.md via `<img src="generated/...">`
4. Update GitHub Action if new triggers are needed
5. Document in this file
