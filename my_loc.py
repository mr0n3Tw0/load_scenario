from locust import HttpLocust, TaskSet, task, between
from random import choice, randint

class TestUserBehavior(TaskSet):
	pic_date_list = [201901, 201902, 201903, 201904, 201905, 201906, 201907, 201908, 201909, 201910, 201911, 201912, 202001, 202002,]
	
	words_list = ['lawyer', 'advertising', 'date', 'available', 'high', 'hope', 'pepper', 'weakness', 'restoration', 'tactic', 'cluster', 'twilight', 'glue', 'performance', 'cabin', 'sodium', 'earthflax',]
	
	@task(2)
	def search(self):
		self.client.get(f'/search?text={random.choice(words_list)}')

	@task(1)
	def change_pic_page(self):
		self.client.get(f'/strips/{random.choice(pic_date_list)}')

	@task(2)
	def change_page(self):
		self.client.get(f'/index{random.randint(1, 3125)}')


class TestUser(HttpLocust):
	task_set = TestUserBehavior
	wait_time = between(5, 9)
		
