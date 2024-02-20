from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import BaiduImageCrawler


class GoogleImageCollector(GoogleImageCrawler):

    @staticmethod
    def describe() -> str:
        return 'author Nikita20002000\n' \
               'Класс GoogleImageCollector наследует класс GoogleImageCrawler\n' \
               'Ссылка на документацию - https://icrawler.readthedocs.io/en/latest/'


class BingImageCollector(BingImageCrawler):

    @staticmethod
    def describe() -> str:
        return 'author Nikita20002000\n' \
               'Класс BingImageCollector наследует класс BingImageCrawler\n' \
               'Ссылка на документацию - https://icrawler.readthedocs.io/en/latest/'


class BaiduImageCollector(BaiduImageCrawler):

    @staticmethod
    def describe() -> str:
        return 'author Nikita20002000\n' \
               'Класс BaiduImageCollector наследует класс BaiduImageCrawler\n' \
               'Ссылка на документацию - https://icrawler.readthedocs.io/en/latest/'


ImageCollect = GoogleImageCollector(storage={'root_dir': 'Sport'})
