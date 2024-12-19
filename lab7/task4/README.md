# Задание №4 по варианту  : `Наибольшая общая подпоследовательность двух последовательностей`

Студент ИТМО, Левахин Лев Александрович.
ИСУ: 343730

---

## Вариант 15

## Задание
Вычислить длину самой длинной общей подпоследовательности из двух последовательностей.
Даны две последовательности A = (a1, a2, ..., an) и B = (b1, b2, ..., bm), найти
длину их самой длинной общей подпоследовательности, т.е. наибольшее неотрицательное целое число p такое, что существуют индексы 1 ≤ i1 < i2 < ... < ip ≤ n
и 1 ≤ j1 < j2 < ... < jp ≤ m такие, что ai1 = bj1
, ..., aip = bjp.
- Формат ввода / входного файла (input.txt).  
Первая строка: n - длина первой последовательности.  
Вторая строка: a1, a2, ..., an через пробел.  
Третья строка: m - длина второй последовательности.  
Четвертая строка: b1, b2, ..., bm через пробел.  
- - Ограничения: 1 ≤ n, m ≤ 100; −109 < ai , bi < 109

- Формат вывода / выходного файла (output.txt).  
Выведите число p.

---

## Input / Output 
Пример 1

| Input | Output |
|-------|--------|
| 3     | 2      |
| 2 7 5 |        |
| 2     |        |
| 2 5   |        |

Пример 2

| Input    | Output |
|----------|--------|
| 1        | 0      |
| 7        |        |
| 4        |        |
| 1 2 3 4  |        |

Пример 3

| Input    | Output |
|----------|--------|
| 4        | 2      |
| 2 7 8 3  |        |
| 4        |        |
| 5 2 8 7  |        |

> В первом примере одна общая подпоследовательность – (2, 5) длиной 2, во
втором примере две последовательности не имеют одинаковых элементов.
В третьем примере - длина 2, последовательности – (2, 7) или (2, 8).

## Ограничения по времени и памяти

- Ограничение по времени. 1сек.
- Ограничение по памяти. 512 мб.

---

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/leonardo_Wer/Algosi.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algosi/lab7
   ```
3. **Запуск тестов к заданию**
 - Перейдите в папку с заданием
    ```bash
   cd task4
  - Перейдите в папку tests
    ```bash
      cd tests
  - Запустите файл `test.py`
    ```bash
      python test.py

4. **Запуск тестов для всех задач в лабораторной**
    ```bash
        python run_all_tests.py
    ```
5. **Запуск всех задач в лабораторной**
> С выводом входных данных и результата**
```bash
    python run_all_src.py
```

## Тестирование
Для запуска всех тестов выполните:
```bash
    pytest tests/
```