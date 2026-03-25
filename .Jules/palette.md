## 2025-03-24 - [Accessibility & UX Improvements for HUD and Deletion]
**Learning:** Status notifications (like a HUD) must use `aria-live` regions to be accessible to screen reader users. Destructive actions like deleting a record should always have a confirmation step to prevent accidental data loss and improve user confidence.
**Action:** Always wrap status messages in elements with `role="status"` and `aria-live="polite"`, and implement `confirm()` for delete actions.
