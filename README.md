Клонирование репозитория:
  git@github.com:Danchiiik/intern.git

Создание виртуального окружения и установка зависимостей:
  python -m venv venv
  source venv/bin/activate  # для Linux/MacOS
  venv\Scripts\activate  # для Windows
  pip install -r requirements.txt

Создайте .env файл:
  SECRET_KEY=your_django_secret_key
  DEBUG=True  # True для разработки, False для продакшена
  ALLOWED_HOSTS=yourdomain.com, localhost
  DATABASE_URL=postgres://user:password@host:port/dbname
  TELEGRAM_BOT_TOKEN=your_telegram_bot_token

Как запустить:
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

Для получения уведомлений в Telegram необходимо:
  Создать бота с помощью BotFather и получить токен.
  Указать полученный токен в .env файле в переменной TELEGRAM_BOT_TOKEN.
  Запустить бота.

Task(Yandex):
  Выполнено все кроме создание комментария неаутентифицированным пользователем.

SQL:
  Не выполнен 4-task
