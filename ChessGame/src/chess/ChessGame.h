#ifndef CHESS_GAME_H
#define CHESS_GAME_H

#include <string>

const int BOARD_SIZE = 8;

class ChessGame {
private:
    char board[BOARD_SIZE][BOARD_SIZE]; // Chessboard representation
    char currentPlayer;                // 'w' for White, 'b' for Black

public:
    ChessGame();                       // Constructor
    void resetBoard();                 // Resets the board to the starting position
    void printBoard() const;           // Prints the board to the console
    bool isValidMove(int startX, int startY, int endX, int endY) const; // Checks if a move is valid
    void makeMove(int startX, int startY, int endX, int endY);          // Executes a move
    bool isWithinBounds(int x, int y) const; // Checks if a position is within bounds
    const char(&getBoard() const)[BOARD_SIZE][BOARD_SIZE]; // Returns the board state
};

#endif
