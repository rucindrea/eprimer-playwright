import pytest
from playwright.sync_api import Page
from assertpy import assert_that

main_app_url = 'https://www.exploratorytestingacademy.com/app'

data = [
    ('To be or not to be is Hamlet\'s dilemma', 9, 3),
    ('nothing', 1, 0),
    ('to be or not to be', 6, 2)
]

@pytest.mark.parametrize('input_text, word_count, discouraged_word_count', data)
def test_word_text(page: Page, input_text, word_count, discouraged_word_count):
    page.goto(main_app_url)
    page.type('#inputtext', input_text)
    page.click('#CheckForEPrimeButton')
    
    assert page.locator('#eprimeoutput').inner_text() == input_text
    assert page.locator('#wordCount').inner_text() == str(word_count)
    assert page.locator('#discouragedWordCount').inner_text() == str(discouraged_word_count)
    