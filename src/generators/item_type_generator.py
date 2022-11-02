from src.baseclasses.builder import BuilderBaseClass
from faker import Faker


fake = Faker()


class ItemsTypeBuilder(BuilderBaseClass):
    """
    Генератор случайных итемов для базы данных
    """
    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_item_type(self, item_type=fake.word()):
        self.result['item_type'] = item_type
        return self

    def reset(self):
        self.set_item_type()

    def build(self):
        return self.result


if __name__ == '__main__':
    item = ItemsTypeBuilder().build()
    print(item)
