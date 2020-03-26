Feature: Parse the right sizes
    As a User
    I want to read PTN Files only with correct board sizes
    So that I can start with initial Game State
    Scenario Outline: valid board size
        When I parse the PTN file
            """
            [Size "<size>"]
            """
        Then The parsing should be successful
        And The size of the board is <size>
        Examples:
            | size |
            | 3    |
            | 4    |
            | 5    |
            | 6    |
            | 8    |

    Scenario Outline: invalid board size
        When I parse the PTN file
            """
            [Size "<size>"]
            """
        Then The parsing should be unsuccessful
        Examples:
            | size |
            | 2    |
            | 7    |
            | 9    |
