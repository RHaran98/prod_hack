import os
import pandas as pd
from config import settings
from datetime import datetime


class ToDoList:
	def __init__(self):
		self.cols = ["Task","Task created","Priority"]
		self.priority_map = {"high":1,"med":2,"def":3, "low" :4}
		todo_file_exists = os.path.isfile(settings["TODO_FILEPATH"])
		if not todo_file_exists:
			# CREATE FILE
			pd.DataFrame({x:[] for x in self.cols}).to_csv(settings["TODO_FILEPATH"], index=None)

		self.df = pd.read_csv(settings["TODO_FILEPATH"])

	@staticmethod
	def checkInt(string: str):
		try:
			int(string)
			return True
		except ValueError:
			return False


	def add_task(self, task_desc,priority="def"):
		self.df.append({"Task":task_desc, "Task Created": datetime.now().timestamp(), "Priority":self.priority_map.get(priority, 3)})


	def remove_task(self, task_id):
		if self.checkInt(task_id):
			task_id = int(task_id)
			if task_id < len(self.df):
				print("No matches")
				return
			self.df = self.df.drop(task_id, inplace=True)
			self.df = self.df.reset_index(drop=True)

		else:
			indices = self.df[self.df["Task"].str.lower(task_id.lower())].index
			if len(indices) == 0:
				print("No matches")
				return
			elif len(indices) > 1:
				print("Multiple Matches")
				return

			self.df = self.df.drop(indices)
			self.df = self.df.reset_index(drop=True)
			print("Success")




