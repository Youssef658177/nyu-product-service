from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@when('I visit the "Home Page"')
def step_impl(context):
    context.driver.get(context.base_url)

@when('I set the "{element_name}" to "{text_value}"')
def step_impl(context, element_name, text_value):
    element_id = element_name.lower().replace(" ", "_")
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_value)

@when('I press the "{button_name}" button')
def step_impl(context, button_name):
    button_id = button_name.lower().replace(" ", "_") + "-btn"
    context.driver.find_element(By.ID, button_id).click()

@then('I should see the message "{message}"')
def step_impl(context, message):
    flash_message = context.driver.find_element(By.ID, "flash_message").text
    assert message in flash_message

@then('I should see "{text_value}" in the "{element_name}" field')
def step_impl(context, text_value, element_name):
    element_id = element_name.lower().replace(" ", "_")
    element = context.driver.find_element(By.ID, element_id)
    assert element.get_attribute("value") == text_value

@when('I change the "{element_name}" to "{text_value}"')
def step_impl(context, element_name, text_value):
    element_id = element_name.lower().replace(" ", "_")
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_value)

@then('I should see "{text_value}" in the results')
def step_impl(context, text_value):
    table = context.driver.find_element(By.ID, "search_results")
    assert text_value in table.text

@then('I should not see "{text_value}" in the results')
def step_impl(context, text_value):
    table = context.driver.find_element(By.ID, "search_results")
    assert text_value not in table.text

@when('I select "{option_value}" from the "{dropdown_name}" dropdown')
def step_impl(context, option_value, dropdown_name):
    dropdown_id = dropdown_name.lower().replace(" ", "_")
    select = Select(context.driver.find_element(By.ID, dropdown_id))
    select.select_by_visible_text(option_value)
