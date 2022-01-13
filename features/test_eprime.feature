Feature: Eprime text analysis
    As a user, 
    I want to verify my text for violations of eprime,
    So I learn to write proper English

    Scenario: Eprime analysis
        Given the eprime page is displayed
        When user analyses sentence "to be or not to be"
        Then user learns sentence has "2" be-verbs, "0" possible be-verbs and total "6" words

    Scenario: Incorrect Eprime analysis
        Given the eprime page is displayed
        When user analyses sentence "To be or not to be - Hamlet's dilemma"
        Then user learns sentence has "2" be-verbs, "1" possible be-verbs and total "9" words

    Scenario: Incorrect Eprime analysis test
        Given the eprime page is displayed
        When user analyses sentence "test"
        Then user learns sentence has "0" be-verbs, "0" possible be-verbs and total "1" words
