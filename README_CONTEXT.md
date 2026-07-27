# Context & Decisions — CyberSOC Profile Dashboard

> Project context, design rationale, and changelog.

---

## Project Overview

**CyberSOC Profile Dashboard** is a next-generation GitHub Profile README for Meet Khamar. It's designed to feel like navigating a premium Security Operations Center dashboard, not scrolling a Markdown document.

### Key Constraints
- **No JavaScript** — GitHub READMEs don't execute JS
- **SVG + Markdown + HTML** — The only rendering technologies available
- **SMIL animations** — Primary animation method (works in SVG `<img>` tags)
- **Static assets** — All SVGs are pre-built; dynamic content via GitHub Actions

### Design Identity
- Inspired by enterprise SOC platforms (CrowdStrike, SentinelOne, Splunk) merged with premium product design (Vercel, Linear, Stripe)
- Purple is the brand color; gold is the premium accent
- Minimal, purposeful, zero clutter

---

## Architecture Decisions

### ADR-001: SVG Over HTML/CSS for Components
**Decision**: Build all visual components as standalone SVG files rather than inline HTML/CSS.

**Rationale**: GitHub sanitizes inline styles aggressively. SVGs referenced via `<img>` tags render with full CSS and SMIL animation support, giving us far more visual capability.

**Trade-off**: SVGs can't be interactive (no click handlers), but this is acceptable for a profile README.

### ADR-002: SMIL Over CSS Animations
**Decision**: Prefer SMIL (`<animate>`, `<animateTransform>`) over CSS `@keyframes`.

**Rationale**: SMIL is more reliably rendered across GitHub's SVG pipeline. CSS animations work but can be stripped in certain contexts.

### ADR-003: Modular File Architecture
**Decision**: Separate documentation into 8 README_*.md files.

**Rationale**: This creates a "permanent memory" for the project. Any future edits consult these files first, preventing design drift and maintaining visual consistency.

### ADR-004: External SVG References
**Decision**: Never inline SVGs into README.md. Always reference via `<img src="...">`.

**Rationale**: Inline SVGs are heavily sanitized by GitHub. External references preserve all styling and animation.

---

## Changelog

### v1.0.0 (2025)
- Initial release
- 6 SVG components: hero portrait, system status, skills radar, pipeline flow, timeline, section divider
- Complete design system with tokens
- Full documentation suite (8 files)
- GitHub Action for dynamic stat updates
- Premium README with SOC dashboard aesthetic
