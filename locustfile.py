from locust import HttpLocust, TaskSet, task, between
from random import choice, randint
from data_handler import data_reader
import csv


words_list = data_reader('pics_data.csv', 0)
pic_date_list = data_reader('words_data.csv', 0)


class TestUserBehavior(TaskSet):
	
	@task(2) # @task is a decorator, takes an optional weight argument that can be used to specify the task’s execution ratio. 
	def search(self):
		self.client.get(f'/search?text={choice(words_list)}')

	@task(1)
	def change_pic_page(self):
		self.client.get(f'/strips/{choice(pic_date_list)}')

	@task(2)
	def change_page(self):
		self.client.get(f'/index{randint(1, 3125)}')


class TestUser(HttpLocust):
	task_set = TestUserBehavior
	wait_time = between(5, 9)
		
