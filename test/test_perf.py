from locust import task, HttpLocust, TaskSet


class DataIngest(TaskSet):

    def on_start(self):
        print('Started')



