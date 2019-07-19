REWARD=`cat reward.txt`
filelines=`cat validators.txt`
echo $REWARD
echo $VALIDATORS
for line in $filelines ; do
	ilp-spsp send --amount $REWARD --receiver $line
done
