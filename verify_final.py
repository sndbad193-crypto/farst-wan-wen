import asyncio
from playwright.async_api import async_playwright
import os
import signal
import subprocess
import time

async def run_verification():
    # Start the server
    server_process = subprocess.Popen(["node", "server.js"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2) # Wait for server to start

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Open the local file (assuming it's served or just opened as a file)
        # Using file:// path for index.html
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        print("Verifying Heritage Design...")
        # Check for emerald green background in header/logo or similar
        logo = await page.query_selector(".logo-box")
        assert logo is not None, "Logo box not found"

        print("Verifying Arabic Localization...")
        title = await page.inner_text("h1")
        assert "ديوان قبيلة الحياني" in title, f"Title incorrect: {title}"

        print("Verifying API Integration (Home Stats)...")
        # Wait for stats to load from API
        await page.wait_for_selector("#count-members")
        members_count = await page.inner_text("#count-members")
        assert members_count == "3", f"Expected 3 members, got {members_count}"

        print("Verifying 3D Tree View...")
        await page.click("text=شجرة النسب التفاعلية")
        await page.wait_for_selector("#tree-3d-container canvas")

        print("Verifying Admin Login...")
        await page.click("text=لوحة الإدارة")
        await page.fill("#adminPass", "1234")
        await page.click("text=تسجيل الدخول")

        # Wait for dashboard
        await page.wait_for_selector("#admin-dashboard:not(.hidden)")
        print("Admin Dashboard verified.")

        await page.screenshot(path="final_verification.png")
        await browser.close()

    # Terminate the server
    os.kill(server_process.pid, signal.SIGTERM)

if __name__ == "__main__":
    asyncio.run(run_verification())
