npm install -g ilp-connector
npm install -g five-bells-condition
npm install -g five-bells-integration-test
npm install -g ilp
npm install -g oer-utils
npm install -g ilp-packet
npm install -g five-bells-service-manager
npm install -g five-bells-integration-test-loader
npm install -g ilp-connector-backend-yahoo
npm install -g ilp-plugin-xrp-paychan
npm install -g koa-ilp
npm install -g btp-packet
npm install -g ilp-curl
npm install -g ilp-plugin
npm install -g ilp-plugin-mini-accounts
npm install -g ilp-plugin-btp
npm install -g ilp-protocol-ildcp
npm install -g ilp-store-redis
npm install -g ilp-plugin-xrp-asym-client
npm install -g ilp-plugin-xrp-asym-server
npm install -g ilp-plugin-xrp-paychan-shared
npm install -g ilp-store-simpledb
npm install -g ilp-plugin-outgoing-settle
npm install -g ilp-protocol-spsp
npm install -g tf-connector
npm install -g ilp-store-memory
npm install -g moneyd
npm install -g ilp-spsp
npm install -g ilp-spsp-server
npm install -g ilp-plugin-ethereum
echo "                  "
echo "Dependencies installation complete! Now we're going to configure your moneyd instance."
echo "After we configure moneyd, we'll start it. If you want to start moneyd in the future, just run moneyd xrp:start"
echo "                  "
moneyd xrp:configure
moneyd xrp:start