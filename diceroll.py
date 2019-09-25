import random


def main():
    faces = int(input('サイコロの面の数は?:'))
    times = int(input('何回振りますか?:'))

    result = []
    for i in range(times):
        result.append(random.randint(1, faces))

    print(result)


if __name__ == "__main__":
    main()