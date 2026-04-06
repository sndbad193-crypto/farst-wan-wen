## 2026-04-06 - Structural and Accessibility Foundation
**Learning:** Found critical malformed HTML (id="hy-hud text-sm") and tag mismatch (</nav> for <script>) in mirrored application files. These structural errors can break JS targeting and browser parsing.
**Action:** Always verify the actual DOM IDs and closing tags in legacy HTML files, especially when mirrored, to ensure UX enhancements (like HUD notifications) function correctly.
