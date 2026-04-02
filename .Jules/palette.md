## 2025-05-14 - Confirmation Dialogs for Destructive Actions
**Learning:** Destructive actions, such as record deletion, should always be gated by a confirmation dialog to prevent accidental data loss. In RTL (Arabic) contexts, ensuring the message is also in Arabic is crucial for accessibility.
**Action:** Always implement `confirm()` or a custom modal for delete buttons, and verify `aria-label` is present for icon-only buttons.
