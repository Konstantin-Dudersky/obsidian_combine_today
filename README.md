# Obsidian_combine_today

Заметки "на сегодня" могут находиться в нескольких хранилищах. Скрипт собирает содержимое таких заметок и ложит в один текстовый файл. Запускать по cron.

## Установка

- настроить переменные в файле `obsidian_combine_today.py`.

- Переместить скрипт в папку:

```bash
cp obsidian_combine_today.py ~/.local/bin
chmod +x ~/.local/bin/obsidian_combine_today.py
```

- добавить задачу в cron. Например, запуск каждые 5 минут.

```bash
crontab -e
```

```
*/5 * * * * ~/.local/bin/obsidian_combine_today.py
```

- в KDE можно добавить виджет "Веб-браузер", ввести адрес `file:///home/konstantin/desktop/today_tasks.md` (тот, который введен в переменной `TARGET_FILE`).

