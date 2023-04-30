class ImageFileAcceptor:
    def __init__(self, extensions: tuple):
        self.extensions = extensions

    def __call__(self, filename=None, *args, **kwargs):
        return any(filename.rfind(f'.{ext}') >= 0 for ext in self.extensions)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
