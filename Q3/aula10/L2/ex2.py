def heap(H: [int]) -> bool:
    H = ["0"] + H
    for a in reversed(range(2, len(H))):
        print(H[a//2], H[a])
        if H[a//2] < H[a]: return False
    return True 