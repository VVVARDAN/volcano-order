from kubernetes import client, config
import time
import os

'''
TODO
# params = os.environ.get("PARAMS", "")
# order = params
# print(params)
'''
config.load_incluster_config()


cnt = 30


while cnt!=0:
    cur_pod_name = "master"
    v1 = client.CoreV1Api()
    current_namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
    pods = v1.list_namespaced_pod(current_namespace).items
    flag = True
    flag = any(cur_pod_name in i.metadata.name and i.status.phase == "Running" for i in v1.list_namespaced_pod(current_namespace).items)

    
    
    if flag == True:
        break

    time.sleep(2)
    cnt-=1
