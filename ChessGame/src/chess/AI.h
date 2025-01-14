#ifndef AI_H
#define AI_H

#include "ChessGame.h"

struct Move {
    int startX, startY, endX, endY;
};

class AI {
private:
    char aiPlayer;         // AI's player ('w' or 'b')
    char opponentPlayer;   // Opponent's player
    int evaluateBoard(const char board[BOARD_SIZE][BOARD_SIZE]);
    int getPieceValue(char piece);
    int minimax(ChessGame& game, int depth, int alpha, int beta, bool isMaximizing);

public:
    AI(char aiPlayer);              // Constructor
    Move findBestMove(ChessGame& game); // Finds the best move using Minimax
};

#endif
