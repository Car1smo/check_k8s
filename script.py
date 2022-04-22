import ConfigParser
import subprocess


config = ConfigParser.RawConfigParser()

config.read('k8s.config')  
client_count_kafka = (int(config.get('k8s.pods.number', 'kafka'))) 
k8s_count_kafka = (int(subprocess.check_output("kubectl describe statefulset timeseries-kafka | grep 'Pods Status: .*$' | awk '{print $3}'", shell=True)))  

print('<__Kafka__>')
print('')
print('Client count:')
print(client_count_kafka)
print('K8s count:')
print(k8s_count_kafka)
print("")

if client_count_kafka == k8s_count_kafka:
    print('Compare result: Ok')
else:
    print('Compare result: Not ok')

print('----------------------------------')

client_count_gateway = (int(config.get('k8s.pods.number', 'gateway')))
k8s_count_gateway = (int(subprocess.check_output("kubectl describe deployment timeseries-gateway | grep 'Replicas: .*$' | awk '{print $2}'", shell=True)))

print('<__Gateway__>')
print('')
print('Client count:')
print(client_count_gateway)
print('K8s count:')
print(k8s_count_gateway)
print("")

if client_count_gateway == k8s_count_gateway:
    print('Compare result: Ok')
else:
    print('Compare result: Not ok')
    
print('----------------------------------')

client_count_pipeline = (int(config.get('k8s.pods.number', 'pipeline')))
k8s_count_pipeline = (int(subprocess.check_output("kubectl describe deployment timeseries-pipeline | grep 'Replicas: .*$' | awk '{print $2}'", shell=True)))

print('<__Pipeline__>')
print('')
print('Client count:')
print(client_count_pipeline)
print('K8s count:')
print(k8s_count_pipeline)
print("")

if client_count_pipeline == k8s_count_pipeline:
    print('Compare result: Ok')
else:
    print('Compare result: Not ok')

print('----------------------------------')

client_count_cassandra = (int(config.get('k8s.pods.number', 'cassandra')))
k8s_count_cassandra = (int(subprocess.check_output("kubectl describe statefulset timeseries-kafka | grep 'Pods Status: .*$' | awk '{print $3}'", shell=True)))

print('<__Cassandra__>')
print('')
print('Client count:')
print(client_count_cassandra)
print('K8s count:')
print(k8s_count_cassandra)
print("")

if client_count_cassandra == k8s_count_cassandra:
    print('Compare result: Ok')
else:
    print('Compare result: Not ok')

print('----------------------------------')

client_count_query = (int(config.get('k8s.pods.number', 'query')))
k8s_count_query = (int(subprocess.check_output("kubectl describe deployment timeseries-query | grep 'Replicas:.*$' | awk '{print $2}'", shell=True)))

print('<__Query__>')
print('')
print('Client count:')
print(client_count_query)
print('K8s count:')
print(k8s_count_query)
print("")

if client_count_query == k8s_count_query:
    print('Compare result: Ok')
else:
    print('Compare result: Not ok')

print('----------------------------------')
