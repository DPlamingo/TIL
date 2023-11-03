from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    # @task
    # def normal_sort(self):
    #     self.client.get("test/normal_sort/")

    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")

    # @task
    # def data_return(self):
    #     self.client.get("test/data_return/")
    
    # @task
    # def file_open(self):
    #     self.client.get("test/file_open/")
        
    @task
    def find_similar_ages(self):
        self.client.get("test/find_similar_ages/")

