# Mia VMS — Landing Page Build Brief

## What you're building
A mobile-first, single-page landing page for **Mia VMS** — a veterinary clinic management platform built for independent Indian vets. The page's sole goal is to get vets to **apply for a free 2-week trial**. It will be shared as a WhatsApp link by a pet therapist called Divya to vets she knows. The reader is a vet seeing this cold on their phone.

---

## The product
Mia VMS is a fully working web app (built on FastAPI + Supabase) with 9 modules:
1. **Dashboard** — KPI cards (today's appointments, revenue, total pets/owners), quick-action tiles (Add Pet, New Appointment, Create Invoice, Add Inventory, Add Staff), upcoming appointments panel, recent invoices with Paid/Pending/Overdue status
2. **Pets** — Patient registry with name, species, breed, health status, owner linkage. Search by name, breed, or owner
3. **Owners** — Pet parent directory with name, phone, email, pets count, last visit
4. **Appointments** — Full calendar (Day/Week/Month views), multi-vet colour coding, walk-in quick-add, filter by vet/status/pet/owner
5. **Today's Patients** — Live consultation queue showing scheduled patients, assigned vet, visit reason, "Start Consultation" CTA
6. **Operations** — Clinic KPI dashboard: collection rate, completion rate, inventory health score, appointment outcomes chart, revenue by service, revenue collection bar (Collected/Pending/Overdue), per-vet productivity chart
7. **Billing** — Auto-numbered invoices (INV-YYYY-XXXXXXX) linked to pet and owner, Paid/Pending/Overdue tracking with due dates, one-click status updates
8. **Inventory** — Item, category, quantity, reorder threshold, expiry, auto Ok/Low status alerts
9. **Staff** — Role-based access: Admin, Vet, Staff. Name, email, phone, specialties per member

---

## Audience
- **Primary:** Independent vets and small clinic owners in India (solo to 5 vets)
- **Secondary:** Vet college students and institutions
- **Context:** Reader receives a WhatsApp forward from a colleague/pet therapist. They're busy, on mobile, skeptical. Page must work in under 3 minutes of reading.

---

## Page structure (in order)
1. **Nav** — Logo ("Mia VMS" with a small paw SVG icon), single CTA button "Join trial →"
2. **Hero** — Headline + sub + CTA button + fine print
3. **Scrollable app preview carousel** — 7 horizontally swipeable cards showing each module as a dark-themed mini mockup (no real screenshots, use coded mini UIs). Scroll-snap, dot indicators, mobile-optimised
4. **Vision section** — "What changes with Mia" — 5 cards showing outcomes, NOT pain points
5. **Features list** — 7 features with SVG icons, title, 1-line description
6. **Early access section** — Dark olive background, honest copy about being in development, 5 trial perks, CTA button
7. **How it works** — 4 steps (no timing promises)
8. **Bottom CTA** — Full-width section with headline + button
9. **Footer** — Logo, tagline, links
10. **Sticky bottom bar** — Appears on scroll, dismissable
11. **Modal form** — Bottom-sheet on mobile, centered on desktop

---

## Colour palette (exact hex values)
| Name | Hex | Usage |
|------|-----|-------|
| Sunset | `#EAC891` | Page background |
| Sunset pale | `#F7EDD8` | Card surfaces, form inputs |
| Sunset mid | `#E0B87A` | Dividers, borders |
| Terracotta | `#D06224` | CTA buttons, icon accents |
| Chile Rojo | `#AE431E` | Hover states |
| Terracotta pale | `#FAE8D5` | Icon backgrounds |
| Olive | `#8A8635` | Section labels, dark sections background |
| Olive dark | `#6B6828` | Dark section panels |
| Olive mid | `#A8A452` | Glow accents, checkmarks |
| Olive pale | `#F0EFDA` | Light green tints |
| Warm white | `#FFFDF8` | Cards on beige bg |
| Ink | `#2C1810` | Body text |
| Muted | `#7A5C40` | Secondary text |

---

## Typography
- **Display/headings:** `Fraunces` (Google Font) — serif, italic for emphasis words
- **Body:** `Instrument Sans` (Google Font) — weights 300, 400, 500 only
- **No Inter, Roboto, or system fonts**

---

## Hero copy
**Headline:** "Your clinic, / *finally under control.*" (italic on "finally under control" in terracotta)

**Subheadline:** "Mia is a veterinary management platform built for Indian clinics — appointments, patient records, billing, inventory, and analytics, all in one place. We're looking for 10 early clinics to trial it free for 2 weeks and help us shape the final product."

**CTA:** "Apply for the free trial →"
**Fine print:** "2-week trial · No credit card · No commitment"

---

## Vision section copy
**Section label:** "What changes with Mia"
**Headline:** "This is what an / *efficient clinic looks like.*"
**Intro:** "Every feature in Mia was built around one question: where does a vet lose time, money, or energy — and how do we give it back?"

**5 cards (label / title / description):**
1. **Scheduling** / "A cancellation is a 10-second fix, not a 30-minute reshuffle" / Your full calendar in one view. Move slots, add walk-ins, reassign vets without a single phone call.
2. **Billing** / "Every rupee accounted for — without a separate spreadsheet" / Invoices generated, tracked, and marked Paid, Pending, or Overdue automatically.
3. **Inventory** / "Stock alerts reach you before the problem does" / Set reorder thresholds. Mia flags low vaccines, consumables, and equipment — so you reorder on your terms, not in a panic.
4. **Patient queue** / "Walk into every consult already prepared" / Today's patient list — with assigned vet, breed, and visit reason — ready before your first patient arrives.
5. **Operations** / "Know exactly how your clinic performed — in 60 seconds" / Collection rate, revenue by service, per-vet productivity — one screen, updated in real time.

---

## Early access section copy
**Section label:** "Early access"
**Headline:** "Be one of the first 10 clinics to use Mia."
**Body:** "Mia is in active development. We're looking for a small group of real clinics to trial it, tell us what's missing, and help shape what it becomes. No polish — just a working product and a team that's listening."

**5 perks:**
- Full 2-week trial — every module, no restrictions
- We onboard your clinic personally and stay available throughout
- Your feedback goes directly into the product roadmap
- Early testers receive founding-member pricing when we launch
- Completely free. No credit card. No obligation.

---

## Form (modal)
**Anonymous — no name fields.** Collect only:
- Email or WhatsApp number (required)
- Clinic name & city
- Clinic size (dropdown: Solo vet / 2–3 vets / 4–6 vets / 7+ vets / Vet college)
- What's your biggest clinic headache right now? (textarea, optional)

**On submit:** Open `https://wa.me/14132752191` with a pre-filled message containing the form data. Show success screen.

---

## Design rules
- **Mobile-first.** Max content width 600px, centred. Everything readable at 375px.
- **No emojis anywhere.** Use Lucide-style SVG icons only.
- **No fake testimonials.** This is a first trial — no social proof invented.
- **No pricing.** Product is not priced yet.
- **No promises about speed of setup** (e.g. "live in a day" — remove this).
- **Sticky bottom bar** — appears after 400px scroll, shows "Join the 2-week trial / Help shape Mia before launch" with a button. Dismissable.
- **Scrollable app carousel** — dark olive/forest background, horizontal scroll-snap, 7 mini app mockups coded in HTML/CSS, dot indicators
- **Scroll reveal animations** on all sections
- **Bottom-sheet modal** on mobile (slides up from bottom), centered dialog on desktop

---

## What NOT to include
- Pricing section
- Testimonials / reviews (none exist yet)
- "Forwarded by a colleague" badge
- "Live in a day" or any specific time promise for setup
- Name or phone number fields in the form
- Any emojis
- Cost/affordability messaging

---

## Tech
- Single self-contained `.html` file
- Google Fonts via CDN
- No external JS libraries
- Vanilla CSS and JS only
- WhatsApp deep link for form submission: `wa.me/14132752191`
