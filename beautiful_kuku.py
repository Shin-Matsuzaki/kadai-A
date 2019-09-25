def lenget(num):
    return len(str(num))


def main():
    anyrow = int(input('行数を入力してください：'))
    anycol = int(input('列数を入力してください：'))

    for row in range(1, anyrow + 1):
        for col in range(1, anycol + 1):
            print(f'{row:{lenget(anyrow)}} × {col:{lenget(anycol)}} = {row * col:{lenget(anyrow*anycol)}} |', end=' ')
        print()


if __name__ == "__main__":
    main()