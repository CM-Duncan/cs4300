Feature: Movie Booking

  Scenario: User views movie list
    Given the database has movies
    When I visit the movie list page
    Then I should see a list of movies

  Scenario: User books a seat
    Given I am logged in
    And there is an available seat
    When I book the seat for a movie
    Then the seat should be marked as booked
