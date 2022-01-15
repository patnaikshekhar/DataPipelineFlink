from stock_pb2 import Stock

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:29092')

from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import random
import time

SYMBOLS = ['GOOG', 'MSFT', 'CRM', 'AAPL', 'AMZN', 'FB', 'NVDA', 'JPM', 'BABA']
PRICES = [(1700, 2800), (314, 324), (218, 307), (130, 182), (3100, 3700), (250, 376), (115, 346), (127, 172), (106, 274)]

def main():
    
    while True:

        t = datetime.now()
        seconds = int(t.timestamp())
        nanos = int(t.timestamp() % 1 * 1e9)

        index = random.randint(0, len(SYMBOLS) - 1)
        low, high = PRICES[index]

        s = Stock(
            symbol = SYMBOLS[index],
            price = random.randint(low, high),
            time = Timestamp(seconds=seconds, nanos=nanos)
        )

        # Send to Kafka

        producer.send('da-stock', s.SerializeToString())
        print(f"Sent to Kafka topic {s.time}")

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