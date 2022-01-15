import order_pb2
from kafka import KafkaConsumer
consumer = KafkaConsumer('da-orders', bootstrap_servers='localhost:29092')

for msg in consumer:
    o = order_pb2.Order()
    o.ParseFromString(msg.value)
    print(o.custID)