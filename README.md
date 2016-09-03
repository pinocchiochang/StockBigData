# Real-time Stock Bigdata

# Description
1. 创建docker image来作为主要架构的运行环境的容器，以达到资源和环境的隔离
2. 利用kafka分布式发布订阅消息系统，快速从网上抓取股票信息
3. 建立一个cassandra数据库，persist从kafka输出的数据流以作备份
4. 构建spark构件，流处理kafka输出的数据，并将处理完的数据回流kafka作暂时缓存，这样可以让连接kafka的其他teams都可以共享处理后的数据
5. 搭建redis存储系统，从kafka读取处理完的数据，以减轻kafka压力，并输出到前端
6. 用nodejs搭建简单的前端应用，并利用smoothie模版实现data visualization
