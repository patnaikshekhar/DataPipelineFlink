from stock_pb2 import Stock
from kafka import KafkaConsumer
consumer = KafkaConsumer('da-stock', bootstrap_servers='localhost:29092')

for msg in consumer:
    s = Stock()
    s.ParseFromString(msg.value)
    print(s)