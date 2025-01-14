#include "AI.h"
#include "Rules.h"
#include <limits>
#include <vector>

AI::AI(char aiPlayer) : aiPlayer(aiPlayer), opponentPlayer(aiPlayer == 'w' ? 'b' : 'w') {}

int AI::evaluateBoard(const char board[BOARD_SIZE][BOARD_SIZE]) {
    int score = 0;
    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            char piece = board[i][j];
            score += getPieceValue(piece);
        }
    }
    return aiPlayer == 'w' ? score : -score;
}

int AI::getPieceValue(char piece) {
    switch (tolower(piece)) {
        case 'p': return 10;   // Pawn
        case 'n': return 30;   // Knight
        case 'b': return 30;   // Bishop
        case 'r': return 50;   // Rook
        case 'q': return 90;   // Queen
        case 'k': return 900;  // King
        default: return 0;
    }
}

Move AI::findBestMove(ChessGame& game) {
    const char(&board)[BOARD_SIZE][BOARD_SIZE] = game.getBoard();
    int bestScore = std::numeric_limits<int>::min();
    Move bestMove = {0, 0, 0, 0};

    for (int startY = 0; startY < BOARD_SIZE; ++startY) {
        for (int startX = 0; startX < BOARD_SIZE; ++startX) {
            if (!Rules::isSamePlayerPiece(board[startY][startX], aiPlayer)) continue;

            for (int endY = 0; endY < BOARD_SIZE; ++endY) {
                for (int endX = 0; endX < BOARD_SIZE; ++endX) {
                    if (!game.isValidMove(startX, startY, endX, endY)) continue;

                    ChessGame copy = game;
                    copy.makeMove(startX, startY, endX, endY);
                    int score = minimax(copy, 3, std::numeric_limits<int>::min(), std::numeric_limits<int>::max(), false);

                    if (score > bestScore) {
                        bestScore = score;
                        bestMove = {startX, startY, endX, endY};
                    }
                }
            }
        }
    }
    return bestMove;
}

int AI::minimax(ChessGame& game, int depth, int alpha, int beta, bool isMaximizing) {
    if (depth == 0) {
        return evaluateBoard(game.getBoard());
    }

    const char(&board)[BOARD_SIZE][BOARD_SIZE] = game.getBoard();
    int bestScore = isMaximizing ? std::numeric_limits<int>::min() : std::numeric_limits<int>::max();

    for (int startY = 0; startY < BOARD_SIZE; ++startY) {
        for (int startX = 0; startX < BOARD_SIZE; ++startX) {
            if (isMaximizing && !Rules::isSamePlayerPiece(board[startY][startX], aiPlayer)) continue;
            if (!isMaximizing && !Rules::isSamePlayerPiece(board[startY][startX], opponentPlayer)) continue;

            for (int endY = 0; endY < BOARD_SIZE; ++endY) {
                for (int endX = 0; endX < BOARD_SIZE; ++endX) {
                    if (!game.isValidMove(startX, startY, endX, endY)) continue;

                    ChessGame copy = game;
                    copy.makeMove(startX, startY, endX, endY);
                    int score = minimax(copy, depth - 1, alpha, beta, !isMaximizing);

                    if (isMaximizing) {
                        bestScore = std::max(bestScore, score);
                        alpha = std::max(alpha, bestScore);
                    } else {
                        bestScore = std::min(bestScore, score);
                        beta = std::min(beta, bestScore);
                    }

                    if (beta <= alpha) break;
                }
            }
        }
    }
    return bestScore;
}
