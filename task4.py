
class String_compare:
    def compare(self, s1, s2):
        ngrams = [s1[i:i +3] for i in range(len(s1))]
        count = 0
        for ngram in ngrams:
            count += s2.count(ngram)

        return count / max(len(s1), len(s2))



if __name__ == '__main__':
    x = String_compare()
    print(x.compare('Мобилизация', 'Мобильник'))

    s1 = ('Григорий', 'Лев', 'Андрей', 'Роман', 'Арсений', 'Степан',
          'Владислав', 'Никита', 'Глеб', 'Марк', 'Давид', 'Ярослав')
    s2 = ('Алексей', 'Андрей', 'Артемий', 'Виктор', 'Никита',
          'Даниил', 'Денис', 'Егор', 'Игорь', 'Тимофей')
    y = String_compare()
    for z in s1:
        for c in s2:
            if y.compare(z, c) > 0:
                print(z,c, y.compare(z, c))