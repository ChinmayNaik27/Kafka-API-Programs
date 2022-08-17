#basic Consumer!!

"""from kafka import KafkaConsumer

consum=KafkaConsumer('chinmay')

for x in consum:
    print(x)"""

from kafka import KafkaConsumer as k

# import sys
bootstrap=['localhost:9092']
topicname='chinmay'
consumer=k(topicname,group_id='test-consumer-group',bootstrap_servers=bootstrap)
for msg in consumer:
    print(type(msg))
    print(f"Topic name={msg.topic},Message={msg.value}")
# sys.exit()