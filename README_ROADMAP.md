# Roadmap — CyberSOC Profile Dashboard

> Planned features and expansion modules.

---

## Status Legend

| Icon | Status |
|---|---|
| ✅ | Complete |
| 🔄 | In Progress |
| 📋 | Planned |
| 💡 | Idea / Under Consideration |

---

## V1.0 — Core Dashboard ✅

- ✅ Repository architecture (modular, scalable)
- ✅ Design system (tokens, documentation)
- ✅ Hero portrait SVG (cyber helmet)
- ✅ System status bar SVG
- ✅ Skills radar SVG
- ✅ Pipeline flow SVG
- ✅ Timeline SVG
- ✅ Section divider SVG
- ✅ Complete README.md
- ✅ 8 documentation files
- ✅ GitHub Action for auto-updates

---

## V1.1 — Polish & Enhancement 📋

- 📋 Optimized SVG file sizes (SVGO pass)
- 📋 Additional badge variants for new tools
- 📋 Light theme compatibility audit
- 📋 Accessibility audit (contrast ratios, alt text)
- 📋 Contribution activity heatmap SVG

---

## V2.0 — Dynamic Intelligence 📋

- 📋 Live CVE highlights (generated via Action)
- 📋 Recent blog/research feed widget
- 📋 Certification timeline with verification links
- 📋 Achievement gallery (hackathons, CTFs)
- 📋 Dynamic "Currently Working On" widget

---

## V3.0 — Interactive Experience 💡

- 💡 Security blog integration
- 💡 Threat intelligence feed visualization
- 💡 Interactive project architecture diagrams
- 💡 Open-source release showcase
- 💡 Live SOC telemetry simulation

---

## Module Architecture

New modules must:
1. Inherit the existing design system automatically
2. Be created as standalone SVG components
3. Follow animation guidelines from `README_ANIMATION.md`
4. Be documented in `README_COMPONENTS.md`
5. Be generated via scripts if dynamic

No module should require redesigning existing components.
