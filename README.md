# ValidatorRewards
An XRP community initiative to incentivize validators

This repo is still under construction. Here is how this app currently works:

1. validator data will be retreived thorugh the XRPL data API (https://xrpl.org/data-api.html). These functions are included in rippleStats.py
2. logic surrounding what makes a good validator is included in validatorScoreCard.py. ultimately, all business logic should be encapsulated in the grep_all function.
3. test.py is where I've been testing these functions

Here's what still needs to be added:

1. ILP module-- this is jenky, I'm probably going to do this in bash tbh. sorry bout it. If someone wants to port everything over to JS, by all means go for it. Shouldn't be too hard. I'm just a masochist.
  A. Need to add all dependencies to the docker file.
  B. Needs to accept a secret/pubkey as an env var


Ultimately I envision a list of good validators being returned each day (maybe look at historical reports using the get_validator_report function with a start of x days), and those validators receiving a bounty.

To deliver the funds, I'll need a payment pointer. I think I'm going to have a static config object that is like this:

```
{
    {{publicKey}}:{{paymentPointer}}
}
```
Getting your validator added will involve submitting a pull request with a comment, the comment must be a signed SHA256 message, decrypted using your public key. The message must be your ILP payment pointer. If you are able to successfully do that, I'll add you to the config. 

Sorry for the rambles, this is all intoxicated stream of conscious. here's the final workflow I'm settling on:
```
Get config
Get all pub keys in config object
Do validator checks (get daily report, look at agreement, missed ledgers, if there's a way to check uptime do that too, etc. Need to decide business logic around this, need community input)
Find the top performers (need to set threshholds, also need community input)
Distribute daily/whatever time period bounty equally between them
```



Initially the bounties will be small because I'll probably be self funding the wallet. If others contribute, that'd be gucci. Not going to post the wallet address until the app is finished. Want to contirbute? DM me on twitter: https://twitter.com/AJ58O


Installation/Running:

```
$ git clone https://github.com/AJ58O/ValidatorRewards.git
$ cd ValidatorRewards
$ docker build test .
$ docker run test
```


UPDATE: I've added new stuff, the payment stuff isn't dockerized but I have an app that works locally. Will use this on a CRON until I can dockerize everything
