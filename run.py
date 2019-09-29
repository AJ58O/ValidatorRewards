from validatorScoreCard import ValidatorScoreCard
from rippleStats import RippleStats
from pastebin import Pastebin
from config import get_config
import xrptipbotPy
import os
import sys
import datetime
import json

try:
	bounty = float(os.environ['BOUNTY'])
except:
	bounty = .05

try:
	x = xrptipbotPy.xrptipbot(os.environ['XRPTIPBOT_TOKEN'])
except Exception as e:
	logging.exception("ERROR")
	print("export XRPTIPBOT_TOKEN")
	sys.exit()

try:
	p = Pastebin(os.environ["PASTEBIN_TOKEN"])
	pastebin_logging = True
except:
	pastebin_logging = False

def create_log(balance, bounty, amount, success, fail):
	t = datetime.datetime.now()
	s = ""
	for suc in success:
		s += suc.replace("xrptipbot://twitter/","") + "\n"
	f = ""
	for fai in fail:
		f += fai.replace("xrptipbot://twitter/","")+ "\n"
	message = """
---------------------------
Runtime: {0}
Bounty: {1}
Amount: {2}
Balance: {3}
Success:
{4}

************
Fail:
{5}
************
---------------------------
	""".format(t, bounty, amount, balance, s, f)
	return message

def bytes_to_json(byteString):
	return json.loads(byteString.decode('utf8').replace("'", '"'))


def tip(amount, recipient):
	return x.tip(amount, recipient, True).json()


def main():
	print("starting")
	validator_config = get_config()
	validator_pubkey_list = list(validator_config.keys())
	rs=RippleStats()
	print("getting validatior reports")
	validator_report_list = rs.get_validator_reports_from_list(validator_pubkey_list)

	# validator_report_list = rs.list_validators()["validators"] ADD A WAY TO CRAWL MANIFESTS AND ASK NODE OPERATORS TO ADD A CUSTOM VALUE, THIS CAN BE ANOTHER OPTION INSTEAD OF THE STATIC CONFIG
	print("getting score cards")
	vsc=ValidatorScoreCard(validator_report_list)
	good_validator_keys = vsc.grep_all(return_keys=True)
	print("preparing payment info")
	good_validator_payment_pointers = [validator_config[x] for x in good_validator_keys]
	amount = round(bounty / len(good_validator_payment_pointers), 6) - .00001
	success = []
	fail = []
	print("making payments")
	for v in good_validator_payment_pointers:
		t = tip(amount, v)
		if t["error"] == False:
			success.append(v)
			balance = t["data"]["balance"]["balance"]["XRP"]
		else:
			fail.append(v)
	l = create_log(balance, bounty, amount, success, fail)
	if pastebin_logging == True:
		print("logging to pastebin")
		print(p.paste(l))
	print(l)
	print("done.")
	sys.exit()



		


main()