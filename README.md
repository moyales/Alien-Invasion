# Alien-Invasion
A simple Space Invaders-like game using Python and Pygame 

*(adapted from Chapters 12-14 of Eric Matthes' Python Crash Course)*
This is one of my first forays into programming a game

**Plans for adding aliens**
* Examine code and determine if refactoring is necessary
* Add a single alien to the top-left corner of the screen with appropriate spacing
* Use spacing around first alien and screen size to determine how many aliens can fit
    on the screen
* Make the fleet move sideways and down until the entire fleet is shot down, an alien
    hits the ship, or an alien reaches the ground. If whole fleet is down, then create
    a new fleet.
* Limit the number of ships the player can use, and end the game when the player has 
    used up the allotment of ships

**Additional Things**
* 13.1 / 13.2 : Find an image of a star and create a background of random star patterns
* 13.3 : Create raindrops and get them to fall in the background
* 13.5 : Create a game of "catch" with a falling ball and a moving player figure *side practice project*
    * 13.6 : Game over condition for this game of catch
    
* 14.4 : Store the high score in a file and retrieve file
* 14.5 : Refactor game code so one function does one thing
* 14.6 : Find ways to expand the game, such as adding *sound effects* or *shields*

**Next Steps**
* Make the aliens move (DONE)
* Shoot those aliens down! (DONE)
* Account for collisions between the ship and alien (DONE)
* Account for collisions between the bullets and alien (DONE)
* Add a way to count score in the game
