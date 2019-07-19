import sys

class ilpTrigger:
	def __init__(self, validators, bounty):
		"""
		writes the trigger file for the bash script, then exits the python phase

		@param validators list: list of validators to receive payment
		@param bounty int: number of XRP to divide amongst the validators
		"""
		unit = 1000000000 #billionth
		reward=bounty * unit // len(validators)
		validators_as_string = ""
		for v in validators:
			validators_as_string+="{0}\n".format(v)
		with open('reward.txt', 'w') as logfile:
			logfile.write(str(reward))
		with open('validators.txt', 'w') as logfile:
			logfile.write(validators_as_string)

		sys.exit()
		
