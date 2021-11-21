import pytest
from pages.eprimer_page import EPrimerPage

data = [
    ('To be or not to be is Hamlet\'s dilemma', 9, 3),
    ('nothing', 1, 0),
    ('to be or not to be', 6, 2)
]

@pytest.mark.parametrize('input_text, word_count, discouraged_word_count', data)
def test_word_text(page, input_text, word_count, discouraged_word_count):
    eprimer_page = EPrimerPage(page)
    eprimer_page.navigate().set_input_text(input_text)
    eprimer_page.click_check_button()
    
    assert eprimer_page.get_output() == input_text
    assert eprimer_page.get_word_count() == word_count
    assert eprimer_page.get_discouraged_word_count() == discouraged_word_count
