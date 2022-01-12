import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize("input_text, expected_wordcount,expected_discouraged, expected_violations", [
    ("to be", "2", "1", "0"), 
    ("", "0", "0", "0"),
    # ("Maaret's test", "3", "0", "1"),
    # ("one\ntwo", "2", "0", "0")
    (5000*"x", "1", "0", "0"), 
    ("TO BE", "2", "1", "0"), 
    # ("To be or not to be - Hamlet dilemma", "8", "2", "1")
    ("be, being, been, am, is, isn't, are, aren't, was, wasn't, were, weren't.", "12", "12", "0"), 
    # ("I'm, you're, we're, they're, he's, she's, it's, there's, here's, where's, how's, what's, who's, that's", "28", "5", "9")
    
], 
ids = ["to be", "empty", "many x-es", "CAPITALS", "all discouraged"])
def test_word_text(page: Page, input_text, expected_wordcount, expected_discouraged, expected_violations):
    page.goto('https://www.exploratorytestingacademy.com/app')
    page.fill("#inputtext", input_text)
    page.click("#CheckForEPrimeButton")
    
    assert page.inner_text("#wordCount") == expected_wordcount
    assert page.inner_text("#discouragedWordCount") == expected_discouraged
    
    assert page.inner_text("#possibleViolationCount") == expected_violations