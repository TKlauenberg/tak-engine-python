Feature: Game initialization

        As a User
        I want to initialize a game with some starting options
        So that I start a Game

        Scenario Outline: needed parameters
        When I initialize a game with the parameters
            | size | <size> |
        Then The size of the board is <size>
        And The board is empty
        Examples:
            | size |
            | 5  |