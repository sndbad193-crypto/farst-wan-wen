## 2025-05-14 - Standardizing Notifications and Fixing Structural Tags
**Learning:** Legacy structural errors, such as using `</nav>` to close `<script>` blocks, can silently break JavaScript functionality. Additionally, malformed ID attributes (e.g., `id="id class"`) prevent reliable DOM selection and CSS styling.
**Action:** Always verify that script blocks are properly closed with `</script>` and that ID and Class attributes are separated. Use accessibility roles like `role="status"` and `aria-live="polite"` for dynamic notifications to ensure they are perceivable by screen readers.
