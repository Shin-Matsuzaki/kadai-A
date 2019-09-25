def main():
    anyrow = int(input('行数を入力してください：')) + 1
    anycol = int(input('列数を入力してください：')) + 1

    for row in range(1, anyrow):
        for col in range(1, anycol):
            print(row * col, end=' ')
        print()


if __name__ == "__main__":
    main()
