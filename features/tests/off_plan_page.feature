# Created by chiranjivisingh at 11/6/24
Feature: off plan page feature tests


  Scenario: verify user can see all three options of visualization are “architecture”, “interior”, “lobby”
     Given open main reelly page
     When log in to the page using valid chirank577@gmail.com and Chirank@577
     And click on off plan at the left side menu
     And click on the first product
     Then Verify the three options of visualization are available
#     And Verify the visualization options are clickable