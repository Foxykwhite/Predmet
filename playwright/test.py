import re
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Включаем запись трассировки
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://solid-goldfish-gvp7vx4jj663qpr-8000.app.github.dev")
    
    # Останавливаем и сохраняем трассировку
    context.tracing.stop(path="trace.zip")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)