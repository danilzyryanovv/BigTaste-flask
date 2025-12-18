import matplotlib.pyplot as plt

data = []
with open("/Users/danil/PycharmProjects/learnpython/true.txt", "r", encoding="utf-8") as f:
    f.readline()
    for l in f:
        arr = l.strip().split(",")
        if (arr[0] == "Средняя пенсия" and
                arr[1] == "Забайкальский край" and
                arr[2] >= "2018-01-01" and
                arr[2] <= "2018-12-31"):
            data.append(arr)

x = []
y = []
data.sort(key=lambda x: x[2])
res = 0

for i in data:
    res += int(i[3])
    date = i[2].split("-")
    x.append(int(date[1]))
    y.append(int(i[3]))

if data:
    average = res / len(data)
    print(f"Средняя пенсия: {average:.2f}")
    print(f"Количество записей: {len(data)}")

    plt.plot(x, y, 'o-')
    plt.title("График изменения пенсии в Забайкальском крае за 2018 год")
    plt.xlabel("Месяц")
    plt.ylabel("Пенсия, руб.")
    plt.grid(True)
    plt.xticks(range(1, 13))
    plt.show()
else:
    print("Нет данных")
