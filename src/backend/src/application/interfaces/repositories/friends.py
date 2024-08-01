from abc import ABC, abstractmethod


class IFriendRepository(ABC):
	@abstractmethod
	def add_one_friend():
		raise NotImplementedError
	
	