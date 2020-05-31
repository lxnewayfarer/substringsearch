# -*- coding: utf-8 -*-


def StraightSearch(text, pattern):
    for i in range(len(text) - len(pattern) + 1):   # цикл по всей строке
        for j in range(len(pattern)):   # цикл по образцу
            # если символ образца совпадает, то счетчик увеличивается
            if pattern[j] != text[i + j]:
                break
            elif j == len(pattern) - 1:
                return i
    return -1  # в случае ненахождения возвращается -1


def Prefix(pattern):    # префикс-функция для КМП поиска
    pi = []
    pi.append(0)
    j = 0
    i = 1
    while i < len(pattern):
        pi.append(0)
        if pattern[i] == pattern[j]:    # при совпадении символов префикса и суф
            pi[i] = j + 1
            i += 1
            j += 1
        elif j == 0:    # если нулевой символ
            pi[i] = 0
            i += 1
        else:   # иначе
            j = pi[j - 1]
    return pi[:len(pattern)]


def KMPsearch(text, pattern):
    pi = Prefix(pattern)    # нахождение префикс-функции
    k = 0
    l = 0
    while True:
        if text[k] == pattern[l]:
            k += 1
            l += 1
            if l == len(pattern):
                return k - len(pattern)  # возврат при полном совпадении
        elif l == 0:
            k += 1
            if k == len(text):
                return -1  # -1 если текст кончился
        else:
            l = pi[l - 1]   # сдвиг в соответствии с префикс-функцией


def RKsearch(text, pattern):
    alphabet = 256  # размер алфавита
    q = 101  # простое число для хэширования
    PatternHash = 0
    TextHash = 0
    m = len(pattern)
    n = len(text)
    h = alphabet ** (m - 1) % q  # множитель для полиноминального хэширования
    #  считаем хэш для образа и для первой подстроки длины образца
    for i in range(m):
        PatternHash = (alphabet * PatternHash + ord(pattern[i])) % q
        TextHash = (alphabet * TextHash + ord(text[i])) % q
    #  сдвигаем паттерн по тексту по букве
    for i in range(n - m + 1):
        #  проверка на совпадение хэшей подстроки и паттерна
        if PatternHash == TextHash:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
                else:
                    if j == m - 1:
                        return i
        if i < n - m:
            # пересчет кольцевого хэша
            TextHash = (
                alphabet * (TextHash - ord(text[i]) * h) + ord(text[i + m])) % q
            if TextHash < 0:
                TextHash += q
    return -1


def main():
    while True:
        print('Which method of search to use?\n\
               1 - KMP-search\n\
               2 - RK-search\n\
               3 - Straight search\n\
               4 - Exit program')
        menu = input()
        if menu == '4':
            return 0
        elif menu == '1' or menu == '2' or menu == '3':
            print('>> Input string:')
            string = input()
            print('>> Input substring:')
            substring = input()
            if menu == '1':
                result = KMPsearch(string, substring)
            elif menu == '2':
                result = RKsearch(string, substring)
            else:
                result = StraightSearch(string, substring)
            print('Result: ', result)
        else:
            print('Wrong option')


if __name__ == "__main__":
    main()
