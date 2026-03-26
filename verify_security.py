import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 375, 'height': 667})
        page = await context.new_page()
        path = "file://" + os.path.abspath("index.html")
        await page.goto(path)

        # 1. Verify Access Code
        # This will trigger a prompt, which Playwright can handle via dialogs
        async def handle_dialog(dialog):
            if "رمز الدخول" in dialog.message:
                await dialog.accept("1234")
            else:
                await dialog.dismiss()

        page.on("dialog", lambda dialog: asyncio.create_task(handle_dialog(dialog)))

        await page.click('header button[onclick="toggleAdmin()"]')
        await asyncio.sleep(1)

        # Take screenshot of admin panel
        await page.screenshot(path='admin_access_verified.png')
        print("Admin access verified screenshot saved.")

        # 2. Check registration wizard and biometric trigger (mock)
        await page.click('button[onclick="openBulkModal()"]')
        await asyncio.sleep(1)

        # Fill first step
        await page.fill('#name_first', 'اختبار')
        await page.fill('#national_id_secure', '999999')
        await page.click('#btnNext')
        await asyncio.sleep(0.5)

        # Step 2
        await page.click('#btnNext')
        await asyncio.sleep(0.5)

        # Step 3 - Biometrics
        await page.screenshot(path='biometric_step.png')
        print("Biometric step reached.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
