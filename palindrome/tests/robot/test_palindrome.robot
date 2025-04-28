*** Settings ***
Documentation     Tests for the get_palindrome.py script.
Library           OperatingSystem
Library           BuiltIn
Library           Process

*** Test Cases ***
Test Palindrome With Valid Input
    [Documentation]    Test get_palindrome.py with a valid input string.
    ${result}=    Run Process      python3    palindrome/get_palindrome.py    madam
    Should Be Equal As Strings    ${result.stdout}    Your palindrome is amdma.

Test Palindrome With Non-Palindrome Input
    [Documentation]    Test get_palindrome.py with a non-palindrome input string.
    ${result}=    Run Process      python3    palindrome/get_palindrome.py    hello
    Should Be Equal As Strings    ${result.stdout}    hello cannot be a palindrome.

Test Palindrome With Empty Input
    [Documentation]    Test get_palindrome.py with an empty input string.
    ${result}=    Run Process      python3    palindrome/get_palindrome.py    ""
    Should Be Equal As Strings    ${result.stdout}    Your palindrome is "".

