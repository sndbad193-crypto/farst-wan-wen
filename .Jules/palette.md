## 2026-04-08 - Standardizing Accessibility and Notifications
**Learning:** Dynamic UI rendering often misses accessibility attributes like `aria-label` for icon-only buttons, and malformed container IDs can break notification systems (HUD).
**Action:** Always verify `aria-label` in template strings and ensure notification containers have distinct ID and Class attributes with appropriate ARIA roles (`role="status"`, `aria-live="polite"`).
