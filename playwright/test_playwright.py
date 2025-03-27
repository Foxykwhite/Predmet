from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Включаем запись трассировки
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()
        page.goto("https://github.com/")
        print("Page title:", page.title())

        # Сохраняем трассировку
        context.tracing.stop(path="github.zip")

        browser.close()

if __name__ == "__main__":
    test_homepage()