import requests
from datetime import datetime, timedelta

class RippleStats:
	def __init__(self):
		#docs: https://xrpl.org/data-api.html
		self.base_url = "https://data.ripple.com"

	def list_validators(self):
		"""
		RESPONSE:
		result	String	The value success indicates that the body represents a successful response.
		count	Integer	Number of validators returned.
		validators	Array of Validator Objects	List of validators active in the last 24 hours.
		"""
		url = "{0}/v2/network/validators".format(self.base_url)
		return requests.get(url=url).json()

	def get_validator(self, pubkey):
		"""
		RESPONSE:
		result	String	The value success indicates that the body represents a successful response.
		validation_public_key	String - Base-58 Public Key	This validator's validator public key.
		domain	String	(May be omitted) The DNS domain associated with this validator.
		chain	String	Ledger hash chain which this validator is currently following. The value main indicates the main network and altnet indicates the XRP Test Network. Other forks are named chain.{NUMBER}, where {NUMBER} is a unique number for each fork.
		unl	Bool	True if the validator is part of the ledger chain's recommended UNL.
		current_index	Number	Ledger index of most recently validated ledger.
		partial	Bool	True if the most recent validation was a partial one.
		agreement_1h	Agreement Object	Object containing agreement stats for the most recent hour.
		agreement_24h	Agreement Object	Object containing agreement stats for the most recent 24 hour period.

		AGREEMENT OBJECTS:
		score	String	Score of agreement with the ledger chain being followed.
		missed	Integer	Number of ledgers not validated during the time period.
		total	Integer	Number of ledgers that could have been validated during the time period.
		incomplete	Bool	True indicates the data does not cover the entire time period.
		"""
		url = "{0}/v2/network/validators/{1}".format(self.base_url, pubkey)
		return requests.get(url=url).json()

	def get_validator_report(self, pubkey, start=1, end=None, descending=None):
		"""
		@param start	int - number of days. defaults 1
		@param end	String - Timestamp	End date and time for historical query. The default is to end with the most recent data available. YYYY-MM-DDThh:mm:ssZ
		@param descending	Bool	Return results in reverse order.

		RESPONSE:
		result	String	The value success indicates that the body represents a successful response.
		count	Integer	Number of validator daily reports returned.
		reports	Array of Single Validator Report Objects	Daily reports of each validator's performance on that day.

		REPORTS OBJECT:
		validation_public_key	String - Base-58 Public Key	Validator public key.
		date	String - Timestamp	The start time of the date this object describes. YYYY-MM-DDThh:mm:ssZ
		chain	String	Ledger hash chain which this validator is currently following. The value main indicates the main network and altnet indicates the XRP Test Network. Other forks are named chain.{NUMBER}, where {NUMBER} is a unique number for each fork.
		score	String	Score of agreement with the ledger chain being followed.
		missed	Integer	Number of ledgers not validated during the time period.
		total	Integer	Number of ledgers that could have been validated during the time period.
		incomplete	Bool	True indicates the data does not cover the entire time period.
		"""
		
		start = str((datetime.now() - timedelta(start)).isoformat()).split(".")[0] #yesterday
		print(start)
		url="{0}/v2/network/validators/{1}/reports".format(self.base_url, pubkey)
		params = {
			"start":start,
			"end":end,
			"descending":descending
		}
		return requests.get(url=url, params=params).json()

	def get_validator_reports_from_list(self, validators):
		"""
		@param validators list: list of public keys to retreive reports for

		RESPONSE: list of report objects
		"""
		report_list = []
		for v in validators:
			try:
				report_list += [x for x in self.get_validator_report(v)["reports"]]
			except Exception as e:
				print("ERROR GETTING VALIDATOR REPORT")
				print(e)
		print(report_list)
		return report_list
		

