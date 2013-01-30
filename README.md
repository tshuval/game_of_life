game_of_life
============

Class that implements the Game Of Life logic.  
The class creates a grid of Cell objects, not a grid of  
zeros and ones. This concept was chosen because it is extensible.  
If a Cell needs to be more than just 0/1, it can be extended  
easily to add properties, methods, logic, etc...  

Usage:

    g = Grid(grid, [debug=False])

where
    'grid' is a list of n lists of n items  
    'debug' can be set to True to display some output

Properties:  
    grid - Returns the grid in its current life cycle  
    visual_grid - Returns the grid as a text matrix  
    original_grid - The original grid  

Methods:  
    iterate(n=1) - Runs n ticks (iterations) on the grid  
    tick() - Runs a single iteration.  

Example:  
Create a 3x3 grid and run 5 iterations. Display results:  

    g = Grid([[0, 1, 0], [1, 0, 0], [0, 0, 0]], True)
    g.iterate(5)
