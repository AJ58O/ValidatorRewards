from validatorScoreCard import ValidatorScoreCard
from rippleStats import RippleStats

rs=RippleStats()
v_list = rs.list_validators()["validators"]

vsc=ValidatorScoreCard(v_list)

good_validators = vsc.grep_all(return_keys=True)
print(good_validators)


for i in range(1):
	print(rs.get_validator_report(good_validators[i], start=1))
