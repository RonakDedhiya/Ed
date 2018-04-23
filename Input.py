import requests
import json
import pandas as pd
import numpy as np
from time import sleep
df = pd.read_csv("Dataset/high_ram_normal_cpu_normal_network.csv")
#df=pd.read_csv("test.csv")
RAM = np.array(df['Available MBytes'])
CPU = np.array(df['Processor Time'])
Network=np.array(df['KBytes Total'])

for i in range(0,RAM.size):
    dataRAM=int(RAM[i])
    dataCPU=int(CPU[i])
    dataNetwork=int(Network[i])

    payload=json.dumps({"CPU_Value":dataCPU,"Available_RAM":dataRAM,"Network_Bytes":dataNetwork})
    print(payload)

    url = "http://localhost:9000/"

    headers = {
    'content-type': "application/json"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    #sleep(1)
