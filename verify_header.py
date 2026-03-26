import asyncio
from playwright.async_api import async_playwright
import os

async def verify_header():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        path = os.path.abspath("index.html")
        page = await browser.new_page()
        await page.goto(f"file://{path}")
        await page.wait_for_timeout(1000)

        # Target header buttons specifically
        sidebar_btn = page.locator("header button[onclick='toggleSidebar()']")
        admin_btn = page.locator("header button[onclick='toggleAdmin()']")

        sidebar_box = await sidebar_btn.bounding_box()
        admin_box = await admin_btn.bounding_box()

        if not sidebar_box or not admin_box:
            print("Could not find header buttons.")
            return

        print(f"Sidebar Toggle X: {sidebar_box['x']}")
        print(f"Admin Button X: {admin_box['x']}")

        # In RTL/LTR context, we want Admin on the right, Sidebar on the left.
        # Right has higher X value.
        if admin_box['x'] > sidebar_box['x']:
            print("Layout Correct: Admin is to the right of Sidebar.")
        else:
            print("Layout Incorrect: Sidebar is to the right of Admin.")

        await page.screenshot(path="/home/jules/verification/screenshots/header_check.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_header())
