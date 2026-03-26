import os
import time
from playwright.sync_api import sync_playwright, expect

def verify_new_features():
    with sync_playwright() as p:
        # 1. Start Browser
        browser = p.chromium.launch(headless=True)
        # Record video with large viewport
        context = browser.new_context(
            record_video_dir="/home/jules/verification/video",
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()

        # 2. Load the page (static file)
        path = os.path.abspath("index.html")
        page.goto(f"file://{path}")
        page.wait_for_timeout(1000)

        # 3. Handle Portal
        page.fill("#auth-email", "test@hayyani.com")
        page.wait_for_timeout(500)
        page.click("button:has-text('بوابة الدخول')")

        # Wait for portal to disappear
        page.wait_for_selector("#neon-portal", state="hidden")
        page.wait_for_timeout(1000)

        # Handle Welcome Gift
        if page.is_visible("#gift-box"):
            page.click("button:has-text('استلام الهدية')")
            page.wait_for_timeout(1000)

        # 4. Open 3D Tree via Header Button
        page.click("header button[onclick='toggleAdmin()']")
        page.wait_for_timeout(500)
        page.click("#adminPanel button:has-text('شجرة النسب 3D')")
        page.wait_for_timeout(2000) # Wait for Three.js init

        # Take screenshot of the tree
        page.screenshot(path="/home/jules/verification/tree_nebula.png")
        page.wait_for_timeout(500)

        # 5. Open Blockchain
        page.evaluate("closeTree()")
        page.wait_for_timeout(500)

        page.evaluate("toggleSidebar()")
        page.wait_for_timeout(500)

        # In sidebar, it's ٧. العقود الذكية (بلوك تشين)
        page.evaluate("openInfoModal('blockchain')")
        page.wait_for_timeout(1000)

        # Take screenshot of Blockchain ledger
        page.screenshot(path="/home/jules/verification/blockchain_ledger.png")
        page.wait_for_timeout(500)

        # 6. Open Stats
        page.evaluate("closeInfoModal()")
        page.wait_for_timeout(500)

        page.evaluate("openInfoModal('stats')")
        page.wait_for_timeout(1000)

        # Take screenshot of Stats
        page.screenshot(path="/home/jules/verification/stats_dashboard.png")
        page.wait_for_timeout(1000)

        context.close()
        browser.close()

if __name__ == "__main__":
    verify_new_features()
