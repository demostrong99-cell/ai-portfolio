# Personal Website — Zeng

A modern, responsive personal website showcasing my professional background as a Project Coordinator and Operations Specialist with 10 years of experience in logistics.

**[Live Demo](https://your-domain.com)** · **[View Resume](https://your-domain.com/resume.html)**

## Features

- **Responsive Design** — Mobile-first layout that adapts seamlessly to phones, tablets, and desktops
- **Dark Mode** — Toggle between light and dark themes with system preference detection and localStorage persistence
- **WCAG 2.1 AA Compliant** — Skip navigation, focus-visible outlines, reduced-motion support, proper ARIA attributes, screen reader friendly
- **Contact Form** — Client-side validated form with live error feedback and success state
- **SEO Optimized** — Open Graph, Twitter Card, meta descriptions, semantic HTML, and canonical-ready structure
- **Printable Resume** — Clean HTML resume page optimized for `Cmd/Ctrl + P` to save as PDF
- **Scroll Animations** — Fade-in content reveals using IntersectionObserver (respects `prefers-reduced-motion`)
- **Zero Dependencies** — Pure HTML, CSS, and JavaScript. No frameworks, no build tools, no npm install

## Technologies

| Layer | Technology |
|-------|-----------|
| **Markup** | HTML5 (semantic elements, ARIA landmarks) |
| **Styling** | CSS3 (custom properties, grid, flexbox, clamp(), backdrop-filter) |
| **Scripting** | Vanilla ES6+ JavaScript (IntersectionObserver, localStorage, form validation) |
| **Typography** | [Inter](https://rsms.me/inter/) via Google Fonts (400–700 weights) |
| **Favicon** | Inline SVG (zero HTTP requests) |

## Installation

No build step required. Clone and open:

```bash
git clone https://github.com/your-username/personal-website.git
cd personal-website
```

**Option A** — Open directly:
```bash
open index.html
```

**Option B** — Local server:
```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

**Option C** — Any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages):
Just point it at the repository root.

## Project Structure

```
personal-website/
├── index.html      # Single-page website (all sections)
├── style.css       # Styles, dark mode, responsive breakpoints
├── script.js       # Theme toggle, nav, animations, form validation
├── resume.html     # Standalone printable resume
├── .gitignore
└── README.md
```

## Usage

### Customization

**Update personal info** — Edit `index.html`:
- Name, title, and bio in the Hero and About sections
- Contact links (email, LinkedIn) in the Contact section
- Skills and experience details

**Update colors** — Edit CSS variables in `style.css`:
```css
:root {
  --primary: #2563eb;     /* Main accent color */
  --accent: #0891b2;      /* Secondary accent */
  --bg: #ffffff;          /* Background */
  --text: #1e293b;        /* Body text */
  --text-light: #4b5e78;  /* Muted text */
}
```

**Update resume** — Edit `resume.html` with your education, experience, and contact details.

### Dark Mode

The site automatically detects the user's system preference (`prefers-color-scheme`). Users can override with the 🌙/☀️ toggle, and their choice persists via `localStorage`.

### Contact Form

The form currently uses client-side validation with simulated submission. To make it functional, replace the `setTimeout` in `script.js` with a real backend:

- **Formspree** — `<form action="https://formspree.io/f/your-id" method="POST">`
- **Netlify Forms** — Add `netlify` attribute to the `<form>` tag
- **EmailJS** — Client-side email sending via their SDK
- **Custom API** — Replace the submit handler with a `fetch()` call

## Accessibility

Built to meet WCAG 2.1 Level AA:

| Feature | Status |
|---------|--------|
| Skip-to-content link | ✅ |
| Semantic landmarks (`<main>`, `<nav>`, `<header>`, `<footer>`) | ✅ |
| `aria-label`, `aria-expanded`, `aria-controls` on interactive elements | ✅ |
| `aria-invalid`, `aria-describedby`, `aria-live` on form fields | ✅ |
| `:focus-visible` outlines on all interactive elements | ✅ |
| `prefers-reduced-motion` disables all animations | ✅ |
| Color contrast ≥ 4.5:1 for normal text, ≥ 3:1 for large text | ✅ |
| 44px minimum touch targets on mobile | ✅ |
| Screen reader text for required fields and decorative icons | ✅ |

## Browser Support

| Browser | Version |
|---------|---------|
| Chrome | 80+ |
| Firefox | 80+ |
| Safari | 14+ |
| Edge | 80+ |
| Mobile Safari | 14+ |
| Chrome Android | 80+ |

> Uses `backdrop-filter`, CSS Grid, `clamp()`, and `IntersectionObserver`. Older browsers get graceful fallbacks (no blur, fixed sizes, no animations).

## Future Improvements

- [ ] Replace emoji icons with SVGs for consistent cross-platform rendering
- [ ] Add `<meta name="theme-color">` for mobile browser chrome
- [ ] Implement real form submission (Formspree or Netlify Forms)
- [ ] Add honeypot field for spam prevention
- [ ] Optimize font loading with `font-display: swap` preload strategy
- [ ] Add structured data (JSON-LD) for rich search results
- [ ] Create an OG image for social sharing
- [ ] Add a custom 404 page
- [ ] Generate a `manifest.json` for PWA support
- [ ] Add a blog/portfolio section

## License

This project is open source and available under the [MIT License](LICENSE).

---

Built by Zeng — Project Coordinator & Operations Specialist.
