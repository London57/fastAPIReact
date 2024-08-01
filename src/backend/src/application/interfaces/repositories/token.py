from abc import ABC, abstractmethod


class ITokenService(ABC):
	@abstractmethod
	def create_token():
		raise NotImplementedError
	
	@abstractmethod
	def verify_token():
		raise NotImplementedError
	