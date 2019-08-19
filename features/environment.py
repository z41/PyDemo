from core.testsession import TestSession
__author__ = 'Serge'


def before_all(context):
    context.session = TestSession.get_instance()

def after_all(context):
    context.session.driver.quit()