package game;

/**
 * Implementation of Move interface representing a position on the game grid.
 * Provides immutable row and column coordinates.
 */
public class MoveImpl implements Move {
    private final int row, col;

    /**
     * Constructs a move with the specified row and column coordinates.
     * 
     * @param row The row coordinate
     * @param col The column coordinate
     * @throws IllegalArgumentException if coordinates are negative
     */
    public MoveImpl(int row, int col) {
        if (row < 0 || col < 0) {
            throw new IllegalArgumentException("Row and column must be non-negative");
        }
        this.row = row;
        this.col = col;
    }

    @Override
    public int getRow() { return row; }

    @Override
    public int getCol() { return col; }

    @Override
    public String toString() {
        return "(" + row + "," + col + ")";
    }
}