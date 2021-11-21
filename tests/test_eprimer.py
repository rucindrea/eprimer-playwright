from playwright.sync_api import Page

main_app_url = 'https://www.exploratorytestingacademy.com/app'
input_text = 'To be or not to be is Hamlet\'s dilemma'
expected_word_count = 9
expected_discouraged_word_count = 3

def test_word_text(page: Page):
    page.goto(main_app_url)
    page.type('#inputtext', input_text)
    page.click('#CheckForEPrimeButton')

    assert page.locator('#eprimeoutput').inner_text() == input_text
    assert page.locator('#wordCount').inner_text() == str(expected_word_count)
    assert page.locator('#discouragedWordCount').inner_text() == str(expected_discouraged_word_count)
    