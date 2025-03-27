from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://fluffy-halibut-6xp4xv9q79jcxrgx-8000.app.github.dev/polls/api/users/")
        assert "Django" in page.title()
        browser.close()

if __name__ == "__main__":
    test_homepage()