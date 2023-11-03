from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def normal_sort(self):
        #  http://localhost:8000/ 가 앞에 붙는다!
        # self.client.get("test/A/")
        # self.client.get("test/B/")
        # self.client.get("test/C/")
        self.client.get("test/D/")

    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")


