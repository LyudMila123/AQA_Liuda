import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dobrobut.com/ua")
    page.goto("https://dobrobut.com/ua/doctors")
    page.goto("https://dobrobut.com/ua/doctors?type=online")
    page.goto("https://dobrobut.com/ua/doctors?type=online&search&letter=%D0%BE")
    page.goto("https://dobrobut.com/ua/doctors?type=online&search&letter=%D1%87")
    page.goto("https://dobrobut.com/ua/about/c-kontakty")
    page.goto("https://dobrobut.com/ua/doctors?type=expert")
    page.goto("https://dobrobut.com/ua/doctors?type=expert&search")
    page.goto("https://dobrobut.com/ua/doctors/category-allergology")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
