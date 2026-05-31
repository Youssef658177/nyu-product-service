Feature: The product store service back-end

Background:
    Given the following products
        | name       | description | price  | available | category    |
        | Fedora     | A fine hat  | 49.95  | true      | CLOTHING    |
        | Smartphone | Tech gadget | 599.00 | true      | ELECTRONICS |
        | Blender    | For shakes  | 29.95  | false     | HOME        |

Scenario: Read a Product
    When I visit the "Home Page"
    And I set the "Name" to "Fedora"
    And I press the "Search" button
    Then I should see the message "Success"
    When I press the "View" button
    Then I should see "Fedora" in the "Name" field

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "Fedora"
    And I press the "Search" button
    Then I should see "Fedora" in the results
    When I change the "Name" to "Red Fedora"
    And I press the "Update" button
    Then I should see the message "Success"

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Blender"
    And I press the "Search" button
    Then I should see "Blender" in the results
    When I press the "Delete" button
    Then I should see the message "Product has been Deleted!"

Scenario: List All Products
    When I visit the "Home Page"
    And I press the "Clear" button
    And I press the "Search" button
    Then I should see "Fedora" in the results
    And I should see "Smartphone" in the results
    And I should see "Blender" in the results

Scenario: Search by Name
    When I visit the "Home Page"
    And I set the "Name" to "Smartphone"
    And I press the "Search" button
    Then I should see "Smartphone" in the results
    And I should not see "Fedora" in the results

Scenario: Search by Category
    When I visit the "Home Page"
    And I select "ELECTRONICS" from the "Category" dropdown
    And I press the "Search" button
    Then I should see "Smartphone" in the results
    And I should not see "Fedora" in the results

Scenario: Search by Availability
    When I visit the "Home Page"
    And I select "True" from the "Available" dropdown
    And I press the "Search" button
    Then I should see "Fedora" in the results
    And I should not see "Blender" in the results
