from playwright.sync_api import Page

def test_word_text(page: Page):
    page.goto('https://www.exploratorytestingacademy.com/app')
