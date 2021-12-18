Feature: E-Prime checker

Scenario Outline: Checking text for E-Prime words
    Given I am on the "https://www.exploratorytestingacademy.com/app" page
    When I enter the text <text>
    And I click "Check for E-Prime"
    Then I should see <words> words altogether
    And I should see <discouraged> discouraged words
    And I should see <violations> possible violations

    Examples:
    | text | words | discouraged | violations |
    | "to be" | 2 | 1 | 0 |
    | "To be or not to be is Hamlet's dilemma" | 9 | 3 | 1 |
    | "" | 0 | 0 | 0 |
    | "Maaret's test" | 3 | 0 | 1 |