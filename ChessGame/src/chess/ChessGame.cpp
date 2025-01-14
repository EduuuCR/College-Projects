#include "ChessGame.h"
#include <iostream>
#include <stdexcept>

// Constructor: Initialize the chessboard with the standard starting position
ChessGame::ChessGame() {
    resetBoard();
}

// Resets the board to the initial chess position
void ChessGame::resetBoard() {
    const std::string initialBoard =
        "rnbqkbnr"
        "pppppppp"
        "        "
        "        "
        "        "
        "        "
        "PPPPPPPP"
        "RNBQKBNR";

    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            board[i][j] = initialBoard[i * BOARD_SIZE + j];
        }
    }

    currentPlayer = 'w'; // White starts
}

// Prints the board to the console (for debugging purposes)
void ChessGame::printBoard() const {
    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            std::cout << board[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

// Validates a move based on chess rules
bool ChessGame::isValidMove(int startX, int startY, int endX, int endY) const {
    // Ensure start and end positions are within bounds
    if (!isWithinBounds(startX, startY) || !isWithinBounds(endX, endY)) {
        return false;
    }

    char piece = board[startY][startX];
    char target = board[endY][endX];

    // Ensure there is a piece at the start position
    if (piece == ' ') {
        return false;
    }

    // Ensure the piece belongs to the current player
    if ((currentPlayer == 'w' && islower(piece)) || (currentPlayer == 'b' && isupper(piece))) {
        return false;
    }

    // Ensure the target square is not occupied by the same player's piece
    if ((currentPlayer == 'w' && isupper(target)) || (currentPlayer == 'b' && islower(target))) {
        return false;
    }

    // Additional piece-specific movement logic will go here
    return true;
}

// Executes a move if valid
void ChessGame::makeMove(int startX, int startY, int endX, int endY) {
    if (!isValidMove(startX, startY, endX, endY)) {
        throw std::invalid_argument("Invalid move!");
    }

    // Move the piece
    board[endY][endX] = board[startY][startX];
    board[startY][startX] = ' ';

    // Switch the current player
    currentPlayer = (currentPlayer == 'w') ? 'b' : 'w';
}

// Checks if a given position is within the chessboard
bool ChessGame::isWithinBounds(int x, int y) const {
    return x >= 0 && x < BOARD_SIZE && y >= 0 && y < BOARD_SIZE;
}

// Returns the current board state
const char(&ChessGame::getBoard() const)[BOARD_SIZE][BOARD_SIZE] {
    return board;
}
