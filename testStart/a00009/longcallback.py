# coding: utf-8
import pika


def consume_msg():
    parameters = pika.URLParameters('amqp://tjhb:daochi12e@mqi.sgate.taijihuabao.com:5672/tjhb')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    queue = "wxasrlong"
    key = 'wxasrlong'
    channel.queue_declare(queue=queue, exclusive=True)
    channel.queue_bind(queue=queue, exchange='sgate.topic', routing_key=key)

    def callback(ch, method, properties, body):
        print(" [x] Received %s" % body.decode())

    channel.basic_consume(callback, queue=queue, no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consume_msg()
