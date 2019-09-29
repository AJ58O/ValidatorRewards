class ValidatorScoreCard:
	def __init__(self, validators):
		self.validators = validators
	def grep_perfect_agreement(self, return_list=False):
		"""
		@param validators: list of validator objects
		@param return_list: bool, if true return_lists self.validators, otherwise updates self.validators
		RESPONSE: list of all validators with perfect agreement
		"""
		start_list = self.validators
		if return_list==False:
			self.validators = [x for x in self.validators if float(x["score"])==1]
			print("Filtered out for non-perfect agreement:\n{0}".format([x for x in start_list if x not in self.validators]))
		else:
			return [x for x in self.validators if float(x["score"])==1]

	def grep_no_misses(self, return_list=False):
		"""
		@param validators: list of validator objects
		@param return_list: bool, if true return_lists self.validators, otherwise updates self.validators
		RESPONSE: list of all validators with no misses
		"""
		start_list = self.validators
		if return_list==False:
			self.validators = [x for x in self.validators if int(x["missed"])==0]
			print("Filtered out for ledger misses:\n{0}".format([x for x in start_list if x not in self.validators]))
		else:
			return [x for x in self.validators if int(x["missed"])==0]

	def grep_main_chain(self, return_list=False):
		"""
		@param validators: list of validator objects
		@param return_list: bool, if true return_lists self.validators, otherwise updates self.validators
		RESPONSE: list of all validators on main chain
		"""
		start_list = self.validators
		if return_list==False:
			self.validators = [x for x in self.validators if x["chain"]=="main"]
			print("Filtered out for non main chain:\n{0}".format([x for x in start_list if x not in self.validators]))
		else:
			return [x for x in self.validators if x["chain"]=="main"]

	def grep_all(self,return_keys=False):
		"""
		@param validators: list of validator objects
		@param return_list: bool, if true return_lists self.validators, otherwise updates self.validators
		RESPONSE: list of all validators on main chain
		"""
		self.grep_main_chain()
		self.grep_no_misses()
		self.grep_perfect_agreement()
		if return_keys:
			return self.get_all_public_keys()

	def get_all_public_keys(self):
		"""
		returns all node public keys from the list
		"""
		return [x["validation_public_key"] for x in self.validators]

	def get_list(self):
		"""
		returns self.validators
		"""
		return self.validators
	
