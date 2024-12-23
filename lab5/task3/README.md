# Задание № по варианту: `Обработка сетевых пакетов`

Студент ИТМО, Левахин Лев Александрович.
ИСУ: 343730

---

## Вариант 15

## Задание
#### В этой задаче вы реализуете программу для моделирования обработки сетевых пакетов.
- Вам дается серия входящих сетевых пакетов, и ваша задача - смоделировать их обработку. Пакеты приходят в определенном порядке. Для каждого
номера пакета i вы знаете время, когда пакет прибыл Ai и время, необходимое процессору для его обработки Pi (в миллисекундах). Есть только один
процессор, и он обрабатывает входящие пакеты в порядке их поступления.
Если процессор начал обрабатывать какой-либо пакет, он не прерывается и
не останавливается, пока не завершит обработку этого пакета, а обработка
пакета i занимает ровно Pi миллисекунд.
Компьютер, обрабатывающий пакеты, имеет сетевой буфер фиксированного
размера S. Когда пакеты приходят, они сохраняются в буфере перед обработкой. Однако, если буфер заполнен, когда приходит пакет (есть S пакетов,
которые прибыли до этого пакета, и компьютер не завершил обработку ни
одного из них), он отбрасывается и не обрабатывается вообще. Если несколько пакетов поступают одновременно, они сначала все сохраняются в буфере
(из-за этого некоторые из них могут быть отброшены - те, которые описаны
позже во входных данных). Компьютер обрабатывает пакеты в порядке их
поступления и начинает обработку следующего доступного пакета из буфера, как только заканчивает обработку предыдущего. Если в какой-то момент
компьютер не занят и в буфере нет пакетов, компьютер просто ожидает прибытия следующего пакета. Обратите внимание, что пакет покидает буфер и
освобождает пространство в буфере, как только компьютер заканчивает его
обработку

- Формат ввода или входного файла (input.txt).  
Первая строка содержит размер S буфера (1 ≤ S ≤ 105) и 
количество n (1 ≤ n ≤ 105) входящих сетевых пакетов. 
Каждая из следующих n строк содержит два числа, i-ая
строка содержит время прибытия пакета Ai (0 ≤ Ai ≤ 106) и время его обработки Pi (0 ≤ Pi ≤ 103) в миллисекундах. 
Гарантируется, что последовательность времени прибытия входящих пакетов – неубывающая, однако,
она может содержать одинаковые значения времени прибытия нескольких
пакетов, 
в этом случае рассматривается пакет, записанный во входном файле
раньше остальных, как прибывший ранее. 
(Ai ≤ Ai+1 для 1 ≤ i ≤ n − 1.)
- Формат вывода или выходного файла (output.txt).  
Для каждого пакета напечатайте время (в миллисекундах), 
когда процессор начал его обрабатывать; или -1, если пакет был отброшен.
Вывести ответ нужно в том же порядке, как пакеты были описаны во входном файле.

---

## Input / Output 
- Пример 1

| Input | Output |
|-------|--------|
| 1 0   |        |
| Row 2 |        |
| Row 3 |        |

- Пример 2

| Input | Output |
|-------|--------|
| 1 1   | 0      |
| 0 0   |        |
| Row 3 |        |

- Пример 3

| Input | Output |
|-------|--------|
| 1 2   | 0      |
| 0 1   |        |
| 0 0   |        |

## Ограничения по времени и памяти

- Ограничение по времени. `10сек`
- Ограничение по памяти `512 мб`

<hr>

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/leonardo_Wer/Algosi.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Algosi/lab4
   ```
3. **Запуск тестов к заданию**
 - Перейдите в папку с заданием
    ```bash
   cd task1
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
