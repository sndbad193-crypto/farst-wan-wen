import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 2000})
        file_path = f"file://{os.getcwd()}/index.html"

        await page.goto(file_path)

        # Inject data
        await page.evaluate("""() => {
            const testData = [
                {id: "HY-001", name: "أحمد الحياني", gov: "الأنبار", date: "2024/01/01"},
                {id: "HY-002", name: "خالد الحياني", gov: "بغداد", date: "2024/01/01"}
            ];
            localStorage.setItem('HY_TRIBE_VAULT_V1', JSON.stringify(testData));
            initSystem();
        }""")

        # Trigger search
        await page.fill('#searchInput', "أحمد")
        # Explicitly call searchName just in case fill doesn't trigger keyup in all envs
        await page.evaluate("searchName()")
        await page.wait_for_timeout(1000)

        # Check if results section is visible
        is_visible = await page.is_visible('#results')
        print(f"Results section visible: {is_visible}")

        # Check count
        count = await page.locator('#resultsGrid > div').count()
        print(f"Results count: {count}")

        await page.screenshot(path="verification/search_full_page.png", full_page=True)

        await browser.close()

asyncio.run(run())
