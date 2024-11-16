Feature: Adding a record to the database

  Scenario: Successfully adding a record to the database
    Given the user has a valid record to add
    When the user adds the record to the database
    Then the record is saved to the database

  Scenario: Adding a record with invalid data
    Given the user has a record with invalid data
    When the user tries to add the record to the database
    Then the record is not saved to the database
    And an error message is displayed