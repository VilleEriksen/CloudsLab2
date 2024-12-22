from locust import HttpUser, task, between

class CalcUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/calc/0/3.14159")