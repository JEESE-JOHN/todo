import os

class Configurations:
    # Simplified verification for checking debug mode/environment
    debug = True 
    environment = 'LOCAL'
    # Kafka/ElasticSearch/etc are disabled for this simple todo app implementation
    kafka = {'enable': False}
