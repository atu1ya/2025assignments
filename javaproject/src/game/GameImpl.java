package game;

import java.util.*;

/**
 * Implementation of the Game interface for a two-player connection game.
 * Handles game state, move validation, and win/draw detection.
 */
public class GameImpl implements Game {
    private final int size;
    private final GridImpl grid;
    private PieceColour currentPlayer;
    private boolean over;
    private PieceColour winner;

    /**
     * Constructs a new game with the given grid size.
     * Throws IllegalArgumentException if size is less than 4.
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
     * Copy constructor for deep copying the game state.
     */
    private GameImpl(int size, GridImpl grid, PieceColour currentPlayer, boolean over, PieceColour winner) {
        this.size = size;
        this.grid = (GridImpl) grid.copy();
        this.currentPlayer = currentPlayer;
        this.over = over;
        this.winner = winner;
    }

    /**
     * Returns true if the game is over (win or draw).
     * Updates the game status if necessary.
     */
    @Override
    public boolean isOver() {
        if (!over) updateGameStatus();
        return over;
    }

    /**
     * Returns the winner of the game, or PieceColour.NONE if there is no winner.
     * Updates the game status if necessary.
     */
    @Override
    public PieceColour winner() {
        if (!over) updateGameStatus();
        return winner;
    }

    /**
     * Returns the current player.
     * If the game is over, the result is undefined.
     */
    @Override
    public PieceColour currentPlayer() {
        return currentPlayer;
    }

    /**
     * Returns a collection of all valid moves for the current player.
     * If the game is over, returns an empty collection.
     */
    @Override
    public Collection<Move> getMoves() {
        List<Move> moves = new ArrayList<>();
        if (over) return moves;
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                if (grid.getPiece(r, c) == PieceColour.NONE) {
                    moves.add(new MoveImpl(r, c));
                }
            }
        }
        return moves;
    }

    /**
     * Executes a move for the current player.
     * Throws IllegalArgumentException if the move is invalid or null.
     * Resets the game status so it will be recalculated on the next query.
     */
    @Override
    public void makeMove(Move move) {
        if (move == null) {
            throw new IllegalArgumentException();
        }
        int r = move.getRow(), c = move.getCol();
        if (r < 0 || r >= size || c < 0 || c >= size) {
            throw new IllegalArgumentException();
        }
        if (grid.getPiece(r, c) != PieceColour.NONE) {
            throw new IllegalArgumentException();
        }
        grid.setPiece(r, c, currentPlayer);
        currentPlayer = (currentPlayer == PieceColour.WHITE) ? PieceColour.BLACK : PieceColour.WHITE;
        // Reset game status so it will be recalculated on demand
        over = false;
        winner = PieceColour.NONE;
    }

    /**
     * Returns a deep copy of the grid.
     */
    @Override
    public Grid getGrid() {
        return grid.copy();
    }

    /**
     * Returns a deep copy of the game.
     */
    @Override
    public Game copy() {
        return new GameImpl(size, grid, currentPlayer, over, winner);
    }

    /**
     * Updates the game status (over/winner) if not already over.
     * Uses PathFinder to check for a win, otherwise checks for draw.
     */
    private void updateGameStatus() {
        if (over) return;
        if (PathFinder.topToBottom(grid, PieceColour.WHITE) || PathFinder.leftToRight(grid, PieceColour.WHITE)) {
            over = true;
            winner = PieceColour.WHITE;
        } else if (PathFinder.topToBottom(grid, PieceColour.BLACK) || PathFinder.leftToRight(grid, PieceColour.BLACK)) {
            over = true;
            winner = PieceColour.BLACK;
        } else {
            // Check for draw: if no empty cells remain, it's a draw
            boolean anyEmpty = false;
            for (int r = 0; r < size; r++) {
                for (int c = 0; c < size; c++) {
                    if (grid.getPiece(r, c) == PieceColour.NONE) {
                        anyEmpty = true;
                        break;
                    }
                }
                if (anyEmpty) break;
            }
            if (!anyEmpty) {
                over = true;
                winner = PieceColour.NONE;
            }
        }
    }
}