
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
~~running into error of broker may not be available~~. Solved by setting JAVA_HOME correctly
`export JAVA_HOME=$(/usr/libexec/java_home)`

I spent a lot of time to build up connection. Worth reading this [blog](https://www.confluent.io/blog/kafka-listeners-explained/) 
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

**producer config**
* ack
  * The acks parameter controls how many partition replicas 
     must receive the record before the producer can consider the write successful
  * ack=0, the producer will not wait for a reply from the broker before assuming the message was sent 
    successfully. this means that if something went wrong and the broker did not receive the message
    the producer will not know about it
  * ack=1, the producer will receive a success response from the broker the moment the leader replica
    received the message. producer will retry sending the message if message can't be written into
    the leader. Throughput will be impacted between asyn and sync approach, for sync approach, the 
    latency will increase significantly because producer is waiting for the response form broker 
    confirmation. if async, the latency is hidden.
  * ack=all, safest option but latency will be even higher compare to ack=1
  ...
* producer ordering guarantee
Apache Kafka preserves the order of messages within a partition. 
This means that if messages were sent from the producer in a specific order, 
the broker will write them to a partition in that order and all consumers will read 
them in that order. For some use cases, order is very important. 
There is a big difference between deposit‐ ing $100 in an account and later withdrawing it, 
and the other way around! However, some use cases are less sensitive.
Setting the retries parameter to nonzero and the max.in.flights.requests.per.session 
to more than one means that it is possible that the broker will fail to write the
first batch of messages, succeed to write the second (which was already in- flight), 
and then retry the first batch and succeed, thereby reversing the order.
Usually, setting the number of retries to zero is not an option in a reliable system, 
so if guaranteeing order is critical, we recommend setting in.flight.requests.per.session=1 to make sure that while a 
batch of messages is retrying, additional messages will not be sent 
(because this has the potential to reverse the correct order). 
This will severely limit the throughput of the producer, 
so only use this when order is important.

**Consumer**
* When a consumer leave or join a consumer group, it is moving partition ownership from one consumer 
to another, it is called rebalance. Rebalance is normally fairly undesirable, as during rebalance,
consumer can't consume messages so rebalance is basically a short window of unavailablility 
of the entire consumer group.  
The way consumer maintain membership in a consumer group and ownership of partition assigned 
to them is by sending heartbeats to a kafka broker designated as the group coordinator (this broker
can be different for consumer groups)
When a consumer join the group, it sends a JoinGroup request to the request coordinator. 
The first consumer join the group become the group leader. The leader will receive a list of all
consumers in the group from the group coordinator. It then responsible for assigning a subset of 
partitions of each consumer.
* commit offset
  * auto commit
  * sync commit
  * async commit
  * combine together

## Chapter 5 - Kafka internals
* The controller. The controller is one of the kafka brokers that, in additional to the 
usual broker functionality, it is responsible for electing partition leader. All brokers
join in cluster, they will try to create an ephemeral node in ZooKeeper, but only the first one will
succeed others will receive "node already exists" exception which causes them to realise that 
the controller node already exists.
When the controller broker loses connectivity, the ephemeral node will disappear, other brokers 
will be notified through the Zookeeper watch and will attempt to create a controller. Again, first
come first served.
All partitions that had a leader on the old broker will need to choose a new leader, it will simply
go to the next replica in the replica list of that partition.

*Replication
  * Leader replica, responsible for client requests
    * follower replica, not handling client requests. Followers attempt to stay up-to-date by 
      replicating all the messages from the leader as messages arrive but they can fail to stay in sync
      for various reason.
      How followers update to date? it will send fetch requests to leader, 
      and the leader will send the message back in response. The messages are in order
      for example, a replica request message 1, then message 2, and then message 3, it will
      not request message 4 before it get all previous message. So leader know that how far 
      each relica is. If a replica hasn't requested a message in more than 10 secs or hasn't 
      caught up to the most recent messages in more than 10 seconds, the replica is considered 
      out of sync. If a replica out of sync, it can no longer become the new leader in the 
      event of failure.
      Each partition has a preferred leader-the replica that was the leader when the topic was
      originally created, it is preferred because when partitions are first created, the leaders are 
      balanced between brokers.
* Compaction
  * delete. which deletes events older than retention time
  * compact, which only store the most recent value for each key in the topic. 
    * user case can be - client only need to remember the most recent shipping address.
    * messages that have been compacted are called clean, messages received after the last compaction
      is called dirty. When topics compacted are decided by `min.cleanable.dirty.ratio` , default is 50% which mean,
      once 50% of the topic contains dirty records, it will perform compaction.