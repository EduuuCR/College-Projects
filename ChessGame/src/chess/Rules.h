#ifndef RULES_H
#define RULES_H

class Rules {
public:
    static bool isSamePlayerPiece(char piece, char player);   // Checks if the piece belongs to the current player
    static bool isOpponentPiece(char piece, char player);     // Checks if the piece belongs to the opponent
};

#endif
