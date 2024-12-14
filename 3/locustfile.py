from locust import HttpUser, task, between

class CalcUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/calc/3/3.14159/100")