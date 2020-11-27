# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle


result_count = []
for index in count(5):
    result_count.append(index)
    if index >= 9:
        break
print(result_count)

result_cycle = []
cycle_len = len(result_count) * 3
for el in cycle(result_count):
    result_cycle.append(el)
    cycle_len -= 1
    if cycle_len <= 0:
        break
print(result_cycle)
