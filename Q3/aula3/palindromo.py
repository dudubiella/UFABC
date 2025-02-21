def palimdromo (n: int) -> bool:
    save = n; m = n % 10; n //= 10
    while(n != 0):
        m = m * 10 + n % 10; n //= 10
    return save == m

if __name__ == "__main__":
    print(palimdromo(int(input("Digite o número para testar se é palíndromo:\n"))))