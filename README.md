# Приложение для бронирования авиабилетов
# =====================================
# Параметры запуска:
## 
## Переменные окружения:ㅤ
### BookingProject/settings/.env 
##  
#### DJANGO_SECRET_KEY
####  DATABASE_NAME
####  DATABASE_USER
####  DATABASE_PASSWORD
####  DATABASE_HOST
####  EMAIL_HOST_USER
####  DEFAULT_FROM_EMAIL
####  EMAIL_HOST_PASSWORD
####  CELERY_RESULT_BACKEND
####  CELERY_BROKER_URL
# =====================================

## Создание образов и контейнеров для Docker:
##  
#### ```docker image build -t booking:0.1 .```   - создание образа приложения
#### ```docker-compose build```    - собирание проекта
#### ```docker-compose up -d```    - запуск контейнеров