Feature: Move Validation

    As a User
    I want that my moves are validated
    So that I cannot make wrong moves

    Background: Initial Game
        Given the user initializes a game with the parameters
            | size |
            | 5    |
        And the user places a flat stone at a1
        And the user places a flat stone at a2

    Scenario: Move out of board
        When the user tries to move one stone from a2 left
        Then the user should get an error
        And The error message should be "Cannot move out of the board"

    Scenario: Move on a standing stone
        Given the user places a standing stone at b1
        When the user tries to move one stone from a1 right
        Then the user should get an error
        And The error message should be "Can only flatten a wall with a capstone"

    Scenario: Move on a capstone
        When the user places a capstone at b1
        And the user tries to move one stone from a1 right
        Then the user should get an error
        And The error message should be "Cannot move a stone onto a capstone"

    Scenario Outline: Wrong place of stone
        When the user tries to place a <stone> at a1
        Then the user should get an error
        And The error message should be "Cannot place a stone on a non empty board"
        Examples:
            | stone          |
            | flat stone     |
            | standing stone |
            | capstone       |

    Scenario: Moving through wall
        Given the user places a capstone at b1
        And the user places a standing stone at b2
        And the user moves one stone from b1 left
        And the user moves one stone from b2 left
        When the user tries to move 2 stones from a1 up, dropping one stone at each square
        Then the user should get an error
        And The error message should be "Can only flatten a wall with a capstone"

    Scenario: Wrong Flattening
        Given the user places a capstone at b1
        And the user places a standing stone at b2
        And the user moves one stone from b1 left
        And the user moves one stone from b2 left
        When the user tries to move 2 stones from a1 up with all stones
        Then the user should get an error
        And The error message should be "Can only flatten a wall with one capstone"