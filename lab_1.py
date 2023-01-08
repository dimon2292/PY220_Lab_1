class Computer:
    def __init__(self, type: str, size_SSD: int):
        """

        :param type: марка ноутбука
        :param size_SSD: объём ССД
        """
        self.type = type
        self.size_SSD = None
        self.init_size_SSD(size_SSD)

    def init_size_SSD(self, size_SSD):                    #
        if not size_SSD > 0:
            raise ValueError('число д.б. больше нуля')
        self.size_SSD = size_SSD

    def __repr__(self):
        return f"Computer({self.type},{self.size_SSD})"

    def is_compatible(self, game_name, game_system_requirements: dict) -> bool:
        """
        Проверка, способен ли компьютер запустить данную видеоигру
        :param name: название игры
        :param system_requirements: словарь содержащий системные требования игры
        :return: возвращает True, если по своим требованиям игра способна запускаться на данном компьютере
        """
    def get_index (self, dict_: dict) -> float:
        """
        По заданному набору характеристик выдаёт индекс производительности компьютера
        :param dict_: словарь характеристик  компьютера
        :return: дробное число (индекс производительности)
        """
my_comp = Computer('MSI', 256)
print(my_comp)