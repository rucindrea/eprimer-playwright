from playwright.sync_api import Page

def test_word_text(page: Page):
    page.goto('https://www.exploratorytestingacademy.com/app')
    page.fill("#inputtext", "to be")
    page.click("#CheckForEPrimeButton")
    
    assert page.inner_text("#wordCount") == "1"
    assert page.inner_text("#discouragedWordCount") == "1"
    assert page.inner_text("#possibleViolationCount") == "0"