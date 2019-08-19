from behave import given, when, then
from pages.careers import CareerPage

@when(u'I open careers page')
def open_careers(context):
    context.session.driver.get('https://www.kaseya.com/careers/')

@when(u'I search for')
def search_for_a_job(context):
    row = context.table[0]
    CareerPage(context.session.driver).search(row['what'], row['department'], row['where'])

@then(u'I hopefully will get at least {num} result')
def have_results(context, num):
    CareerPage(context.session.driver).validate_has_results(int(num))