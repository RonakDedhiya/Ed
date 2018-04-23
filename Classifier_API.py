import pickle
from flask import Flask
from flask import request
app = Flask(__name__)


class_names=["Normal",
            "NoNetwork",
            "HighRAM",
            "HighRAM_NoNetwork",
            "HighCPU",
            "HighCPU_NoNetwork",
            "HighCPU_HighRAM",
            "HighCPU_HighRAM_NoNetwork"]



file_name="Classifier_model"
with open(file_name, 'rb') as file:  
    clf= pickle.load(file)

result=clf.predict([[410,34,0]])
out_prev="Normal"

@app.route('/',methods=['POST'])
def hello_world():
    global out_prev
    content=request.json
    CPU_Value=content["CPU_Value"]
    Available_RAM=content["Available_RAM"]
    Network_Bytes=20
    result=clf.predict([[Available_RAM,CPU_Value,Network_Bytes]])
    out=class_names[int(result)]
    print(out)
    if out_prev != out:
        out_prev=out
        if result not in [0,4]:
            return "mqtt:"+out
    return out

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=9000)
