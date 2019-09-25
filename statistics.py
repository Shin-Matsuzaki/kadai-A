def sum_calc(data):
    sum = 0
    for num in data:
        sum += num
    return sum


def max(data):
    max = 0
    for num in data:
        if num > max:
            max = num
    return max


def min(data):
    min = data[0]
    for num in data:
        if num < min:
            min = num
    return min


def ave(data):
    return sum_calc(data) / len(data)


def main():
    in_data = input('データを入力してください(スペース区切り) >')
    data_list = list(map(int, in_data.split(' ')))
    print(f'合計値：{sum_calc(data_list)}')
    print(f'最大値：{max(data_list)}')
    print(f'最小値：{min(data_list)}')
    print(f'平均値：{ave(data_list)}')


if __name__ == "__main__":
    main()
