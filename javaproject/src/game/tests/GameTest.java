package game.tests;

import game.*;

// Tests for Game implementation 
// Testing grid sizes, validity of player moves and win/draw logic

public class GameTest extends Test {
    public static void main(String[] args) {
        // Test: constructing a game with size 0 should throw IllegalArgumentException
        boolean failed = false;
        try {
            new GameImpl(0);
            failed = true;
        } catch (IllegalArgumentException e) {}
        if (failed) System.out.println("Expected exception for size 0. ERROR");

        // Test: constructing a game with valid size (5) should not throw
        failed = false;
        try {
            new GameImpl(5);
        } catch (IllegalArgumentException e) {
            failed = true;
        }
        if (failed) System.out.println("Unexpected exception for valid size 5. ERROR");

        // Test: constructing a game with size less than 4 should throw
        for (int i = 0; i < 4; i++) {
            failed = false;
            try {
                new GameImpl(i);
                failed = true;
            } catch (IllegalArgumentException e) {}
            if (failed) System.out.println("Expected exception for size " + i + ". ERROR");
        }

        // Test: grid is square, getSize() returns correct value, and grid is empty at start
        for (int size = 4; size <= 10; size++) {
            Game game = new GameImpl(size);
            Grid grid = game.getGrid();
            if (size != grid.getSize()) {
                System.out.println("Expected grid size " + size + " but got " + grid.getSize() + ". ERROR");
            } else {
                boolean allNone = true;
                for (int r = 0; r < size; r++)
                    for (int c = 0; c < size; c++)
                        allNone &= (grid.getPiece(r, c) == PieceColour.NONE);
                if (!allNone) System.out.println("Expected all grid pieces to be NONE. ERROR");
            }

            // Test: accessing grid out-of-bounds should throw
            boolean outOfBounds = false;
            try { grid.getPiece(size, 0); } catch (IllegalArgumentException e) { outOfBounds = true; }
            if (!outOfBounds) System.out.println("Expected exception for out-of-bounds getPiece(size, 0). ERROR");
            outOfBounds = false;
            try { grid.getPiece(0, size); } catch (IllegalArgumentException e) { outOfBounds = true; }
            if (!outOfBounds) System.out.println("Expected exception for out-of-bounds getPiece(0, size). ERROR");
        }

        // Test: initial player is WHITE and grid is empty
        Game game = new GameImpl(4);
        if (!PieceColour.WHITE.equals(game.currentPlayer())) System.out.println("Expected WHITE as initial player. ERROR");
        boolean allNone = true;
        for (int r = 0; r < 4; r++)
            for (int c = 0; c < 4; c++)
                allNone &= (game.getGrid().getPiece(r, c) == PieceColour.NONE);
        if (!allNone) System.out.println("Expected all grid pieces to be NONE at start. ERROR");

        // Test: making a valid move updates grid and switches player
        game = new GameImpl(4);
        game.makeMove(new MoveImpl(0, 0));
        if (!PieceColour.BLACK.equals(game.currentPlayer())) System.out.println("Expected BLACK after first move. ERROR");
        if (!PieceColour.WHITE.equals(game.getGrid().getPiece(0, 0))) System.out.println("Expected WHITE at (0,0) after first move. ERROR");
        if (15 != game.getMoves().size()) System.out.println("Expected 15 moves after first move. ERROR");

        // Test: making a move on an occupied cell should throw
        failed = false;
        try { game.makeMove(new MoveImpl(0, 0)); failed = true; } catch (IllegalArgumentException e) {}
        if (failed) System.out.println("Expected exception for move on occupied cell. ERROR");

        // Test: making a move out of bounds should throw
        failed = false;
        try { game.makeMove(new MoveImpl(-1, 0)); failed = true; } catch (IllegalArgumentException e) {}
        if (failed) System.out.println("Expected exception for move out of bounds (-1,0). ERROR");
        failed = false;
        try { game.makeMove(new MoveImpl(0, 4)); failed = true; } catch (IllegalArgumentException e) {}
        if (failed) System.out.println("Expected exception for move out of bounds (0,4). ERROR");

        // Test: getMoves returns all and only valid moves
        game = new GameImpl(4);
        if (16 != game.getMoves().size()) System.out.println("Expected 16 moves at start. ERROR");
        game.makeMove(new MoveImpl(0, 0));
        if (15 != game.getMoves().size()) System.out.println("Expected 15 moves after one move. ERROR");

        // Test: win detection (left-to-right for WHITE)
        game = new GameImpl(4);
        game.makeMove(new MoveImpl(0, 0)); // W
        game.makeMove(new MoveImpl(1, 0)); // B
        game.makeMove(new MoveImpl(0, 1)); // W
        game.makeMove(new MoveImpl(1, 1)); // B
        game.makeMove(new MoveImpl(0, 2)); // W
        game.makeMove(new MoveImpl(1, 2)); // B
        game.makeMove(new MoveImpl(0, 3)); // W wins
        if (!game.isOver()) System.out.println("Expected game to be over after win. ERROR");
        if (!PieceColour.WHITE.equals(game.winner())) System.out.println("Expected WHITE as winner. ERROR");
        if (0 != game.getMoves().size()) System.out.println("Expected 0 moves after win. ERROR");

        // Test: draw detection (no winner, board full)
        game = new GameImpl(4);
        int[][] moves = {
            {0,0},{0,1},{0,2},{0,3},
            {1,1},{1,0},{1,3},{1,2},
            {2,2},{2,3},{2,0},{2,1},
            {3,3},{3,2},{3,1},{3,0}
        };
        for (int i = 0; i < moves.length; i++) {
            game.makeMove(new MoveImpl(moves[i][0], moves[i][1]));
        }
        if (!game.isOver()) System.out.println("Expected game to be over after draw. ERROR");
        if (!PieceColour.NONE.equals(game.winner())) System.out.println("Expected NONE as winner for draw. ERROR");
        if (0 != game.getMoves().size()) System.out.println("Expected 0 moves after draw. ERROR");

        // Test: moves after game over should not change state (should throw)
        failed = false;
        try { game.makeMove(new MoveImpl(0, 0)); failed = true; } catch (Exception e) {}
        if (failed) System.out.println("Expected exception for move after game over. ERROR");

        // Test: copy() returns a deep copy (modifications to copy do not affect original)
        game = new GameImpl(4);
        game.makeMove(new MoveImpl(0, 0));
        Game copy = game.copy();
        if (!game.currentPlayer().equals(copy.currentPlayer())) System.out.println("Expected currentPlayer to match in copy. ERROR");
        if (game.isOver() != copy.isOver()) System.out.println("Expected isOver to match in copy. ERROR");
        if (!game.winner().equals(copy.winner())) System.out.println("Expected winner to match in copy. ERROR");
        if (game.getMoves().size() != copy.getMoves().size()) System.out.println("Expected moves size to match in copy. ERROR");
        if (!game.getGrid().getPiece(0, 0).equals(copy.getGrid().getPiece(0, 0))) System.out.println("Expected grid piece (0,0) to match in copy. ERROR");
        copy.makeMove(new MoveImpl(0, 1));
        if (!PieceColour.NONE.equals(game.getGrid().getPiece(0, 1))) System.out.println("Expected original grid (0,1) to remain NONE after copy move. ERROR");

        // Test: getGrid() returns a deep copy (modifications to returned grid do not affect game)
        Grid g1 = game.getGrid();
        g1.setPiece(1, 1, PieceColour.BLACK);
        if (!PieceColour.NONE.equals(game.getGrid().getPiece(1, 1))) System.out.println("Expected original grid (1,1) to remain NONE after modifying copy. ERROR");

        // Test: diagonal does not win (only horizontal/vertical wins are valid)
        game = new GameImpl(4);
        game.makeMove(new MoveImpl(0, 0)); // W
        game.makeMove(new MoveImpl(0, 1)); // B
        game.makeMove(new MoveImpl(1, 1)); // W
        game.makeMove(new MoveImpl(0, 2)); // B
        game.makeMove(new MoveImpl(2, 2)); // W
        game.makeMove(new MoveImpl(0, 3)); // B
        game.makeMove(new MoveImpl(3, 3)); // W
        if (game.isOver()) System.out.println("Expected game not to be over for diagonal. ERROR");
        if (!PieceColour.NONE.equals(game.winner())) System.out.println("Expected NONE as winner for diagonal. ERROR");

        // Test: setting a piece to null should throw 
        failed = false;
        Grid grid = new GameImpl(4).getGrid();
        try { grid.setPiece(0, 0, null); failed = true; } catch (IllegalArgumentException e) {}
        if (failed) System.out.println("Expected exception for setting piece to null. ERROR");

        // Test: makeMove(null) should throw
        failed = false;
        try { game.makeMove(null); failed = true; } catch (IllegalArgumentException e) {}
        if (failed) System.out.println("Expected exception for makeMove(null). ERROR");

        // Test: MoveImpl with invalid coordinates should throw
        failed = false;
        try { new MoveImpl(-1, 0); } catch (IllegalArgumentException e) { failed = true; }
        if (!failed) System.out.println("Expected exception for MoveImpl(-1, 0). ERROR");

        // Test: getMoves() returns unmodifiable list
        game = new GameImpl(4);
        failed = false;
        try { game.getMoves().clear(); } catch (UnsupportedOperationException e) { failed = true; }
        if (!failed) System.out.println("Expected exception for modifying unmodifiable moves list. ERROR");

        checkAllTestsPassed();
    }
}