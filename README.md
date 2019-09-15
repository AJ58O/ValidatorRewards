# ValidatorRewards
An XRP community initiative to incentivize good validator behavior

### How this app works:

1. Validator data is retreived thorugh the XRPL data API (https://xrpl.org/data-api.html). These functions are included in rippleStats.py
2. logic determining what makes a good validator is included in validatorScoreCard.py. All business logic is executed in the grep_all function
3. run.py pulls payment pointers and node public keys from the config file, gets a report for the past 24 hours, if the validator is good, adds them to a trigger files. Good validators are tipped using the XRPTipBot API

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

####Python3:
```
$ git clone https://github.com/AJ58O/ValidatorRewards.git
$ cd ValidatorRewards
$ export XRPTIPBOT_TOKEN={your token}
$ python3 run.py
```

####Docker
```
$ docker build -t validator-rewards
$ docker run --env XRPTIPBOT_TOKEN={your token} validator-rewards
```

### Things to do:

1. Find and add other data sources (ideally the source should be my own rippled node)
2. Automate bounty amount selection-- the daily bounty should be a function of (at least) market price and wallet balance.


**Want to contirbute?** DM me on twitter: https://twitter.com/AJ58O
