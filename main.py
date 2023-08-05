from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    @staticmethod
    def get_page_data(html_filename):
        """
        Метод чтения html-кода из html-файла
        :param html_filename: имя html-файла
        :return: содержимое html-файла
        """
        with open(html_filename, "r", encoding="utf-8") as file:
            file_data = file.read()
        return file_data

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        html_page = self.get_page_data('homework.html')
        self.send_response(200)     # Отправка кода ответа
        self.send_header("Content-type", "text/html")   # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(html_page, "utf-8"))     # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
