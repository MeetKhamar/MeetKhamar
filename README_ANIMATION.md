# Animation Reference — CyberSOC Profile Dashboard

> Guidelines for all motion and animation across the project.

---

## Core Principles

1. **Purposeful** — Every animation must communicate information or reinforce visual hierarchy. Never animate merely because animation is possible.
2. **Slow & Elegant** — Movements should feel deliberate, never rushed or jarring.
3. **Professional** — The overall feel should match enterprise security dashboards, not game UIs.
4. **Subtle** — If a user has to focus to notice an animation, it's probably the right amount.
5. **Consistent** — Similar elements should animate identically. Reuse timing values.

---

## Timing Reference

| Token | Duration | Usage |
|---|---|---|
| `fast` | 0.3s | Hover transitions, micro-interactions |
| `normal` | 0.6s | Fade-ins, state changes |
| `slow` | 1.2s | Major reveals, section entries |
| `pulse` | 3s | Breathing effects, status indicators |
| `float` | 6s | Portrait floating, ambient motion |
| `scan` | 8s | Scanner lines, radar sweeps |
| `breathe` | 5s | Scale breathing effects |
| `radar` | 4s | Radar sweep rotation (fast variant) |

---

## Easing Functions

| Name | Value | Usage |
|---|---|---|
| `default` | `cubic-bezier(0.4, 0, 0.2, 1)` | Standard UI transitions |
| `smooth` | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | Floating, breathing motions |
| `bounce` | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` | Reserved — not currently used |

SMIL equivalent: `calcMode="spline"` with `keySplines="0.45 0.05 0.55 0.95"`

---

## Animation Catalog

### Ambient (Always Running)
| Animation | Target | Properties | Duration | Notes |
|---|---|---|---|---|
| Float | Hero portrait | `translateY(0 → -6px)` | 6s loop | Gentle vertical bob |
| Breathe | Hero portrait | `scale(1 → 1.008)` | 5s loop | Barely perceptible |
| Status Pulse | Status dots | `opacity(0.5 → 1)` | 2–3.5s loop | Each indicator has unique timing |
| Radar Sweep | Skills radar line | `rotate(0 → 360°)` | 8s loop | Continuous sweep |
| Center Pulse | Radar center | `r(2 → 4)` | 3s loop | Pulsing dot |
| Diamond Pulse | Section divider | `opacity(0.5 → 1)` | 3s loop | Subtle glow |
| Orbital Ring | Portrait ring | `rotate(0 → 360°)` | 30s loop | Very slow rotation |

### Entrance (Play Once)
| Animation | Target | Properties | Duration | Delay |
|---|---|---|---|---|
| Polygon Reveal | Skills radar fill | `opacity(0 → 1)` | 1.5s | 0.3s |
| Data Point Fade | Radar dots | `opacity(0 → 1)` | 0.5s | 0.5s–1.5s staggered |
| Timeline Card | Timeline milestones | `opacity(0 → 1)` | 0.6s | 0.3s–1.9s staggered |

### Data Flow
| Animation | Target | Properties | Duration | Notes |
|---|---|---|---|---|
| Flow Particles | Pipeline particles | `animateMotion` along path | 4s loop | Multiple particles, staggered starts |
| Dash Stream | Connection lines | `stroke-dashoffset(20 → 0)` | 1.5s loop | Directional flow |
| Alert Pulse | SIEM/Remediate rings | `r(40 → 55)`, `opacity(0.4 → 0)` | 2–3s loop | Expanding, fading ring |

### Special
| Animation | Target | Properties | Duration | Notes |
|---|---|---|---|---|
| Scanner Sweep | Hero visor overlay | `translateY(-30 → 40)` | 8s loop | Horizontal scan band |
| Eye Blink | Hero eye dots | `opacity(0.9 → 0.3)` | 4s loop | Slight offset between eyes |

---

## Implementation Rules

### SVG Animations
- Use **SMIL** (`<animate>`, `<animateTransform>`, `<animateMotion>`) as the primary method
- Use **CSS `@keyframes`** inside `<style>` blocks only when SMIL doesn't support the required effect
- Always include `repeatCount="indefinite"` for ambient animations
- Always include `fill="freeze"` for entrance animations

### GitHub Compatibility
- GitHub renders SVGs as `<img>` tags — SMIL animations **will play** when SVG is referenced directly via URL
- CSS animations inside SVGs work when the SVG is loaded directly but **not** when inlined as base64
- Always reference SVGs via relative URL, never inline

### Performance
- Keep total animation count per SVG under 15
- Avoid animating `filter` properties (expensive)
- Use `will-change` sparingly
- Prefer `transform` and `opacity` over layout-triggering properties

---

## Do's and Don'ts

✅ **Do**: Use slow, elegant timing (3s+ for ambient)  
✅ **Do**: Stagger entrance animations for visual rhythm  
✅ **Do**: Keep floating/breathing barely perceptible  
✅ **Do**: Use consistent easing across all components  

❌ **Don't**: Use animations faster than 0.3s  
❌ **Don't**: Add bouncing, shaking, or jittery motion  
❌ **Don't**: Animate text content  
❌ **Don't**: Create blinking/flashing effects (accessibility)  
❌ **Don't**: Use more than 2 simultaneous transform animations on one element  
