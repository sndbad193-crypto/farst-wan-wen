## 2025-05-15 - [HUD and Icon Button Accessibility]
**Learning:** Malformed HTML IDs (containing spaces) prevent proper CSS targeting and can be an indicator of intended CSS classes. Additionally, status elements like HUDs require specific ARIA roles to be announced by screen readers during asynchronous updates.
**Action:** Always validate element IDs for syntax errors and ensure all status-conveying elements use `role="status"` and `aria-live="polite"`. Every icon-only button must have a descriptive `aria-label`.
