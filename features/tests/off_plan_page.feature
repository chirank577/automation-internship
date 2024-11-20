
Feature: off plan page feature tests


  Scenario: verify user can see all three options of visualization are “architecture”, “interior”, “lobby”
     Given open main reelly page
     When log in to the page using valid chirank577@gmail.com and Chirank@577
     And click on off plan at the left side menu
     And click on the first product
     Then Verify the three options of visualization are available and clickable


  Scenario: verify data driven case
     Given open main reelly page
     Then log into the page using data from xls file


