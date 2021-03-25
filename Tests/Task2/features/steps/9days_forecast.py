from behave import *
from datetime import date
import socket
import requests
import ssl
import logging
import json

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

@given('Request next 9 days weather')
def step_request_9_days_weather(context):
    pass

@when('Send a get request to Hong Kong Observatory api "{url}" language is "{language}"')
def step_send_get_request_9_days_weather(context, url, language):
#request API
    response = requests.get(url+language)
    context.response_code = response.status_code
    context.body = response.text
    response.close()

@then('There will received a 200 response code')
def step_validate_9_days_weather_response(context):
#Check response status
    assert context.response_code == 200
    logging.info(context.response_code)

@then('Extract the relative humidity for the day after tomorrow')
def step_extract_tomorrow_weather(context):
#Convert into json format
    today = date.today()
    data = json.loads(context.body)
#Retreive the relative humidity
    data['weatherForecast'][2]['forecastDate']
    data['weatherForecast'][2]['forecastMinrh']
    data['weatherForecast'][2]['forecastMaxrh']

    logging.info(data['weatherForecast'][2]['forecastDate'])
    logging.info(data['weatherForecast'][2]['forecastMinrh'])
    logging.info(data['weatherForecast'][2]['forecastMaxrh'])

    # logging.info(today)
    # logging.info(context.response_code)
    # logging.info(context.body)

