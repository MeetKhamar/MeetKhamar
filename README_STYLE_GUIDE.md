# Style Guide — CyberSOC Profile Dashboard

> Visual rules, conventions, and quality standards.

---

## Visual Identity

The profile communicates: **"This person builds enterprise-grade security systems."**

We draw inspiration from:
- Microsoft Security, CrowdStrike Falcon, SentinelOne (SOC dashboards)
- Vercel, Linear, Stripe (premium product design)
- Arc Browser, Raycast, Figma, Framer (modern UI elegance)

We combine these into a unique identity that feels like a **premium cybersecurity product interface** rendered through GitHub.

---

## Do's

- ✅ Use the design tokens consistently — never hardcode ad-hoc values
- ✅ Maintain strong visual hierarchy: Hero → Status → Content → Footer
- ✅ Use purple as the primary accent in every component
- ✅ Keep animations slow and intentional (3s+ for ambient)
- ✅ Maintain generous whitespace between sections
- ✅ Use the section divider SVG between every major section
- ✅ Include meaningful alt text for all embedded images
- ✅ Ensure high contrast ratios (WCAG AA minimum)
- ✅ Test rendering on both light and dark GitHub themes
- ✅ Keep SVGs under 5KB each (except hero portrait)

---

## Don'ts

- ❌ No Matrix rain, no hacker skulls, no "Elite Hacker" aesthetics
- ❌ No excessive neon or saturated green-on-black terminal effects
- ❌ No JavaScript — GitHub doesn't execute it
- ❌ No inline base64 SVGs — always reference via relative URL
- ❌ No pure black (`#000`) or pure white (`#FFF`)
- ❌ No futuristic unreadable fonts
- ❌ No bouncing, shaking, or jarring animations
- ❌ No random decorative elements without purpose
- ❌ No more than 2 gold accents per section
- ❌ No placeholder images — every asset must be final quality

---

## Badge Styling

Use `for-the-badge` style consistently for all technology badges:

```
https://img.shields.io/badge/LABEL-COLOR?style=for-the-badge&logo=LOGO&logoColor=white
```

Group badges by category. Add `<br/>` between rows. Maximum 3 badges per row.

---

## Section Structure

Every major section follows this pattern:

```
1. Section divider SVG
2. Section header (## with emoji)
3. Optional subheading or quote
4. Content (table, SVG, badges, text)
5. Spacing (---) before next section
```

---

## Emoji Usage

Use emojis sparingly and consistently:

| Emoji | Usage |
|---|---|
| ⚡ | whoami / identity |
| 🛡️ | Defense, protection |
| ⚔️ | Offense, threat hunting |
| 🐍 | Python, scripting |
| 📈 | Statistics, metrics |
| 📡 | Contact, communication |
| 🔬 | Research, analysis |
| ⚙️ | Automation, pipelines |
| 🕐 | Timeline, history |

No more than 1 emoji per heading. Never use emojis in body text.

---

## Naming Conventions

| Type | Convention | Example |
|---|---|---|
| SVG files | `kebab-case.svg` | `hero-portrait.svg` |
| Documentation | `README_SCREAMING_SNAKE.md` | `README_DESIGN_SYSTEM.md` |
| Design tokens | `camelCase` | `brand.purpleLight` |
| CSS classes | `kebab-case` | `.radar-label` |
| Gradient IDs | `camelCase` | `visorGrad` |
| Filter IDs | `camelCase` | `purpleGlow` |
