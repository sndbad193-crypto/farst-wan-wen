const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('index.html');
  await page.goto(filePath);
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'diwan_initial.png', fullPage: true });

  // Test navigation
  await page.click('button:has-text("02 //")');
  await page.waitForTimeout(500);
  await page.screenshot({ path: 'diwan_lineage.png', fullPage: true });

  await page.click('button:has-text("ADMIN_PANEL")');
  await page.waitForTimeout(500);
  await page.screenshot({ path: 'diwan_admin_login.png', fullPage: true });

  await browser.close();
})();
