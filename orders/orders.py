import order_pb2

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:29092')

from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import random
import time

SYMBOLS = ['GOOG', 'MSFT', 'CRM', 'AAPL', 'AMZN', 'FB', 'NVDA', 'JPM', 'BABA']
CUSTOMERS = ['DODGY', 'WODGY', 'BOOBIE', 'KYRA', 'BABA', 'CORNO', 'ELLA', 'LILLY']
ACTIONS = [order_pb2.Action.BUY, order_pb2.Action.SELL]

def main():
    
    while True:

        t = datetime.now()
        seconds = int(t.timestamp())
        nanos = int(t.timestamp() % 1 * 1e9)

        o = order_pb2.Order(
            symbol = random.choice(SYMBOLS),
            custID = random.choice(CUSTOMERS),
            action = random.choice(ACTIONS),
            quantity = random.randint(100, 1000),
            orderTime = Timestamp(seconds=seconds, nanos=nanos)
        )

        # Send to Kafka

        producer.send('da-orders', o.SerializeToString())
        print(f"Sent to Kafka topic {o.orderTime}")
        # f = open('test2.bin', 'ab')
        # f.write(o.SerializeToString())
        # f.close()

        time.sleep(2)
        

    

if __name__ == "__main__":
    main()



# orderSample = {
#     "symbol" : "GOOG",
#     "action": "BUY",
#     "quantity": 100,
#     "orderTime" : "2022-01-09T13:15:00Z",
#     "custID": "DODGY"
# }