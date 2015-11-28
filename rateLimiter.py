# double buffering
class client:
	def __init__(self, maxTries, timeout):
		self.maxTries = maxTries
		self.timeout = timeout
		self.attempts = dict()

	def rateLimiter(self,clientId,time):
		recentAttempts = 0
		if clientId in self.attempts:
			for attempt in self.attempts[clientId]:
				if attempt > time-self.timeout:
					recentAttempts+=1
			self.attempts[clientId] = self.attempts[clientId][-self.maxTries:]
			if recentAttempts>=self.maxTries:
				return True
			self.attempts[clientId].append(time)
			return False
		else:
			self.attempts[clientId] = list()
			self.attempts[clientId].append(time)
			return False

rateLimiter = client(2,5)
print rateLimiter.rateLimiter(1, 3)
print rateLimiter.rateLimiter(1, 4)
print rateLimiter.rateLimiter(1, 6)
print rateLimiter.rateLimiter(1,10)