from playwright.sync_api import sync_playwright
import os
import json

def verify_integration():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local index.html
        path = os.path.abspath("index.html")
        page.goto(f"file://{path}")

        # Inject some test data into localStorage
        test_data = [
            {"id": "HY-12345", "name": "فيصل الحياني", "gov": "الرياض", "verified": True, "date": "2024/01/01"}
        ]
        page.evaluate(f"localStorage.setItem('HY_TRIBE_VAULT_V1', '{json.dumps(test_data)}')")
        page.reload()

        # Perform search
        page.fill("#searchInput", "فيصل")
        page.keyboard.press("Enter")

        # Explicitly call searchName just in case keyup wasn't enough
        page.evaluate("searchName()")

        # Wait for results
        page.wait_for_selector("#resultsGrid >> text=فيصل الحياني")

        # Check for the certificate button
        cert_btn = page.query_selector("text=تحميل شهادة التوثيق")
        if cert_btn:
            print("Found certificate button in results.")

        # Take screenshot
        page.screenshot(path="verification/final_search_result.png")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    verify_integration()
