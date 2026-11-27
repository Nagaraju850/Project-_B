*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    Equipment_API    ${BASE_URL}

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000
${EQUIPMENT_ID}    101

*** Test Cases ***
Get Equipment By Argument
    ${response}=    GET On Session    Equipment_API    /equipment/${EQUIPMENT_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    "id": ${EQUIPMENT_ID}
    Log To Console    ${response.text}
