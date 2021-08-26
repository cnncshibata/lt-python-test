from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.wikipedia.org/
    page.goto("https://www.wikipedia.org/")

    # Click text=English
    page.click("text=English")
    # assert page.url == "https://en.wikipedia.org/wiki/Main_Page"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
