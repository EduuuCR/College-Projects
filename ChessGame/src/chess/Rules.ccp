#include "Rules.h"
#include <cctype>

bool Rules::isSamePlayerPiece(char piece, char player) {
    if (piece == ' ') return false;
    return (player == 'w' && isupper(piece)) || (player == 'b' && islower(piece));
}

bool Rules::isOpponentPiece(char piece, char player) {
    if (piece == ' ') return false;
    return (player == 'w' && islower(piece)) || (player == 'b' && isupper(piece));
}
