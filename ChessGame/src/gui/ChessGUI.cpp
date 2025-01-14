#include "ChessGUI.h"
#include "Utils.h"
#include <SFML/Graphics.hpp>
#include <iostream>

ChessGUI::ChessGUI(ChessGame& game) : game(game) {
    if (!boardTexture.loadFromFile("assets/board.png") || !piecesTexture.loadFromFile("assets/pieces.png")) {
        throw std::runtime_error("Failed to load assets!");
    }

    boardSprite.setTexture(boardTexture);
    piecesSprite.setTexture(piecesTexture);
}

void ChessGUI::run() {
    sf::RenderWindow window(sf::VideoMode(800, 800), "Chess Game");
    sf::Vector2i selectedSquare(-1, -1);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            } else if (event.type == sf::Event::MouseButtonPressed && event.mouseButton.button == sf::Mouse::Left) {
                handleMouseClick(window, event.mouseButton.x, event.mouseButton.y, selectedSquare);
            }
        }

        window.clear();
        drawBoard(window);
        drawPieces(window);
        window.display();
    }
}

void ChessGUI::drawBoard(sf::RenderWindow& window) {
    window.draw(boardSprite);
}

void ChessGUI::drawPieces(sf::RenderWindow& window) {
    const char(&board)[BOARD_SIZE][BOARD_SIZE] = game.getBoard();

    for (int y = 0; y < BOARD_SIZE; ++y) {
        for (int x = 0; x < BOARD_SIZE; ++x) {
            char piece = board[y][x];
            if (piece == ' ') continue;

            int pieceIndex = Utils::getPieceIndex(piece);
            int pieceX = pieceIndex % 6;
            int pieceY = pieceIndex / 6;

            piecesSprite.setTextureRect(sf::IntRect(pieceX * 100, pieceY * 100, 100, 100));
            piecesSprite.setPosition(x * 100.f, y * 100.f);
            window.draw(piecesSprite);
        }
    }
}

void ChessGUI::handleMouseClick(sf::RenderWindow& window, int x, int y, sf::Vector2i& selectedSquare) {
    int gridX = x / 100;
    int gridY = y / 100;

    if (selectedSquare == sf::Vector2i(-1, -1)) {
        // First click: Select a piece
        if (game.getBoard()[gridY][gridX] != ' ') {
            selectedSquare = sf::Vector2i(gridX, gridY);
        }
    } else {
        // Second click: Attempt to move the piece
        try {
            game.makeMove(selectedSquare.x, selectedSquare.y, gridX, gridY);
        } catch (const std::exception& e) {
            std::cerr << "Invalid move: " << e.what() << std::endl;
        }
        selectedSquare = sf::Vector2i(-1, -1); // Deselect
    }
}
