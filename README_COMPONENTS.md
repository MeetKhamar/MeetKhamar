# Component Reference — CyberSOC Profile Dashboard

> Inventory and specification for every visual component.

---

## Component Index

| # | Component | File | Dimensions | Status |
|---|---|---|---|---|
| 1 | Hero Portrait | `assets/svg/hero-portrait.svg` | 320 × 380 | ✅ Complete |
| 2 | System Status Bar | `assets/svg/system-status.svg` | 840 × 56 | ✅ Complete |
| 3 | Skills Radar | `assets/svg/skills-radar.svg` | 460 × 460 | ✅ Complete |
| 4 | Pipeline Flow | `assets/svg/pipeline-flow.svg` | 800 × 220 | ✅ Complete |
| 5 | Timeline | `assets/svg/timeline.svg` | 700 × 400 | ✅ Complete |
| 6 | Section Divider | `assets/svg/section-divider.svg` | 800 × 40 | ✅ Complete |

---

## Component Specifications

### 1. Hero Portrait (`hero-portrait.svg`)

**Purpose**: Primary visual identity — a geometric cyber helmet/visor.

**Visual Features**:
- Low-poly geometric helmet with visor, ear pieces, shoulder plates
- Purple gradient visor with glass reflection
- Scanner line sweeping across visor
- Blinking eye dots
- Status LED on forehead (green = operational)
- Subtle circuit-line detailing on helmet surface
- Decorative orbital ring

**Animations** (all SMIL/CSS):
- Float: `translateY(0 → -6px)` over 6s ease
- Breathe: `scale(1 → 1.008)` over 5s ease
- Scanner: vertical sweep across visor, 8s
- Eye blink: opacity 0.9 → 0.3 over 4s
- Status LED: pulse 0.6 → 1 over 2s
- Ear accents: alternating pulse, 3s offset
- Orbital ring: 360° rotation over 30s

**Color Tokens Used**: `brand.purple`, `brand.purpleLight`, `brand.purpleDark`, `bg.secondary`, `bg.tertiary`, `accent.white`, `status.success`

---

### 2. System Status Bar (`system-status.svg`)

**Purpose**: Dashboard-style top bar showing operational metrics.

**Indicators**:
| Label | Value | Color | Pulse Duration |
|---|---|---|---|
| SYSTEM STATUS | OPERATIONAL | `status.success` | 2.5s |
| THREAT LEVEL | NOMINAL | `status.info` | 3s |
| CORE ROLE | SOC ANALYST & AUTOMATION ENGINEER | `brand.purple` | 3.5s |
| UPTIME | 24 × 7 × 365 | `accent.gold` | 2s |

**Layout**: Horizontal bar, 4 sections separated by subtle purple dividers.

---

### 3. Skills Radar (`skills-radar.svg`)

**Purpose**: Hexagonal radar chart showing 6 skill domains.

**Data Points**:
| Axis | Skill | Score | Radius |
|---|---|---|---|
| Top | Blue Team | 90% | 162 |
| Top-Right | Scripting | 85% | 153 |
| Bottom-Right | Cloud Sec | 70% | 126 |
| Bottom | Automation | 95% | 171 |
| Bottom-Left | Threat Hunt | 80% | 144 |
| Top-Left | Incident Resp | 88% | 158.4 |

**Animations**:
- Polygon fade-in: 0 → 1 over 1.5s
- Sweep line: 360° rotation, 8s
- Data points: staggered fade-in (0.5s each, 0.2s offsets)
- Center dot: pulsing radius 2 → 4

---

### 4. Pipeline Flow (`pipeline-flow.svg`)

**Purpose**: Visual representation of SOC automation workflow.

**Flow**: `SIEM Alert → Parser → [Threat Intel → Remediate]` and `[Parser → Notify]`

**Nodes**:
| Node | Icon | Border Color | Description |
|---|---|---|---|
| SIEM Alert | 🚨 | purple | Splunk / Wazuh triggers |
| Parser | 🐍 | purple | Python / Bash processing |
| Threat Intel | 🔍 | gold | VirusTotal / AbuseIPDB |
| Notify | 📨 | blue | Slack / Teams alerts |
| Remediate | 🛡️ | green | Block / Isolate actions |

**Animations**:
- Dashed connection lines: moving dash offset, 1.5s
- Flow particles: travel along bezier paths, 4s with stagger
- Alert pulse ring: expanding radius, fading out

---

### 5. Timeline (`timeline.svg`)

**Purpose**: Career progression milestones.

**Milestones**:
| Year | Title | Side | Dot Color |
|---|---|---|---|
| 2022 | Security Foundations | Left | Purple |
| 2023 | SOC Operations | Right | Gold |
| 2024 | SecOps Automation | Left | Green |
| 2025 | Detection Engineering | Right | Purple |
| NOW | Building the Future | Left | Gold (pulsing) |

**Animations**: Staggered fade-in (0.4s intervals), pulsing "NOW" marker.

---

### 6. Section Divider (`section-divider.svg`)

**Purpose**: Consistent visual separator between README sections.

**Features**:
- Gradient line fading from transparent → purple → transparent
- Center diamond glyph with inner accent
- Side accent dots

**Animations**: Diamond opacity pulse (3s), side dots alternating pulse (4s).

---

## Adding New Components

1. Create SVG in `assets/svg/`
2. Follow the design tokens from `design/tokens.json`
3. Use SMIL animations (no JavaScript)
4. Add specification to this document
5. Update `README_ANIMATION.md` if new animations are introduced
