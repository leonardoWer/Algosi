# Алгоритм подсчёта количества инверсий
### Описание задачи
> Инверсией в последовательности чисел A называется такая ситуация, 
> когда i < j, а Ai > Aj . 
> Количество инверсий в последовательности в некотором роде определяет, насколько близка данная последовательность к отсортированной.
>> Например, в сортированном массиве число инверсий равно 0, а в массиве, сортированном наоборот - каждые два элемента будут составлять инверсию (всего
n(n − 1)/2).

_Дан массив целых чисел. Ваша задача — подсчитать число инверсий в нем.
Подсказка: чтобы сделать это быстрее, можно воспользоваться модификацией
сортировки слиянием_

### Формат входного файла (input.txt). 
> - В первой строке входного файла содержится число n (1 ≤ n ≤ 105) — число элементов в массиве. 
> - Во второй строке находятся n различных целых чисел, по модулю не превосходящих 109.

### Формат выходного файла (output.txt). 
> В выходной файл надо вывести число инверсий в массиве

### Ограничения
> - Ограничение по времени. 2сек.
> - Ограничение по памяти. 256 мб.

### Пример
> `input.txt`  
10  
1 8 2 1 4 7 3 2 3 6  
> `output.txt`  
> 17