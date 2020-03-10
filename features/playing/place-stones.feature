Feature: Move handling

    As a User
    I want to excecute different Moves
    in order to play the game

    Background: Initial Game
        When the user initializes a game with the parameters
            | size |
            | 5    |

    Scenario: simple first move
        When the user places a flat stone at b2
        Then On b2 is a flat black stone

    Scenario: both player one move
        When the user places a flat stone at b2
        And the user places a flat stone at a1
        Then On b2 is a flat black stone
        Then On a1 is a flat white stone

    Scenario: completed second round
        When the user places a flat stone at b2
        And the user places a flat stone at a1
        And the user places a flat stone at a2
        And the user places a flat stone at a3
        Then On b2 is a flat black stone
        And On a1 is a flat white stone
        And On a2 is a flat white stone
        And On a3 is a flat black stone

    Scenario: place standing stone
        # first moves must be a flat stone
        When the user places a flat stone at b2
        And the user places a flat stone at a1
        And the user places a standing stone at a2
        And the user places a standing stone at a3
        Then On a2 is a standing white stone
        And On a3 is a standing black stone

    Scenario: place capstone
        # first moves must be a flat stone
        When the user places a flat stone at b2
        And the user places a flat stone at a1
        And the user places a capstone at a2
        And the user places a capstone at a3
        Then On a2 is a white capstone
        And On a3 is a black capstone
