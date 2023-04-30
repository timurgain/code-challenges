class Model:

    def query(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        res = 'Model'
        if len(self.__dict__) > 0:
            res = f"Model: {', '.join([f'{k} = {v}'for k, v in self.__dict__.items()])}"

        return res


if __name__ == '__main__':
    model = Model()
    model.query(id=1, fio='Sergey', old=33)
    print(model)
