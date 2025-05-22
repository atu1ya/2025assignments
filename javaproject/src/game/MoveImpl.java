package game;

/**
 * Immutable implementation of the Move interface.
 * Represents a move on the grid by row and column.
 */
public class MoveImpl implements Move {
    private final int row, col;

    /**
     * Constructs a move with the given row and column.
     */
    public MoveImpl(int row, int col) {
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