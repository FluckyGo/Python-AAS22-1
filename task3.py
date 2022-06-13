def LevensteineDistance(s, t):
    n, m = len(t), len(s)
    v0 = list(range(n)) + [0]
    v1 = [0]*(n + 1)

    for i in range(m):
        v1[0] = i +1
        for j in range(n):
            deletionCost = v0[j + 1] + 1
            insertionCost = v1[j] + 1
            if s[i] == t[j]:
                substitutionCost = v0[j]
            else:
                substitutionCost = v0[j] + 1

            v1[j + 1] = min(deletionCost, insertionCost, substitutionCost)
        v0, v1 = v1, v0

    return v0[n]/ max(len(s), len(t))

if __name__ == '__main__':

    word1 = str(input('Введи первое слово: \n'))
    word2 = str(input('Введи второе слово: \n'))
    pairs = [(word1, word2)]

    for s, t in pairs:
        print(s, t,  (1 - LevensteineDistance(s, t)))




s1 = ('гусь', 'хвост', 'лис', 'собака', 'кошка', 'птица', 'дом', 'январь', 'арматура', 'китай')
s2 = str(input('Введи слово: \n'))

def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count / max(len(s1), len(s2))

for i in s1:
    print(i, compare(i, s2))







