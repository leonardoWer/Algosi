file_in = open("input.txt")
file_out = open("output.txt", "w")

n = int(file_in.readline()) #Количество жителей
m = list(map(float, file_in.readline().split())) #Список с состоянием житиель, индексы жителей i+1

if n%2==0 or len(m)%2==0:
    print("Число жителей должно быть нечётно!")
else:
    win_list = []

    win_list.append(m.index(min(m)) + 1)
    m_sort = sorted(m)
    win_list.append(m.index(m_sort[len(m_sort)//2]) + 1)
    win_list.append(m.index(max(m)) + 1)

    win_list = [str(el) for el in win_list]
    file_out.write(" ".join(win_list))








