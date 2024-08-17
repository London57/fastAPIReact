from abc import ABC, abstractmethod


class IUserAuthService(ABC):
	@abstractmethod
	def register_user():
		raise NotImplementedError

	@abstractmethod
	def authenticate_user():
		raise NotImplementedError
	
	
