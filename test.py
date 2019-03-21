#!/usr/bin/env python3
# coding=utf-8

import argparse


__version__ = '0.0.2'

def telemetry(project_id, topic_name):
    # [START telemetry]
    from google.cloud import pubsub_v1
    import RPi.GPIO as GPIO
    import time
    import os
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pubsubcredentials.json"

    # Set up PIN 21 as input
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21, GPIO.IN)	

    project_id = "appliedautonomybackend"
    topic_name = "iot-test-topic"
    
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = subscriber.topic_path(project_id, topic_name)

    def callback(message_future):
        # When timeout is unspecified, the exception method waits indefinitely.
        if message_future.exception(timeout=30):
            print('Publishing message on {} threw an Exception {}.'.format(
                topic_name, message_future.exception()))
        else:
            print(message_future.result())

    # Every second read input
    while True:
        val = GPIO.input(21)
        print('GPIO21 = {}', format(val))

        # Publish messages.
        data = u'GPIO21: {}'.format(val)
        # Data must be a bytestring
        data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        message_future = publisher.publish(
            topic_path, data=data) #, timestamp=time.time(), description='IoT test GPIO telemetry')
        message_future.add_done_callback(callback)
        print('Published {} of message ID {}.'.format(data, message_future.result()))    
        time.sleep(1)
    # [END telemetry]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('project_id', help='Your Google Cloud project ID')
    parser.add_argument('topic_name', help='Your topic name')
    args = parser.parse_args()

    telemetry(args.project_id, args.topic_name)