
# Chapter 2 - Installing Kafka
**My Installation**
* `brew install zookeeper`
* confirm the java_home
* go to `/opt/homebrew/Cellar/zookeeper/3.7.0_1/bin`
* we can use `zkServer start` or `zkServer stop` to start/stop service
* when we start, we found that zookeeper is using default config file located at
`/opt/homebrew/etc/zookeeper/zoo.cfg`
we add following config into it
```
dataDir=/Users/eric.wang/Desktop/zookeeper_data
```
* To verify if zookeeper is running, first to install telnet
* `brew install telnet`
* `telnet loclahost 2181` then `srvr`
* download kafka `brew install kafka`
* change kafka setting to enable advertised port
* ```
  advertised.listeners=PLAINTEXT://localhost:9092
  ```
* run kafka `opt/homebrew/Cellar/kafka/3.3.1_1/bin/kafka-server-start -daemon libexec/c
onfig/server.properties`
* create topic, when run 
```
/opt/homebrew/Cellar/kafka/3.3.1_1/bin/kafka-topics \
--create --bootstrap-server localhost:9092 \
--replication-factor 1 \
--partitions 1 \
--topic test
```
running into error of broker may not be available
**Topic defaults**
* num.partitions
  * partition can only increase not decrease.
  * how to choose correct partition depends on several factors:
    * What is the maximum throughput you expect to achieve when
consuming from a single partition? You will always have, at
most, one consumer reading from a partition, so if you know
that your slower consumer writes the data to a database and
this database never handles more than 50 MB per second from
each thread writing to it, then you know you are limited to
60MB throughput when consuming from a partition.
    * if I want to be able to write and read 1 GB/sec from a topic, and I
know each consumer can only process 50 MB/s, then I know I need
at least 20 partitions. 
* log.retention.ms
  * describe the amount of time after which messages will be deleted
  * the default specified in the configuration file `log.retention.hours` is 168 hours - one week
  * but there are other parameters allowed `log.retention.minutes`, `log.retention.ms`, but 
    recommend to use `log.retention.ms` as the smaller unit size will take precedence if more
    than one is specified. 
* log.retention.bytes
  * apart from retention, another way to expire message is based the total bytes of message.
    This value applies to per-partition. So if `log.retention.bytes` is set to 1GB, and
    a topic has 8 partitions, then the data retained for the topic is 8GB
* If both `log.retention.ms` and `log.retention.bytes` are defined, then the topic will be deleted
  when either condition met.
* log.segment.byte
  * interesting topic, but too long, review later
  * question, if log.segment.bytes is 1G, log.retention.ms is 1 week, producer produce 100 mb preday,
    when will the message is going to be deleted ? why. answer is 17 day
  * default - 1GB
* log.segment.ms
  * default none
* message.max.bytes
  * default 1mb. will receive error from broker if the size is bigger than this. it is after compressed value.