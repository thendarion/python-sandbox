*** Settings ***
Documentation     Tests for the get_palindrome.py script.
Library           OperatingSystem
Library           BuiltIn
Library           Process

*** Variables ***
${USAGE}    Usage: python get_palindrome.py <candidate>\nCandidate must be a string of lowercase letters and wildcards (?)

*** Keywords ***
Get Palindrome
    [Arguments]    ${candidate}
    [Documentation]    Get the palindrome from the candidate string.
    ${result}=    Run Process      python3    palindrome/get_palindrome.py    ${candidate}
    Return From Keyword    ${result}

*** Test Cases ***
Test Palindrome With Valid Input
    [Documentation]    get_palindrome.py should return a palindrome for valid input
    ${result}=    Get Palindrome    madam
    Should Be Equal As Strings    ${result.stdout}    Your palindrome is amdma.

Test Palindrome With Non-Palindrome Input
    [Documentation]    get_palindrome.py should return a message for non-palindrome input
    ${result}=    Get Palindrome    hello
    Should Be Equal As Strings    ${result.stdout}    hello cannot be a palindrome.

Test Palindrome With Wildcard Input
    [Documentation]    get_palindrome.py should return a palindrome for input with wildcards
    ${result}=    Get Palindrome    hello??
    Should Be Equal As Strings    ${result.stdout}    Your palindrome is ehlolhe.

Test Palindrome With Empty Input
    [Documentation]    get_palindrome.py should return the usage message for empty input
    ${result}=    Get Palindrome    ${EMPTY}
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}

Test Palindrome With Numeric Input
    [Documentation]    get_palindrome.py should return the usage message for numeric input
    ${result}=    Get Palindrome    12321
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}

Test Palindrome With Capital Letters
    [Documentation]    get_palindrome.py should return the usage message for capital letters
    ${result}=    Get Palindrome    Madam
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}

Test Palindrome With Special Characters
    [Documentation]    get_palindrome.py should return the usage message for special characters
    ${result}=    Get Palindrome    &@&
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}