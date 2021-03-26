@ios_request_9days
Feature: Checking the Hong Kong Observatory 9 days forecasts with AOS version

  Scenario: To see Hong Kong Observatory 9 days forecasts with AOS version
     Given Open Hong Kong Observatory App
     Given User click the menu bar
     When User click the 9 days forecasts button
     Then User will see the next 9 days forecasts information


