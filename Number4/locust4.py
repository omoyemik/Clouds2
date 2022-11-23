import time
from locust import HttpUser, task, between

class QuickStartUser(HttpUser):
    @task
    def integral(self):
        self.client.get("/?lower=0&upper=3.14159")
