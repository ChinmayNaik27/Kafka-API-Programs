from kafka import KafkaProducer
topicname='chinmay'
boot_ser=['localhost:9092']
producer=KafkaProducer(bootstrap_servers=boot_ser)
producer.send(topicname,b'Welcome Buddy , This is Kafka Enviornment Dude!!')
print("Message Sent!!")
producer.flush()
producer.close()