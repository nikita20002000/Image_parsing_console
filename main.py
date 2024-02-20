from img_collector import GoogleImageCollector
from img_collector import BingImageCollector
from img_collector import BaiduImageCollector


def info_collector() -> dict:
    arguments = {
        "feeder_threads": 1,
        "parser_threads": int(input("Введите количество Parser Threads - ")),
        "downloader_threads": int(input("Введите количество Downloader Threads - ")),
        "storage": {
            'root_dir': input('Введите название директории для сохранения - ')
        }
    }

    return arguments


def parsing_process(parser) -> None:
    filters = dict(
        size='large',
        color='orange',
        license='commercial,modify',
        date=((2017, 1, 1), (2017, 11, 30)))

    if input('Желаете применить дополнительные фильтры? Y/n ').lower() == 'y':

        filters['size'] = input('Введите желаемый размер small / large - ')
        filters['color'] = input('Введите желаемый цвет на латинице - ')
        filters['license'] = 'commercial,modify'

        while True:
            try:
                in_date = list(map(lambda x: int(x), input('Введите диапазон дат через пробел в порядке увеличения\n'
                                                           'Пример: 2017 1 1 2018 1 1\n').split(' ')))
                filters['date'] = ((in_date[0], in_date[1], in_date[2]), (in_date[3], in_date[4], in_date[5]))

                print('Фильтры успешно применены')
                break

            except Exception as e:
                print(e, " Проверьте правильность ввода даты")

    keyword = input('Введите комбинацию слов для поиска - ')
    max_num = int(input('Введите желаемое количество картинок - '))

    parser.crawl(keyword=keyword, filters=filters, max_num=max_num, file_idx_offset=0)


def main(user_choice):
    data = info_collector()
    print('Данные успешно собраны, выполняется создание парсера...')

    match user_choice:
        case '0':
            google_p = GoogleImageCollector(
                feeder_threads=data['feeder_threads'],
                parser_threads=data['parser_threads'],
                downloader_threads=data['downloader_threads'],
                storage=data['storage'], )

            try:
                parsing_process(google_p)
            except Exception as e:
                return 'Проверьте правильность ввода данных и повторите попытку\n' \
                       'ERROR MES: ' + e

        case '1':
            bing_p = BingImageCollector(
                feeder_threads=data['feeder_threads'],
                parser_threads=data['parser_threads'],
                downloader_threads=data['downloader_threads'],
                storage=data['storage'], )

            try:
                parsing_process(bing_p)
            except Exception as e:
                return 'Проверьте правильность ввода данных и повторите попытку\n' \
                       'ERROR MES: ' + e

        case '2':
            baidu_p = BaiduImageCollector(
                feeder_threads=data['feeder_threads'],
                parser_threads=data['parser_threads'],
                downloader_threads=data['downloader_threads'],
                storage=data['storage'], )

            try:
                parsing_process(baidu_p)
            except Exception as e:
                return 'Проверьте правильность ввода данных и повторите попытку\n' \
                       'ERROR MES: ' + e

    print('Процесс завершен, проверьте пожалуйста директорию')


if __name__ == "__main__":
    while True:
        a: str = input('Выберите желаемый парсер 0 - 2 \n'
                       '0 - Google\n'
                       '1 - Bing\n'
                       '2 - Baidu\n')
        if a in ['0', '1', '2']:
            break
        else:
            print('Проверьте правильность введенных данных и попробуйте еще раз...')
    main(a)
