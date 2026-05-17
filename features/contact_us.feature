Feature: Contact Us

  Scenario: Submit contact us form
    Given user opens contact us page
    When user submits contact form
    Then contact form should be submitted successfully