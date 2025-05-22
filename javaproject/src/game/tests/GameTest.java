package game.tests;

import game.*;

public class GameTest extends Test {
    public static void main(String[] args) {
        boolean caught = false;
        try {
            new GameImpl(0);
        } catch (IllegalArgumentException e) {
            caught = true;
        }
        expect(true, caught);

        caught = false;
        try {
            new GameImpl(5);
        } catch (IllegalArgumentException e) {
            caught = true;
        }
        expect(false, caught);

        // Test for grids smaller than 4x4
        for (int i = 0; i < 4; i++) {
            boolean invalidsizecaught = false;
            try {
                new GameImpl(i);
            } catch (IllegalArgumentException e) {
                invalidsizecaught = true;
            }
            expect(true, invalidsizecaught);
        }

        // Test that the grid is always square and accessible for a range of sizes
        for (int size = 4; size <= 50; size++) { 
            Game game = new GameImpl(size);
            Grid grid = game.getGrid();
            expect(size, grid.getSize());
            boolean allAccessible = true;
            for (int r = 0; r < size; r++) {
                for (int c = 0; c < size; c++) {
                    try {
                        expect(PieceColour.NONE, grid.getPiece(r, c));
                    } catch (Exception e) {
                        allAccessible = false;
                    }
                }
    }
    expect(true, allAccessible);
}

        checkAllTestsPassed();
    }
}
