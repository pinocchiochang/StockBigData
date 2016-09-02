# Node.js

## index.js
实现了一个简单的前端应用实时显示数据动态

### Dependencies
socket.io       http://socket.io/

redis           https://www.npmjs.com/package/redis

smoothie        https://www.npmjs.com/package/smoothie

minimist        https://www.npmjs.com/package/minimist

```sh
npm install nodejs_requirements.txt
```

### 运行代码
假如你的所有服务运行在一个叫做bigdata的docker-machine里面, 然后虚拟机的ip是192.168.99.100
```sh
node index.js --redis_host=192.168.99.100 --redis_port=6379 --subscribe_topic=average-stock-price
```
