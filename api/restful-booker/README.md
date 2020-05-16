# Percobaan automate Restful Booker API
https://restful-booker.herokuapp.com/apidoc/index.html

Scenario: Create Booking
    Given I am authenticated user
    When I Create new booking
    Then I should see the booking created
    And I should be able to verify booking detail