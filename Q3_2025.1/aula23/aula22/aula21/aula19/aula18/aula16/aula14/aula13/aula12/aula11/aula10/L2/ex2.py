def heap (H: [int]) -> bool:
    H = [""] + H
    for a in reversed (range (2, len (H))):
        if H[a//2] < H[a]: return False
    return True