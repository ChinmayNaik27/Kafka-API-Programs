#reading dat from a file for kafka !!

from kafka import KafkaProducer
import os
topicname='chinmay'
bootser=['localhost:9092']
producer=KafkaProducer(bootstrap_servers=bootser)
os.chdir('E:/Data-main/datakafka/Data-main')
dirs=os.listdir()
for data in dirs:
    with open(data) as f1:
        data=f1.read()
        producer.send(topicname,data.encode())
print("Message Sent")
producer.flush()
producer.close()



