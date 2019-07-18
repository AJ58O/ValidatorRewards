from validatorScoreCard import ValidatorScoreCard
from rippleStats import RippleStats
from paymentHandler import ilpTrigger
import time

time.sleep(15)
rs=RippleStats()
v_list = rs.list_validators()["validators"]

vsc=ValidatorScoreCard(v_list)

good_validators = vsc.grep_all(return_keys=True)

ilpTrigger(good_validators, 1)
