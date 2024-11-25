# Точки и отрезки
### Описание задачи
> Допустим, вы организовываете онлайн-лотерею. 
> Для участия нужно сделать ставку на одно целое число. 
> При этом у вас есть несколько интервалов последовательных целых чисел. 
> В этом случае выигрыш участника пропорционален количеству интервалов, содержащих номер участника, минус количество интервалов, которые его не содержат. (В нашем случае для начала - подсчет только
количества интервалов, содержащих номер участника). 
>> Вам нужен эффективный
алгоритм для расчета выигрышей для всех участников. Наивный способ сделать
это - просто просканировать для всех участников список всех интевалов. 
> >>Однако ваша лотерея очень популярна: у вас тысячи участников и тысячи интервалов. По
этой причине вы не можете позволить себе медленный наивный алгоритм.

>#### Цель. Вам дается набор точек и набор отрезков. Цель состоит в том, чтобы вычислить для каждой точки количество отрезков, содержащих эту точку

### Формат входного файла (input.txt). 
> - Первая строка содержит два неотрицательных целых числа s и p. s - количество отрезков, p - количество
точек. 
> - Следующие s строк содержат 2 целых числа ai, bi, которые определяют i-ый отрезок [ai, bi]. 
> - Последняя строка определяет p целых чисел - точек
x1, x2, ..., xp. 
> - Ограничения: 1 ≤ s, p ≤ 50000; −108 ≤ ai ≤ bi ≤ 108 для
всех 0 ≤ i < s; −108 ≤ xi ≤ 108 для всех 0 ≤ j < p.

### Формат выходного файла (output.txt).
> - Выведите p неотрицательных целых чисел k0, k1..., kp−1, где ki - это число отрезков, которые содержат xi
>> То есть, ki = |j : aj ≤ xi ≤ bj |.

## Примеры
### Пример 1
`input.txt`  
2 3  
0 5  
7 10  
1 6 11  
`output.txt`  
1 0 0

> Здесь, у нас есть 2 отрезка и 2 точки. Первая точка принадлежит интервалу
> [0, 5], остальные точки не принадлежат ни одному из данных интервалов.

### Пример 2.
`input.txt`  
1 3  
-10 10  
-100 100 0  
`output.txt`  
0 0 1

### Пример 3.
`input.txt`  
3 2  
0 5  
-3 2  
7 10  
1 6  
`output.txt`  
2 0