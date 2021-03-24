@Health_Check
Feature: Checking the Tandem API health

  Scenario: Tandem API health check
     Given The tandem API is ready
     When Send a get request to tandem api "tandem-alb-1769846793.ap-southeast-1.elb.amazonaws.com"
     Then we will received a "200" response code
     Then we will received a "Welcome to Tandem API!"


