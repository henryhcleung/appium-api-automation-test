"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.
before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.
before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.
before_tag(context, tag), after_tag(context, tag)
"""
# from selenium import webdriver
# from environment_common import init_selenium_chrome_driver
# from environment_common import use_headless_mode
# from environment_common import set_remote_chrome_addr
# # -- SETUP: Use cfparse as default matcher
# from behave import use_step_matcher
# step_matcher("cfparse")
# use_headless_mode(False)


# def before_all(context, feature):
#     # context.config.setup_logging()
#     pass

def after_all(context):
    pass
#
# def before_feature(context, feature):
#     pass