## 2025-05-15 - Deletion Safeguards and Accessibility
**Learning:** Destructive actions without confirmation and feedback lead to user anxiety and potential data loss. Malformed HTML attributes (like IDs mixed with classes) break functional DOM selection for status feedback systems.
**Action:** Always gate deletions with `confirm()`, provide immediate success feedback via toast/HUD, and ensure icon-only buttons have descriptive `aria-label` attributes in the target language.
