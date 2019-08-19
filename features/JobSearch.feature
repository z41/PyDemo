# Created by Serge at 19.08.2019
Feature: Searching for a job on Kaseya website

  Scenario: Searching for SDET jobs on Kaseya website
    When I open careers page
    And I search for
      | what | department  | where          |
      | test | Development | Minsk, Belarus |
    Then I hopefully will get at least 1 result