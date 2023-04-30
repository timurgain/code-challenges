# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def _check_is_show(func):
        def wrapper(self):
            if not self.is_show:
                return print("Отображение данных закрыто")
            return func(self)
        return wrapper

    @_check_is_show
    def show_table(self):
        table = ' '.join(str(value) for value in self.data)
        print(table)

    @_check_is_show
    def show_graph(self):
        table = ' '.join(str(value) for value in self.data)
        print(f"Графическое отображение данных: {table}")

    @_check_is_show
    def show_bar(self):
        table = ' '.join(str(value) for value in self.data)
        print(f"Столбчатая диаграмма: {table}")

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()
