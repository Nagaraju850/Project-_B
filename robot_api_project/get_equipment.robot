*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    Equipment_API    ${BASE_URL}

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Test Get All Equipment
    ${response}=    GET On Session    Equipment_API    /equipment
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    Equipment A
    Should Contain    ${response.text}    Equipment B
    Log To Console    ${response.text}

Test Get Equipment 101
    ${response}=    GET On Session    Equipment_API    /equipment/101
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    Equipment A

Test Get Equipment 102
    ${response}=    GET On Session    Equipment_API    /equipment/102
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    Equipment B

Test Unknown Equipment Returns 404
    ${response}=    GET On Session    Equipment_API    /equipment/999    expected_status=404
    Should Be Equal As Integers    ${response.status_code}    404
    Should Contain    ${response.text}    Equipment not found

Test Home Page Displays Equipment 101
    ${response}=    GET On Session    Equipment_API    /?id=101
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    Equipment A

Test Home Page Displays Equipment 102
    ${response}=    GET On Session    Equipment_API    /?id=102
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    Equipment B