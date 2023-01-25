from db.consumer import Consumer

def main():
    consumer = Consumer('transactions')
    consumer.read()


if __name__ == '__main__':
    main()
