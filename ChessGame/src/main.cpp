#include <iostream>
#include "ChessGame.h"
#include "ChessGUI.h"

int main() {
    try {
        // Create a ChessGame instance
        ChessGame game;

        // Create a ChessGUI instance and link it with the ChessGame
        ChessGUI gui(game);

        // Run the game loop
        gui.run();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
