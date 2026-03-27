import asyncio
from playwright.async_api import async_playwright
import os
import subprocess
import time

async def run_verification():
    # Start server
    server_process = subprocess.Popen(['python3', '-m', 'http.server', '3000'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})

        try:
            # 1. Landing Page & Loading Tunnel
            await page.goto('http://localhost:3000')
            await page.wait_for_timeout(4000) # Wait for loading tunnel
            await page.screenshot(path='final_landing_hero.png')
            print("Captured landing page.")

            # 2. Open Sidebar - Targeting the toggle in header
            # The previous error was targeting the close button inside the sidebar which is hidden
            await page.click('header button[onclick="toggleSidebar()"]')
            await page.wait_for_timeout(1000)
            await page.screenshot(path='final_sidebar_menu.png')
            print("Captured sidebar menu with 16 modules.")

            # 3. Open 3D Tree from sidebar
            await page.click('button[onclick="openTree();"]')
            await page.wait_for_timeout(3000)
            await page.screenshot(path='final_3d_tree.png')
            print("Captured 3D Lineage Tree.")
            await page.click('#treeModal button[onclick="closeTree()"]')

            # 4. Login to Registry
            await page.fill('#landing-email', 'admin@hayyani.com')
            await page.click('button[onclick="handleLandingLogin()"]')
            await page.wait_for_timeout(3000)
            await page.screenshot(path='final_registry_view.png')
            print("Captured registry view.")

        except Exception as e:
            print(f"Error during verification: {e}")
        finally:
            await browser.close()
            server_process.terminate()

if __name__ == "__main__":
    asyncio.run(run_verification())
