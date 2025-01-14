#ifndef UTILS_H
#define UTILS_H

#include <cctype>

class Utils {
public:
    // Maps a chess piece character to its index in the sprite sheet
    static int getPieceIndex(char piece) {
        piece = std::tolower(piece);
        switch (piece) {
            case 'p': return 5;  // Pawn
            case 'r': return 4;  // Rook
            case 'n': return 3;  // Knight
            case 'b': return 2;  // Bishop
            case 'q': return 1;  // Queen
            case 'k': return 0;  // King
            default: return -1;
        }
    }
};

#endif
