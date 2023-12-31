from wsgiref.simple_server import make_server
from dmitry_framework.main import Framework
from lesson_4.urls import routes, fronts
import lesson_4.dmitry_framework.my_requests as my_requests

application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
