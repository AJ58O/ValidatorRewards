# ValidatorRewards
An XRP community initiative to incentivize good validator behavior

### How this app works:

1. Validator data is retreived thorugh the XRPL data API (https://xrpl.org/data-api.html). These functions are included in rippleStats.py
2. logic determining what makes a good validator is included in validatorScoreCard.py. All business logic is executed in the grep_all function
3. test.py pulls payment pointers and node public keys from the config file, gets a report for the past 24 hours, if the validator is good, adds them to a trigger files. 
4. Reward.sh reads the reward amount and payment pointers from files and runs an ilp-spsp send on each of the payment pointers.

### What defines good behavior?

Currently the App looks for 3 features:

1. Validating on the main net
2. Agreement score of 1
3. 0 missed ledgers

If you have other ideas, please let me know.

### Adding your validator

Config.py includes an object formatted like this:

```
{
    "publicKey":"paymentPointer"
}
```

1. Fork the repo
2. Add your node/validator to the object in config.py
3. Submit a pull request
4. Offer some sort of proof that you own this validator

If you don't know how to do 1-3, reach out to me on twitter: https://twitter.com/AJ58O


### Installation/Running:

If you don't have moneyd installed and configured yet, you will need to do that. Here's an extremely overkill script that can help you do that: https://github.com/AJ58O/K-ILP-it-with-fire

```
$ git clone https://github.com/AJ58O/ValidatorRewards.git
$ cd ValidatorRewards
$ pip3 install requirements.txt
$ bash run.sh
```

### Things to do:

1. Still trying to dockerize everything.
2. Test.py waits 15 seconds for moneyd to start up. It would be better for it to wait until the stdin shows the message "connector ready" or whatever the success message is.
3. Instead of the bash script being the entry point, make the python script start the bash script using os.subprocesses, then make it watch the stdout for the connector ready message, continue through the python script, then kick off another os.subprocess to start reward.sh (would this work?)


**Want to contirbute?** DM me on twitter: https://twitter.com/AJ58O
