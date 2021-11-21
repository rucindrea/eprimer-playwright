class EPrimerPage:
    @property
    def input_text_locator(self):
        return self.page.locator('#inputtext')
    
    @property
    def check_button(self):
        return self.page.locator('#CheckForEPrimeButton')
    
    @property
    def output_locator(self):
        return self.page.locator('#eprimeoutput')
    
    @property
    def word_count_locator(self):
        return self.page.locator('#wordCount')
    
    @property
    def discouraged_word_count_locator(self):
        return self.page.locator('#discouragedWordCount')
    
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto('https://www.exploratorytestingacademy.com/app')
        return self

    def set_input_text(self, text):
        self.input_text_locator.type(text)
        return self
        
    def click_check_button(self):
        self.check_button.click()
        return self
        
    def get_output(self):
        return self.output_locator.inner_text()
    
    def get_word_count(self):
        return int(self.word_count_locator.inner_text()) 
    
    def get_discouraged_word_count(self):
        return int(self.discouraged_word_count_locator.inner_text())