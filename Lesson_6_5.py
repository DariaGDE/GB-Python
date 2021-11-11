class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки')
class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом - {self.title}')
class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой - {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером - {self.title}')

bic = Stationery('Новая запись')
bic.draw()
new_bic = Pen('Еще одна запись')
new_bic.draw()
new_pencil = Pencil('Что-то другое')
new_pencil.draw()
new_handle = Handle('Абсолютно новая запись')
new_handle.draw()
