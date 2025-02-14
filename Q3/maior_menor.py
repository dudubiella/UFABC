def main(list):
    max, min = list[0], list[0]
    for a in list[1:]:
        if a > max:
            max = a
        if a < min:
            min = a
    print(min, max)
    return

if __name__ == '__main__':
    main(input('envie os 3 valores separados por espaços\n').split())