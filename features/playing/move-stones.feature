Feature: Move handling
    As a User
    I want to excecute different Moves
    in order to play the game

  Background: Initial Game
    Given Bop initializes a game with the parameters
      | size |
      |    5 |
    And Bop places a flat stone at a1
    And Bop places a flat stone at c3

  Scenario Outline: move into any direction
    When Bop moves one stone from c3 <direction>
    Then On <position> is a flat white stone

    Examples:
      | direction | position |
      | up        | c4       |
      | down      | c2       |
      | right     | d3       |
      | left      | b3       |

  Scenario: Move Stack
    Given Bop places a flat stone at c2
    And Bop places a flat stone at c1
    And Bop moves one stone from c3 down
    And Bop moves one stone from c1 up
    And Bop places a flat stone at a2
    When Bop moves 3 stones from c2 up, dropping one stone at each square
    Then On c3 is a flat white stone
    And On c4 is a flat white stone
    And On c5 is a flat black stone

  Scenario: Wall flattening
    Given Bop places a capstone at e3
    And Bop places a standing stone at d3
    When Bop moves one stone from e3 left
    Then On d3 should be a stack with a flat black stone and a white capstone
