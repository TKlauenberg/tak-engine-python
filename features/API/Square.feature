Feature: Stone Position

    As a developer
    I want to take and drop stones to a square and have appropiate Error Messages if it fails

    Scenario: dropStones
        Given an empty square
        When the developer drops a white stone
        Then the square should have a white stone