package game;

// Implementation of Grid interface
// Represents a square grid of PieceColour values
public class GridImpl implements Grid {
    private final int size;
    private final PieceColour[][] board;

    // Construct new empty grid of required size
    public GridImpl(int size) {
        this.size = size;
        this.board = new PieceColour[size][size];
        for (int r = 0; r < size; r++)
            for (int c = 0; c < size; c++)
                board[r][c] = PieceColour.NONE;
    }

    // Copy constructor for deep copying the grid
    private GridImpl(int size, PieceColour[][] board) {
        this.size = size;
        this.board = new PieceColour[size][size];
        for (int r = 0; r < size; r++)
            System.arraycopy(board[r], 0, this.board[r], 0, size);
    }

    @Override
    public int getSize() { return size; }

    @Override
    public PieceColour getPiece(int row, int col) {
        if (row < 0 || row >= size || col < 0 || col >= size)
            throw new IllegalArgumentException();
        return board[row][col];
    }

    @Override
    public void setPiece(int row, int col, PieceColour piece) {
        if (row < 0 || row >= size || col < 0 || col >= size)
            throw new IllegalArgumentException();
        if (piece == null)
            throw new IllegalArgumentException();
        board[row][col] = piece;
    }

    @Override
    public Grid copy() {
        return new GridImpl(size, board);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                PieceColour p = board[r][c];
                if (p == PieceColour.BLACK) sb.append('B');
                else if (p == PieceColour.WHITE) sb.append('W');
                else sb.append('.');
            }
            sb.append('\n');
        }
        return sb.toString();
    }
}