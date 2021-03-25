@9days_forecast
Feature: Checking next 9 days weather forecast 

  Scenario: Checking next 9 days weather forecast 
     Given Request next 9 days weather
     When Send a get request to Hong Kong Observatory api "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=" language is "tc"
     Then There will received a 200 response code
     Then Extract the relative humidity for the day after tomorrow

