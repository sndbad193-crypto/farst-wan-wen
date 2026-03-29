## 2026-03-29 - [Consistency in Destructive Actions]
**Learning:** In highly technical or administrative interfaces like the 'Diwan Al-Hayyani' platform, users value security and prevention of accidental data loss. Destructive actions like deleting a registry record should always be preceded by a confirmation dialog to maintain trust.
**Action:** Always implement `confirm()` or a custom modal for destructive actions, and ensure buttons for these actions have descriptive ARIA labels in the user's language.
