# Image parsing console prog
Консольная программа для парсинга изображений по определенным критериям. Есть возможность сбора изображений с Google, Bing и Baidu.
## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Требования](#to-do)
- [FAQ](#FAQ)

## Технологии
- [icrawler](https://icrawler.readthedocs.io/en/latest/)


## Начало работы
Расскажите как установить и использовать ваш проект, покажите пример кода:

Установите все необходимые зависимости выполнив команду
```sh
pip install -r requirements.txt
```
Или 
```sh
pip3 install -r requirements.txt
```

Запустите исполняемый файл main.py выполнив команду
```typescript
python main.py
```
Или
```typescript
python3 main.py
```

## Требования
python версии 3 или выше<br>
pip версии 21 или выше

## FAQ
Классы GoogleImageCollector, BingImageCollector и BaiduImageCollector полностью наследуют функционал исходных классов из библиотеки icrawler для более подробной информации рекомендуется ознакомиться с документацией на сайте https://icrawler.readthedocs.io/en/latest/
