"""E-Prime checker feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
from playwright.sync_api import Page

@scenario('eprimer_text_check.feature', 'Checking text for E-Prime words')
def test_checking_text_for_eprime_words():
    pass

@given('I am on the "https://www.exploratorytestingacademy.com/app" page')
def i_am_on_the_httpswwwexploratorytestingacademycomapp_page(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app")


@when('I click "Check for E-Prime"')
def i_click_check_for_eprime(page: Page):
    page.click("#CheckForEPrimeButton")


@when(parsers.parse('I enter the text {text}'))
def i_enter_the_text_to_be_or_not_to_be_is_hamlets_dilemma(page: Page, text):
    page.fill("#inputtext", text)


@then(parsers.parse('I should see {violations} possible violations'))
def i_should_see_0_possible_violations(page: Page, violations):
    assert page.inner_text("#possibleViolationCount") == violations


@then(parsers.parse('I should see {discouraged} discouraged words'))
def i_should_see_3_discouraged_words(page: Page, discouraged):
    assert page.inner_text("#discouragedWordCount") == discouraged


@then(parsers.parse('I should see {words} words altogether'))
def i_should_see_9_words_altogether(page: Page, words):
    assert page.inner_text("#wordCount") == words
    
