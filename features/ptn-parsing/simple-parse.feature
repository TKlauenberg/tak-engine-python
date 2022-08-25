Feature: Parse PTN File
    As a User
    I want to read PTN Files
    So that I can start with initial Game State

  Scenario: PTN without a move
    When Bop parse the PTN file
      """
      [Size "5"]
      """
    Then The parsing should be successful
    And The size of the board is 5
    And The board is empty
