from behave import *
import socket
import requests
import http.client, urllib.parse
import ssl

@given('The Hong Kong Observatory API is ready')
def step_given_api_is_ready(context):
    pass

@when('Send a get request to Hong Kong Observatory api "{url}"')
def step_send_get_request(context, url):

    # http_client = http.client.HTTPSConnection(url)
    # http_client.request("GET", "")
    # response = http_client.getresponse()
    # context.response_code = response.code
    # http_client = http.client.HTTPSConnection(url)
    # http_client.request("GET", "")
    response = requests.get(url)
    context.response_code = response.status_code

@then('we will received a 200 response code')
def step_validate_response1(context):
    assert context.response_code == 200

