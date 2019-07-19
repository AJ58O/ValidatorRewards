from validatorScoreCard import ValidatorScoreCard
from rippleStats import RippleStats
from paymentHandler import ilpTrigger
from config import get_config
import time

time.sleep(15) #to wait for moneyd to start
validator_config = get_config()
validator_pubkey_list = list(validator_config.keys())
rs=RippleStats()
validator_report_list = rs.get_validator_reports_from_list(validator_pubkey_list)

# validator_report_list = rs.list_validators()["validators"] ADD A WAY TO CRAWL MANIFESTS AND ASK NODE OPERATORS TO ADD A CUSTOM VALUE, THIS CAN BE ANOTHER OPTION INSTEAD OF THE STATIC CONFIG

vsc=ValidatorScoreCard(validator_report_list)

good_validator_keys = vsc.grep_all(return_keys=True)
good_validator_payment_pointers = [validator_config[x] for x in good_validator_keys]
print(good_validator_payment_pointers)

ilpTrigger(good_validator_payment_pointers, .1)
