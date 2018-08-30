from raven import Client

client = Client('https://11d2b3e3afc0dae10b8f63e623ef8d07f668a7ca7b27c625e3bea902784f6e2b:3e3b29ebb231fa4e40a0a083875a15973f112494cb91eaf684160b9f28b19dea@sentry.io/1545')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()