# bybit_parser
Парсер новостей на Scrapy.

### Описание ###
Парсер собирает новости с сайта https://announcements.bybit.com/en/?category=&page=1 и сохраняет их в файл output.csv
Парсер обновляет информацию каждую секунду.

### Установка ###

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Stanislav-Gutnikov/bybit_parser.git
```
```
cd bybit_parser/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить парсер ЕДИНОЖДЫ:

```
scrapy crawl bybit -O output.csv 
```

Запустить парсер С ОБНОВЛЕНИЕМ ИНФОРМАЦИИ КАЖДУЮ СЕКУНДУ:

```
python main.py
```

Чтобы остановить парсер - Ctrl + C