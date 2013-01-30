"""
gol.py implements the Game Of Life logic using objects.

The module defines two classes:
    Grid and Cell

A Grid object is a grid of Cell objects.
Each Grid object has methods and properties to run the game and see the results.
"""

class Cell:
    """
    A class representing a single cell in the grid.
    Used by Grid class
    """
    def __init__(self, row, col, state):
        self.row = row
        self.col = col
        self.state = state
        self.new_state = None
        self.neighbours = []

    def make_neighbour_list(self, grid):
        """Construct a list of neighbours of the cell"""
        positions = ((-1, -1), (0, -1), (1, -1),
                     (-1, 0), (1, 0),
                     (-1, 1), (0, 1), (1, 1))
        n = len(grid)
        for row, col in positions:
            nrow = self.row + row
            ncol = self.col + col
            # The modulator is used to ensure border wrapping
            self.neighbours.append(grid[nrow % n][ncol % n])

    def run_rules(self):
        """Execute the Game Of Life set of rules"""
        score = sum(neighbour.get_state() for neighbour in self.neighbours)
        self.new_state = self.state
        if self.state:
            if score < 2 or score > 3:
                self.new_state = 0
        elif score == 3:
            self.new_state = 1

    def update_state(self):
        """Set the state of the cell to the new calculated state"""
        self.state = self.new_state
        
    def get_state(self):
        return self.state


class Grid:
    """
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
    1. Create a 3x3 grid and run 5 iterations. Display results:
    
        g = Grid([[0, 1, 0], [1, 0, 0], [0, 0, 0]], True)
        g.iterate(5)

    """
    def __init__(self, grid=[], debug=False):
        if not grid:
            if debug:
                print "No grid was provided"
            return

        self.n = len(grid)
        
        # Validate we have a square matrix
        for row in grid:
            if len(row) != self.n:
                if debug:
                    print "Matrix has to be size n*n"
                return

        self.original_grid = grid
        self.debug = debug
        
        # Initialize the grid
        # Create empty grid
        self._init_grid()
        
        # Construct grid
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                self._grid[r][c] = Cell(r, c, int(v))
                
        # Update grid neighbours
        self._update_cells()

        self.tick_count = 0
        
        if self.debug:
            print "Grid created: \n" + self.visual_grid
            
    def tick(self):
        """Run a single iteration on the grid"""
        # Apply rules to all cells
        for c in self.cells():
            c.run_rules()
            
        # Update each cell's new state
        for c in self.cells():
            c.update_state()
            
        self.tick_count += 1
        
        if self.debug:
            print "Iteration #%d" % self.tick_count
            print self.visual_grid

    def iterate(self, n=1):
        """Run n ticks on the grid"""
        for i in range(n):
            self.tick()
            
    @property
    def grid(self):
        """Return the grid as list of lists"""
        return [[c.state for c in row] for row in self._grid]

    @property
    def visual_grid(self):
        """Return the grid as a text matrix"""
        return '\n'.join([''.join([str(c.state) for c in row]) for row in self._grid])

    def _init_grid(self):
        """Create an empty grid"""
        self._grid = [[0 for i in range(self.n)] for j in range(self.n)]
        
    def _update_cells(self):
        """Create a list of neigbours to each cell"""
        for c in self.cells():
            c.make_neighbour_list(self._grid)
            
    def cells(self):
        """A simple iterator that return all the cells"""
        for row in range(self.n):
            for col in range(self.n):
                yield self._grid[row][col]
                
def main():
    print "Usage:"
    print "g = Grid(grid, [debug=False])"
    print "g.iterate(n)"
    print "\nExample:"
    print "from gol import Grid"
    print "g = Grid([[0, 1, 0], [1, 0, 0], [0, 0, 0]], True)"
    print "g.iterate(5)"
        
if __name__ == '__main__':
    main()
    
