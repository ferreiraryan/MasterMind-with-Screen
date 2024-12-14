import random
from typing import List, Tuple, Dict

COLORS = ["R", "G", "B", "Y", "W","O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
        
    return code

def check_code(guess: List[str], real_code: List[str]) -> Tuple[int, Dict[str, int]]:
    """Check the guessed code against the real code.
    
    Returns:
        - Number of correct colors in the correct position.
        - Remaining counts of colors in the real code.
    """
    color_counts = {color: real_code.count(color) for color in COLORS}
    correct_pos = sum(1 for g, r in zip(guess, real_code) if g == r)

    # Reduce counts for correctly guessed positions
    for g, r in zip(guess, real_code):
        if g == r:
            color_counts[g] -= 1

    return correct_pos, color_counts


