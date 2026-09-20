from pathlib import Path
from playwright.sync_api import sync_playwright


def test_capture_aritifact():
    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        assert "The Internet" in page.title()
        screenshot_path = artifacts_dir /"homepage.png"
        page.screenshot(path=str(screenshot_path),full_page=True)
        browser.close()

                         
     
 
 