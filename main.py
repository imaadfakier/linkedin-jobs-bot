import config
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

inputs = [
    os.environ.get('LINKEDIN_USERNAME'),
    os.environ.get('LINKEDIN_PASSWORD'),
]
chrome_driver_path = 'type chrome driver path here'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# logging into linkedin
driver.get(url='https://www.linkedin.com/')
driver.maximize_window()
input_fields = driver.find_elements_by_class_name(name='input__input')
for input_field_index in range(len(input_fields)):
    input_fields[input_field_index].send_keys(inputs[input_field_index])
sign_in_button = driver.find_element_by_class_name(name='sign-in-form__submit-button')
sign_in_button.click()

# searching for job
jobs_anchor_tag = driver.find_element_by_xpath(xpath='//*[@id="global-nav"]/div/nav/ul/li[3]')
jobs_anchor_tag.click()
time.sleep(5)  # time in seconds
search_bar_input = driver.find_element_by_css_selector(
    css_selector='.jobs-search-box__text-input.jobs-search-box__keyboard-text-input'
)
search_bar_input.send_keys('python developer')
location_bar_input = driver.find_element_by_css_selector(
    css_selector='.jobs-search-box__input.jobs-search-box__input--location input.jobs-search-box__text-input'
)
location_bar_input.send_keys('London, England, United Kingdom')
search_jobs_button = driver.find_element_by_class_name(name='jobs-search-box__submit-button')
search_jobs_button.click()

# easily apply filter
time.sleep(5)
easily_apply_button = driver.find_element_by_xpath(
    xpath='//*[@id="search-reusables__filters-bar"]/ul/li[8]/div/button'
)
# print(easily_apply_button.text)
easily_apply_button.click()

# save job listing
time.sleep(5)
save_listing_button = driver.find_element_by_class_name(name='jobs-save-button')
save_listing_button.click()

# follow company (that posted listing)
time.sleep(10)
job_salary_info = driver.find_element_by_css_selector(
    css_selector='.job-view-layout .jobs-details__main-content #SALARY'
)
scroll_into_view = driver.execute_script('arguments[0].scrollIntoView(true)', job_salary_info)
time.sleep(5)
follow_company_button = driver.find_element_by_class_name(name='follow')
follow_company_button.click()

# driver.quit()
