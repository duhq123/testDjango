#!/usr/bin/env python
# coding=utf8
import pika

# if __name__ == '__main__':

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 使用队列
# channel.queue_declare(queue='hello')
#
# channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()



#定义交换机
channel.exchange_declare(exchange='messages', type='fanout')

#将消息发送到交换机
channel.basic_publish(exchange='messages', routing_key='', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()