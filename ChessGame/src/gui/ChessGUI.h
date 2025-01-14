#ifndef CHESS_GUI_H
#define CHESS_GUI_H

#include "ChessGame.h"
#include <SFML/Graphics.hpp>

class ChessGUI {
private:
    ChessGame& game;
    sf::Texture boardTexture;
    sf::Texture piecesTexture;
    sf::Sprite boardSprite;
    sf::Sprite piecesSprite;

    void drawBoard(sf::RenderWindow& window);
    void drawPieces(sf::RenderWindow& window);
    void handleMouseClick(sf::RenderWindow& window, int x, int y, sf::Vector2i& selectedSquare);

public:
    ChessGUI(ChessGame& game); // Constructor
    void run();                // Runs the game loop
};

#endif
