# Design System — CyberSOC Profile Dashboard

> Single source of truth for all visual decisions across the project.

---

## Color Palette

| Token | Hex | Usage |
|---|---|---|
| `bg.primary` | `#0D1117` | Page background, SVG backgrounds |
| `bg.secondary` | `#161B22` | Card backgrounds, elevated surfaces |
| `bg.tertiary` | `#1C2333` | Hover states, active surfaces |
| `bg.card` | `#13171F` | Widget card fills |
| `brand.purple` | `#8B5CF6` | Primary brand color — borders, accents, links |
| `brand.purpleLight` | `#A78BFA` | Highlights, hover states, secondary elements |
| `brand.purpleDark` | `#7C3AED` | Depth, shadows, gradient endpoints |
| `brand.purpleMuted` | `#6D28D9` | Subtle accents |
| `accent.gold` | `#F59E0B` | Premium details, key highlights, "NOW" markers |
| `accent.goldLight` | `#FBBF24` | Gold hover states |
| `accent.white` | `#F1F5F9` | Primary text, headings |
| `accent.slate` | `#94A3B8` | Body text, descriptions |
| `accent.slateDark` | `#64748B` | Muted labels, captions |
| `accent.slateLight` | `#CBD5E1` | Secondary text |
| `status.success` | `#10B981` | Operational, success indicators |
| `status.warning` | `#F59E0B` | Warning, caution states |
| `status.critical` | `#EF4444` | Alert, critical, malicious |
| `status.info` | `#3B82F6` | Information, nominal states |

### Color Rules

- **Purple is the identity.** It appears in every component as the primary accent.
- **Gold is premium.** Used sparingly — only for "now" markers, key highlights, top-performing skills. Never overuse.
- **Status colors follow security conventions.** Green = safe, amber = warning, red = critical, blue = informational.
- **Never use pure black** (`#000`) — always use `#0D1117` or darker variants.
- **Never use pure white** (`#FFF`) — always use `#F1F5F9` or muted whites.

---

## Typography

| Level | Size | Weight | Color | Usage |
|---|---|---|---|---|
| Hero | 28px | 700 | `#F1F5F9` | Main profile title |
| H1 | 22px | 700 | `#F1F5F9` | Section headers |
| H2 | 18px | 600 | `#F1F5F9` | Sub-section headers |
| H3 | 15px | 600 | `#CBD5E1` | Widget titles |
| Body | 13px | 400 | `#94A3B8` | Descriptions |
| Caption | 11px | 500 | `#64748B` | Labels, status text |
| Micro | 9px | 500 | `#64748B` | Tags, metadata |

### Font Stack

```
Primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
Mono:    'SF Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace
```

---

## Spacing

Base unit: **4px**

| Token | Value | Usage |
|---|---|---|
| `xs` | 4px | Tight inner spacing |
| `sm` | 8px | Badge gaps, icon margins |
| `md` | 16px | Card padding, element gaps |
| `lg` | 24px | Section sub-spacing |
| `xl` | 32px | Major element gaps |
| `xxl` | 48px | Section separator spacing |
| `section` | 64px | Between major sections |

---

## Border Radius

| Token | Value | Usage |
|---|---|---|
| `sm` | 6px | Small badges, tags |
| `md` | 10px | Cards, panels |
| `lg` | 16px | Large containers |
| `xl` | 24px | Hero sections |
| `pill` | 999px | Status pills |

---

## Effects

### Glow
- Purple glow: `0 0 20px rgba(139, 92, 246, 0.25)`
- Gold glow: `0 0 12px rgba(245, 158, 11, 0.2)`
- Success glow: `0 0 10px rgba(16, 185, 129, 0.3)`

### Glass
- Background: `rgba(13, 17, 23, 0.7)`
- Blur: `12px`
- Border: `1px solid rgba(139, 92, 246, 0.12)`

### Shadows
- Small: `0 2px 8px rgba(0, 0, 0, 0.3)`
- Medium: `0 4px 16px rgba(0, 0, 0, 0.4)`
- Large: `0 8px 32px rgba(0, 0, 0, 0.5)`

---

## Machine-Readable Tokens

Full token definitions: [`design/tokens.json`](design/tokens.json)
