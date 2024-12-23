# Задание № по варианту  : `Скобочная последовательность. Версия 2`

Студент ИТМО, Левахин Лев Александрович.
ИСУ: 343730

<hr>

## Вариант 15

## Задание
Определение правильной скобочной последовательности такое же, как и в
задаче 3, но теперь у нас больше набор скобок: []{}().
Нужно написать функцию для проверки наличия ошибок при использовании
разных типов скобок в текстовом редакторе типа LaTeX.
Для удобства, текстовый редактор должен не только информировать о наличии
ошибки в использовании скобок, но также указать точное место в коде (тексте) с
ошибочной скобочкой.
 - В первую очередь объявляется ошибка при наличии первой несовпадающей
закрывающей скобки, перед которой отсутствует открывающая скобка, или которая не соответствует открывающей, например, ()[} - здесь ошибка укажет на
}.
 - Во вторую очередь, если описанной выше ошибки не было найдено, нужно
указать на первую несовпадающую открывающую скобку, у которой отсутствует
закрывающая, например, ( в ([].
> Если не найдено ни одной из указанный выше ошибок, нужно сообщить, что
использование скобок корректно.
>>Помимо скобок, код может содержать большие и маленькие латинские буквы,
цифры и знаки препинания.

Формально, все скобки в коде (тексте) должны быть разделены на пары совпадающих скобок, так что в каждой паре открывающая скобка идет перед закрывающей скобкой,
а для любых двух пар скобок одна из них вложена внутри другой,
как в (foo[bar]) или они разделены, 
как в f(a,b)-g[c]. 
> Скобка [ соответствует скобке ], и ( соответствует ).

<hr>

- Формат входного файла (input.txt).  
Входные данные содержат одну строку S, состоящую из больших и маленьких латинских букв, цифр, знаков
препинания и скобок из набора [] (). Длина строки S – 1 ≤ S leq105
4
- Формат выходного файла (output.txt).  
Если в строке S скобки используются правильно, выведите «Success» (без кавычек). В противном случае
выведите отсчитываемый от 1 индекс первой несовпадающей закрывающей
скобки, а если нет несовпадающих закрывающих скобок, выведите отсчитываемый от 1 индекс первой открывающей скобки, не имеющей закрывающей. 

<hr>

## Input / Output 

| Input      | Output  |
|------------|---------|
| []         | Success |
| {}[]       | Success |
| [()]       | Success |
| (())       | Success |
| {          | 1       |
| {[}        | 3       |
| foo(bar)   | Success |
| foo(bar[i) | 10      |

## Ограничения по времени и памяти

- Ограничение по времени. 5сек.
- Ограничение по памяти. 256 мб.

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

## Тестирование
Для запуска всех тестов выполните:
```bash
    pytest tests/
```
