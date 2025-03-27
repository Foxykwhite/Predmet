from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Ждём от 1 до 5 секунд между запросами

    @task(1)
    def load_homepage(self):
        response = self.client.get("/")
        print(f"Status code: {response.status_code}, Response length: {len(response.text)}")
    
    @task(2)
    def load_users_api(self):
        response = self.client.get("/polls/api/users/")
        print(f"Status code: {response.status_code}")

    def on_start(self):
        """Выполняется при старте пользователя, можно добавить авторизацию"""
        print("Запускаем тест пользователя!")