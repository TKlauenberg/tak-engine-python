@TPS
Feature: Parse PTN File with TPS
    As a User
    I want to read PTN Files with TPS
    So that I can start with initial Game State

  Scenario: empty TPS
    When Bop parse the PTN file
      """
      [Size "5"]
      [TPS "x5/x5/x5/x5/x5 1 1"]
      """
    Then The size of the board is 5
    And The board is empty

  Scenario: little board
    When Bop parse the PTN file
      """
      [Size "3"]
      [TPS "1,x2/x3/x3 2 1"]
      """
    Then The size of the board is 3
    And On a3 is a flat white stone

  Scenario: wrong board size
    When Bop parse the PTN file
      """
      [Size "3"]
      [TPS "1,x4/x5/x5/x5/x5 2 1"]
      """
    Then The parsing should be unsuccessful

  Scenario: TPS with stack of Stones
    When Bop parse the PTN file
      """
      [Size "3"]
      [TPS "1212,x2/x3/x3 1 1"]
      """
    Then On a3 should be a stack with stones "1212"
    And the top stone on a3 should be black

  Scenario Outline: TPS with special types of Stones
    When Bop parse the PTN file
      """
      [Size "5"]
      [TPS "1<type>,x4/x5/x5/x5/x5 1 1"]
      """
    Then the top stone on a5 should be of type <type>

    Examples:
      | type |
      | S    |
      | C    |

  Scenario Outline: next player
    When Bop parse the PTN file
      """
      [Size "3"]
      [TPS "x3/x3/x3 <Player> <Round>"]
      """
    Then the next Player should be Player <Player>
    And the current Round should be <Round>

    Examples:
      | Player | Round |
      |      1 |     1 |
      |      1 |    10 |
      |      2 |     1 |
      |      2 |    10 |

  Scenario: To much stones
    When Bop parse the PTN file
      """
      [Size "3"]
      [TPS "1212121212121212121212,x2/x3/x3 1 1"]
      """
    Then The parsing should be unsuccessful
    And The error message should be "Not enough stones for this board. Could not use TPS"
