# MyObservatory
This repository is MyObservatory automation test using behave.

## Setup local environment
   1. ```brew install python```
   2. ```pip3 install behave```
   3. Check whether it's succesfuly installed ```behave --version``` result is something like: ```behave 1.
   4. ```brew install pre-commit``` should display the version you are using ```pre-commit --version```
   5. ```pip3 install requests```
   6. ```brew install node```      # get node.js
   7. ```sudo npm install -g appium --unsafe-perm=true --allow-root```  # get appium
   8. ```sudo npm install wd```         # get appium client
   9. ```appium &```               # start appium

## Run Task1 - AOS (UI)
   1. ```cd /Users/henryhcleung/MyObservatory/Tests/Task1/AOS/features```
   2. ```Behave```

## Run Task1 - IOS (UI)
   1. ```cd /Users/henryhcleung/MyObservatory/Tests/Task1/IOS/features```
   2. ```Behave```

## Run Task2 (API)
   1. ```cd /Users/henryhcleung/MyObservatory/Tests/Task2```
   2. ```Behave```

## TroubleShoot 
   1. ```killall -9 node``` when the appium port is occupied