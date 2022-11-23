import time
from locust import Httpuser, task, between

class QuickstartUser(HttpUser):
  @task
  def hello_world(self):
    self.client.get("/integral/0/3.1)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
