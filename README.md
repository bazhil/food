Тестовое задание для CodingTeam (подробности по ссылке: https://gist.github.com/ir0nfelix/88095feccf59824a60deb0ddb3aa3f29)

Чтобы проверить необходимо:
1) Выполнить в терминале команду для выгрузки репозитория: "git clone https://github.com/bazhil/food". Или выгрузить его иным способом. 
2) Установить зависимости выполнив команду: "pip install -r requirements.txt" (или иным способом).
3) Установить Postman (или иное ПО для выполнения API запросов).
4) Запустить сервер через терминал: "python manage.py runserver 127.0.0.1:8000".
5) В Postman (или аналоге) сделать GET-запрос по адресу: "http://127.0.0.1:8000/api/v1/foods/".

Так же для проверки можно воспользоваться Docker:
1) Установить Docker в соответствии с инструкцией на официальном сайте: "https://www.docker.com"
2) Запустить в Docker следующий image: "https://hub.docker.com/repository/docker/bazhil/food"
3) Выполнить п.3-5 из предыдущей инструкции.