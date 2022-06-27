# Парсер документации PEP.
### Финальный проект 18-го спринта курса Python+.
### Яндекс Практикум. 5-я когорта pythonplus.
### Студент: Андрей Федотов.

### Перед началом работы:
1. Склонируйте репозиторий.
2. Создайте виртуальное окружение.
3. Установите зависимости ```pip install -r requirements.txt```.

### Запуск парсера:
```
main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}
Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```

### Режимы работы парсера:

1. ```python main.py whats-new``` - Парсер статей по нововведениям в Python.
2. ```python main.py latest-versions``` - Статусы последних версий со ссылками на документацию.
3. ```python main.py download``` - Скачивание документации по последней версии Python.
4. ```python main.py pep``` - Формирование таблицы с количеством PEP в разрезе по статусам.

### Опции:

1. ```--output pretty``` - вывод в табличном представлении в консоль.
2. ```--output file``` - вывод таблицы с результатами в файл csv.
3. ```-c``` - очистка кеша перед следующими запросами парсера.


