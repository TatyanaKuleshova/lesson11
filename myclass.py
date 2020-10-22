import pickle

class Articles:

    def __init__(self, article, num_characters, price):
        '''
        :param article: количество статей
        :param num_characters: количество знаков в статье
        :param price: стоимость 1 знака в рублях
        '''
        self.article = article
        self.num_characters = num_characters
        self.price = price
        self.all = [article, num_characters, price]


#равенство
    def __eq__(self, other):
        return self.all == other.all

#умножение
    def __mul__(self, other):
        return (self.article * other.article, self.num_characters * other.num_characters, self.price * other.price)

#сложение
    def __add__(self, other):
        return (self.article + other.article, self.num_characters + other.num_characters, self.price + other.price)

#оператор Меньше
    def __lt__(self, other):
        return self.article < other.article

#Оператор больше
    def __gt__(self, other):
        return self.price > other.price

#оператор не равно
    def __ne__(self, other):
        return (self.article != other.article, self.price != other.price)

#возведение в степень 1 и 3 параметров
    def __pow__(self, other, modulo=None):
        return (self.article**other.article, self.price**other.price)

#разность между art1 b art2
    def __sub__(self, other):
        return (self.article - other.article, self.num_characters - other.num_characters, self.price - other.price)

#Сериализация, десериализация
    def __getstate__(self):
        return self.all

    def __setstate__(self, state):
        self.all = state

#удалим из памяти все параметры
    def __del__(self):
        del self.all


if __name__ == '__main__':
    art1 = Articles(4, 245, 3)
    art2 = Articles(6, 978, 2)

    print(art1 * art2)
    print(art1 + art2)
    print(art1 < art2)
    print(art1 > art2)
    print(art1 != art2)
    print(art1**art2)
    print(art1 - art2)

f = open('data.pkl', 'wb')
pickle.dump(art1, f)
f.close()

f = open('data.pkl', 'rb')
art1_new = pickle.load(f)
print(art1, art1_new)
f.close()








