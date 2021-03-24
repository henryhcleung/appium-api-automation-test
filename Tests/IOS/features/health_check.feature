#@Health_Check
#Feature: Checking the Hong Kong Observatory API health
#
#  Scenario: Hong Kong Observatory API health check
#     Given The Hong Kong Observatory API is ready
#     When Send a get request to Hong Kong Observatory api "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"
#     Then we will received a "200" response code
#
#
