from playwright.sync_api import sync_playwright
import os

def verify_sidebar():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local index.html
        path = os.path.abspath("index.html")
        page.goto(f"file://{path}")

        # Click the dashboard button in the header
        # Using a CSS selector that targets the button in the header specifically
        page.click("header button >> text=لوحة التحكم")

        # Wait for transition
        page.wait_for_timeout(500)

        # Take screenshot of the sidebar
        page.screenshot(path="verification/sidebar_open.png")

        # Verify logo text in the sidebar logo section
        logo_text = page.inner_text("#sidebar p.font-black.text-lg")
        print(f"Found logo text in sidebar: {logo_text}")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    verify_sidebar()
