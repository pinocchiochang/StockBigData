# Node.js

## index.js
Implement a simple front-end chart for stock-data visualization

### Dependencies
socket.io       http://socket.io/
redis           https://www.npmjs.com/package/redis
smoothie        https://www.npmjs.com/package/smoothie
minimist        https://www.npmjs.com/package/minimist

```sh
npm install socket.io --save 
npm install express --save
npm install minimist --save 
npm install smoothie --save
```

### Run
```sh
node index.js --redis_host=`docker-machine ip bigdata` --redis_port=6379 --subscribe_topic=average-stock-price
```
