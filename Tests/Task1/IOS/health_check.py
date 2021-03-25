from behave import *
import socket
import requests
from behave_pandas import table_to_dataframe, dataframe_to_table
import http.client, urllib.parse
import json
import ssl
import logging
from allure_commons.types import AttachmentType

@given('The Hong Kong Observatory API is ready')
def step_given_api_is_ready(context):
    pass

@when('Send a get request to Hong Kong Observatory api "{url}"')
def step_send_get_request(context, url):

    http_client = http.client.HTTPSConnection(url)
    http_client.request("GET", "/")
    response = http_client.getresponse()
    context.response_code = response.code

@then('we will received a "{code}" response code')
def step_validate_response(context, code):
    assert context.response_code == int(code)

