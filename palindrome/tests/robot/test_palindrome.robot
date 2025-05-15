*** Settings ***
Documentation     get_palindrome.py e2e tests
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
Valid Input
    [Documentation]    should return a palindrome for valid input
    ${result}=    Get Palindrome    madam
    Should Be Equal As Strings    ${result.stdout}    Your palindrome is amdma.

Non-Palindrome Input
    [Documentation]    should return a message for non-palindrome input
    ${result}=    Get Palindrome    hello
    Should Be Equal As Strings    ${result.stdout}    hello cannot be a palindrome.

Wildcard Input
    [Documentation]    should return a palindrome for input with wildcards
    ${result}=    Get Palindrome    hello??
    Should Be Equal As Strings    ${result.stdout}    Your palindrome is ehlolhe.

Empty Input
    [Documentation]    should return the usage message for empty input
    ${result}=    Get Palindrome    ${EMPTY}
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}

Numeric Input
    [Documentation]    should return the usage message for numeric input
    ${result}=    Get Palindrome    12321
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}

Capital Letters
    [Documentation]    should return the usage message for capital letters
    ${result}=    Get Palindrome    Madam
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}

Special Characters
    [Documentation]    should return the usage message for special characters
    ${result}=    Get Palindrome    &@&
    Should Be Equal As Strings    ${result.stdout}    ${USAGE}