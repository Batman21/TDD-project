from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # X has heard about a cool new online to-do app. X goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # X notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # X is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # X puts Economics Assignment as her first task.
        inputbox.send_keys('Economics Assignment')

        # When she hits enter, the page updates, and now the page lists
        # "1: Economics Assignment" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Economics Assignment')

        # There is still a text box inviting her to add another item. She
        # enters "Metaphysics Assignment."
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Metaphysics Assignment')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('2: Metaphysics Assignment')
        self.check_for_row_in_list_table('1: Economics Assignment')

        # X wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
