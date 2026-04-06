## 2024-05-15 - [Structural Fix in Legacy HTML]
**Learning:** In legacy HTML files with mixed content, search-and-replace for closing tags like `</nav>` or `</script>` can lead to regressions if the same tag is used multiple times (e.g., once for navigation and once as a malformed closing tag for a script).
**Action:** Always verify the context of a tag before replacing it, especially when fixing malformed structures in SPAs. Use line numbers or unique surrounding content for targeted `sed` or `replace_with_git_merge_diff` operations.
