# from behave import *
# import socket
# import requests
# import http.client, urllib.parse
# import ssl
#
# @given('The Hong Kong Observatory API is ready')
# def step_given_api_is_ready(context):
#     pass
#
# @when('Send a get request to Hong Kong Observatory api "{url}"')
# def step_send_get_request(context, url):
#
#     http_client = http.client.HTTPSConnection(url)
#     http_client.request("GET", "/")
#     response = http_client.getresponse()
#     context.response_code = response.code
#
# @then('we will received a# def step_validate_response(context, code): "{code}" response code')
# def step_validate_response1(context, message):
#     convert = json.loads(context.body)
#     assert context.response_code == int(code)
#
