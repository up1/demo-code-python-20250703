*** Settings ***
Library  SeleniumLibrary
Test Teardown  Close All Browsers

*** Test Cases ***
Play with game
    Open Browser  http://localhost:5000/  chrome
    Maximize Browser Window
    Click Element  name=reset
    Sleep  1s
    Click Element  xpath=//tr[1]/td[1]/button
    Sleep  1s
    Click Element  xpath=//tr[1]/td[2]/button
    Sleep  1s
    Click Element  xpath=//tr[1]/td[3]/button
    Sleep  1s
    Click Element  xpath=//tr[2]/td[1]/button
    Sleep  1s
    Click Element  xpath=//tr[2]/td[2]/button
    Sleep  1s
    Click Element  xpath=//tr[2]/td[3]/button
    Sleep  1s
    Click Element  xpath=//tr[3]/td[1]/button
    Sleep  1s
    Click Element  xpath=//tr[3]/td[2]/button
    Sleep  1s
    Click Element  xpath=//tr[3]/td[3]/button
