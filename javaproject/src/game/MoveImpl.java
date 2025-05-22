package game;

// Implementation of Move interface
public class MoveImpl implements Move {
    private final int row, col;

    // Construct move with given row and column
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