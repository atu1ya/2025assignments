package game;

import java.util.*;

/**
 * Implementation of Game interface that manages a connect-4 style game
 * where players aim to create paths across the grid.
 */
public class GameImpl implements Game {
    private final int size;
    private final GridImpl grid;
    private PieceColour currentPlayer;
    private boolean over;
    private PieceColour winner;

    /**
     * Constructs a game with the given grid size.
     * 
     * @param size The size of the grid (must be at least 4)
     * @throws IllegalArgumentException if size is less than 4
     */
    public GameImpl(int size) {
        if (size < 4) {
            throw new IllegalArgumentException("Size must be at least 4");
        }
        this.size = size;
        this.grid = new GridImpl(size);
        this.currentPlayer = PieceColour.WHITE;
        this.over = false;
        this.winner = PieceColour.NONE;
    }

    /**
     * Copy constructor for creating a deep copy of the game state.
     */
    private GameImpl(int size, GridImpl grid, PieceColour currentPlayer, boolean over, PieceColour winner) {
        this.size = size;
        this.grid = (GridImpl) grid.copy();
        this.currentPlayer = currentPlayer;
        this.over = over;
        this.winner = winner;
    }

    @Override
    public boolean isOver() {
        if (!over) updateGameStatus();
        return over;
    }

    @Override
    public PieceColour winner() {
        if (!over) updateGameStatus();
        return winner;
    }

    @Override
    public PieceColour currentPlayer() {
        return currentPlayer;
    }

    /**
     * Returns all valid moves for the current player.
     * If the game is over, returns an empty collection.
     * 
     * @return An unmodifiable collection of valid moves
     */
    @Override
    public Collection<Move> getMoves() {
        List<Move> moves = new ArrayList<>();
        if (over) return Collections.unmodifiableList(moves);
        
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                if (grid.getPiece(r, c) == PieceColour.NONE) {
                    moves.add(new MoveImpl(r, c));
                }
            }
        }
        return Collections.unmodifiableList(moves);
    }

    /**
     * Executes a move for the current player and switches to the other player.
     * 
     * @param move The move to execute
     * @throws IllegalArgumentException if the move is null, out of bounds, or targets an occupied cell
     */
    @Override
    public void makeMove(Move move) {
        if (move == null) {
            throw new IllegalArgumentException("Move cannot be null");
        }
        int r = move.getRow(), c = move.getCol();
        if (r < 0 || r >= size || c < 0 || c >= size) {
            throw new IllegalArgumentException("Move coordinates out of bounds");
        }
        if (grid.getPiece(r, c) != PieceColour.NONE) {
            throw new IllegalArgumentException("Cell already occupied");
        }
        grid.setPiece(r, c, currentPlayer);
        currentPlayer = (currentPlayer == PieceColour.WHITE) ? PieceColour.BLACK : PieceColour.WHITE;
        // Reset game status to be recalculated on next status check
        over = false;
        winner = PieceColour.NONE;
    }

    @Override
    public Grid getGrid() {
        return grid.copy();
    }

    @Override
    public Game copy() {
        return new GameImpl(size, grid, currentPlayer, over, winner);
    }

    /**
     * Updates the game status by checking for win conditions or a draw.
     * Sets the 'over' and 'winner' fields accordingly.
     */
    private void updateGameStatus() {
        if (over) return;
        
        // Check for winning paths
        if (PathFinder.topToBottom(grid, PieceColour.WHITE) || PathFinder.leftToRight(grid, PieceColour.WHITE)) {
            over = true;
            winner = PieceColour.WHITE;
        } else if (PathFinder.topToBottom(grid, PieceColour.BLACK) || PathFinder.leftToRight(grid, PieceColour.BLACK)) {
            over = true;
            winner = PieceColour.BLACK;
        } else {
            // Check for draw (no empty cells left)
            boolean anyEmpty = false;
            for (int r = 0; r < size && !anyEmpty; r++) {
                for (int c = 0; c < size; c++) {
                    if (grid.getPiece(r, c) == PieceColour.NONE) {
                        anyEmpty = true;
                        break;
                    }
                }
            }
            if (!anyEmpty) {
                over = true;
                winner = PieceColour.NONE;
            }
        }
    }
}