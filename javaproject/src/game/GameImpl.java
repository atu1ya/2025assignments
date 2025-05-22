package game;

import java.util.*;

public class GameImpl implements Game {
    private final int size;
    private final GridImpl grid;
    private PieceColour currentPlayer;
    private boolean over;
    private PieceColour winner;

    public GameImpl(int size) {
        if (size <= 0) {
        throw new IllegalArgumentException("Size must be positive");
        }
        this.size = size;
        this.grid = new GridImpl(size);
        this.currentPlayer = PieceColour.WHITE;
        this.over = false;
        this.winner = PieceColour.NONE;
    }

    private GameImpl(int size, GridImpl grid, PieceColour currentPlayer, boolean over, PieceColour winner) {
        this.size = size;
        this.grid = (GridImpl) grid.copy();
        this.currentPlayer = currentPlayer;
        this.over = over;
        this.winner = winner;
    }

    @Override
    public boolean isOver() {
        updateGameStatus();
        return over;
    }

    @Override
    public PieceColour winner() {
        updateGameStatus();
        return winner;
    }

    @Override
    public PieceColour currentPlayer() {
        return currentPlayer;
    }

    @Override
    public Collection<Move> getMoves() {
        List<Move> moves = new ArrayList<>();
        if (isOver()) return moves;
        for (int r = 0; r < size; r++)
            for (int c = 0; c < size; c++)
                if (grid.getPiece(r, c) == PieceColour.NONE)
                    moves.add(new MoveImpl(r, c));
        return moves;
    }

    @Override
    public void makeMove(Move move) {
        int r = move.getRow(), c = move.getCol();
        if (r < 0 || r >= size || c < 0 || c >= size)
            throw new IllegalArgumentException();
        if (grid.getPiece(r, c) != PieceColour.NONE)
            throw new IllegalArgumentException();
        grid.setPiece(r, c, currentPlayer);
        currentPlayer = (currentPlayer == PieceColour.WHITE) ? PieceColour.BLACK : PieceColour.WHITE;
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

    private void updateGameStatus() {
        if (over) return;
        if (PathFinder.topToBottom(grid, PieceColour.WHITE) || PathFinder.leftToRight(grid, PieceColour.WHITE)) {
            over = true;
            winner = PieceColour.WHITE;
    }
        else if (PathFinder.topToBottom(grid, PieceColour.BLACK) || PathFinder.leftToRight(grid, PieceColour.BLACK)) {
            over = true;
            winner = PieceColour.BLACK;
    }
        else if (getMoves().isEmpty()) {
            over = true;
            winner = PieceColour.NONE;
    }
}
}