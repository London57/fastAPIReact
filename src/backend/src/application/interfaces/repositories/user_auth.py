from abc import ABC, abstractmethod


class IUserAuthRepository(ABC):
	@abstractmethod
	def create_user():
		raise NotImplementedError
	
	@abstractmethod
	def get_user_by_username():
		raise NotImplementedError
	
	@abstractmethod
	def authenticate_user():
		raise NotImplementedError
	