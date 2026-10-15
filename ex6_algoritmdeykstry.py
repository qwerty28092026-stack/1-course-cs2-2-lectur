
import math

graph = {
    "Дом": {"Остановка": 5, "Парк": 12},
    "Остановка": {"Парк": 4, "Колледж": 15},
    "Парк": {"Колледж": 6},
    "Колледж": {}
}

time = {v: math.inf for v in graph}
time["Дом"] = 0

came_from = {}
done = set()

while len(done) < len(graph):
    current = None

    # Ищем ближайшую необработанную вершину
    for v in graph:
        if v in done:
            continue
        if current is None or time[v] < time[current]:
            current = v

    # Если оставшиеся вершины недостижимы
    if time[current] == math.inf:
        break

    # Проверяем соседей
    for neighbor, minutes in graph[current].items():
        if time[current] + minutes < time[neighbor]:
            time[neighbor] = time[current] + minutes
            came_from[neighbor] = current

    done.add(current)

# Время до колледжа
print("Минимальное время:", time["Колледж"], "минут")

# Восстанавливаем маршрут
route = []
current = "Колледж"

while current in came_from:
    route.append(current)
    current = came_from[current]

route.append("Дом")
route.reverse()

print("Кратчайший маршрут:", " -> ".join(route))
