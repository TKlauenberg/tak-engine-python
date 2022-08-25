Feature: Move Validation
    As a User
    I want that my moves are validated
    So that I cannot make wrong moves

  Background: Initial Game
    Given Bop initializes a game with the parameters
      | size |
      |    5 |
    And Bop places a flat stone at a1
    And Bop places a flat stone at a2

  Scenario: Move out of board
    When Bop tries to move one stone from a2 left
    Then Bop should get an error
    And The error message should be "Cannot move out of the board"

  Scenario: Move on a standing stone
    Given Bop places a standing stone at b1
    When Bop tries to move one stone from a1 right
    Then Bop should get an error
    And The error message should be "Can only flatten a wall with a capstone"

  Scenario: Move on a capstone
    When Bop places a capstone at b1
    And Bop tries to move one stone from a1 right
    Then Bop should get an error
    And The error message should be "Cannot move a stone onto a capstone"

  Scenario Outline: Wrong place of stone
    When Bop tries to place a <stone> at a1
    Then Bop should get an error
    And The error message should be "Cannot place a stone on a non empty board"

    Examples: 
      | stone          |
      | flat stone     |
      | standing stone |
      | capstone       |

  Scenario: Moving through wall
    Given Bop places a capstone at b1
    And Bop places a standing stone at b2
    And Bop moves one stone from b1 left
    And Bop moves one stone from b2 left
    When Bop tries to move 2 stones from a1 up, dropping one stone at each square
    Then Bop should get an error
    And The error message should be "Can only flatten a wall with a capstone"

  Scenario: Wrong Flattening
    Given Bop places a capstone at b1
    And Bop places a standing stone at b2
    And Bop moves one stone from b1 left
    And Bop moves one stone from b2 left
    When Bop tries to move 2 stones from a1 up with all stones
    Then Bop should get an error
    And The error message should be "Can only flatten a wall with one capstone"

  Scenario: Move a stone from the wrong Player
    When Bop tries to move one stone from a1 up
    Then Bop should get an error
    And The error message should be "Player doesn't control that square"
