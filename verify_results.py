import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_path = f"file://{os.getcwd()}/index.html"

        await page.goto(file_path)

        # Add test data and reload
        await page.evaluate("""() => {
            const testData = [
                {id: 1, name: "أحمد الحياني"},
                {id: 2, name: "سارة الحياني"},
                {id: 3, name: "خالد الحياني"},
                {id: 4, name: "فاطمة الحياني"},
                {id: 5, name: "محمد الحياني"}
            ];
            localStorage.setItem('HY_TRIBE_VAULT_V1', JSON.stringify(testData));
        }""")

        await page.reload()

        # Wait for stats badge - use state='attached' if it's still transparent,
        # but my code should remove opacity-0
        await page.wait_for_selector('#stats-badge:not(.opacity-0)', timeout=5000)

        # Type search query
        await page.fill('input[type="text"]', "أحمد")
        await page.wait_for_timeout(1000)

        results_visible = await page.is_visible('#results:not(.hidden)')
        print(f"Results visible: {results_visible}")

        # Capture the search result area
        await page.screenshot(path="verification/search_results_احمد.png")

        # Check if the result "أحمد الحياني" is there
        content = await page.content()
        if "أحمد الحياني" in content:
            print("Found result text")
        else:
            print("Result text NOT found")

        await browser.close()

asyncio.run(run())
