import pytest
from pytest_bdd import scenarios, given, when, then, parsers 
from playwright.sync_api import Page

HOME = "https://www.exploratorytestingacademy.com/app/"

scenarios('features/eprime.feature')

@given("the eprime page is displayed")
def eprime_home(page: Page):
    page.goto(HOME)

@when(parsers.parse('user analyses sentence "{phrase}"'))
def analyze_phrase(page: Page, phrase):
    page.fill("#inputtext", phrase)
    page.click("#CheckForEPrimeButton")

@then(parsers.parse('user learns sentence has "{violations}" be-verbs, "{discouraged}" possible be-verbs and total "{words}" words'))
def search_results(page: Page, words, violations, discouraged):
    assert page.inner_text("#wordCount") == words
    assert page.inner_text("#discouragedWordCount") == violations
    assert page.inner_text("#possibleViolationCount") == discouraged

