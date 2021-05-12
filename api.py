import requests

dict={'5ea0abd3d43ec2250a483a4f': 'ariyalur', '5ea0abd4d43ec2250a483a61': 'chengalpattu', '5ea0abd2d43ec2250a483a40': 'chennai', '5ea0abd3d43ec2250a483a4a': 'coimbatore', '5ea0abd3d43ec2250a483a50': 'cuddalore', '5ea0abd2d43ec2250a483a43': 'dharmapuri', '5ea0abd3d43ec2250a483a4b': 'dindigul', '5ea0abd2d43ec2250a483a48': 'erode', '5ea0abd4d43ec2250a483a5f': 'kallakurichi', '5ea0abd2d43ec2250a483a41': 'kancheepuram', '5ea0abd3d43ec2250a483a5c': 'kanniyakumari', '5ea0abd3d43ec2250a483a4c': 'karur', '5ea0abd3d43ec2250a483a5d': 'krishnagiri', '5ea0abd3d43ec2250a483a56': 'madurai', '60901c5f2481a4362891d572': 'mayiladuthurai', '5ea0abd3d43ec2250a483a51': 'nagapattinam', '5ea0abd2d43ec2250a483a47': 'namakkal', '5ea0abd3d43ec2250a483a49': 'nilgiris', '5ea0abd3d43ec2250a483a4e': 'perambalur', '5ea0abd3d43ec2250a483a54': 'pudukkottai', '5ea0abd3d43ec2250a483a59': 'ramanathapuram', '5ea0abd4d43ec2250a483a63': 'ranipet', '5ea0abd2d43ec2250a483a46': 'salem', '5ea0abd3d43ec2250a483a55': 'sivagangai', '5ea0abd4d43ec2250a483a60': 'tenkasi', '5ea0abd3d43ec2250a483a53': 'thanjavur', '5ea0abd3d43ec2250a483a57': 'theni', '5ea0abd3d43ec2250a483a4d': 'thiruchirappalli', '5ea0abd4d43ec2250a483a62': 'thirupathur', '5ea0abd3d43ec2250a483a52': 'thiruvarur', '5ea0abd3d43ec2250a483a5a': 'thoothukudi', '5ea0abd3d43ec2250a483a5b': 'tirunelveli', '5ea0abd4d43ec2250a483a5e': 'tiruppur', '5ea0abd1d43ec2250a483a3f': 'tiruvallur', '5ea0abd2d43ec2250a483a44': 'tiruvannamalai', '5ea0abd2d43ec2250a483a42': 'vellore', '5ea0abd2d43ec2250a483a45': 'villupuram', '5ea0abd3d43ec2250a483a58': 'virudhunagar'}

district_dict = {value:key for key, value in dict.items()}

def RUN(district):
    try:
        ret={}
        ret["Credits"]="API developed by SAYAD PERVEZ - sayadpervez.b.2019.ece@rajalakshmi.edu.in / pervez2504@gmail.com"
        ret['District name']=district
        ret["Hospitals"]={}                  # oiesdhfcisdn
        url = r'https://tncovidbeds.tnega.org/api/hospitals'
        d = {
        "searchString":"",
        "sortCondition":{"Name":1},
        "pageNumber":1,
        "pageLimit":10,
        "SortValue":"Availability",
        "Districts":[f"{district_dict[district]}"],
        "BrowserId":"b4c5b065a84c7d2b60e8b23d415b2c3a",
        "IsGovernmentHospital":"true",
        "IsPrivateHospital":"true",
        "FacilityTypes":["CHO","CHC","CCC"]
        }

        for ii in range(1,11):

            d["pageNumber"]=ii
            res = requests.post(url, json=d)
            object = res.json()
            result_list = object['result']

            for _ in result_list:
                (ret["Hospitals"])[(_["Name"]).replace(",","-")]={"Hospital Name":(_["Name"]).replace(",","-"),"District Name":(_["District"])["Name"],"Total Vacant Beds":str((_["CovidBedDetails"])["TotalVaccantBeds"])}
        return(ret)
    except Exception as e:
        return({"Error":str(e)})


'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''
#uvicorn api:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/all")
@app.get("/list")
async def all():
    return {"Credits":"API developed by SAYAD PERVEZ - sayadpervez.b.2019.ece@rajalakshmi.edu.in / pervez2504@gmail.com","list": list(district_dict.keys())}

@app.get("/hi")
async def hi():
    return({"Message":"Hi","Credits":"API developed by SAYAD PERVEZ - sayadpervez.b.2019.ece@rajalakshmi.edu.in / pervez2504@gmail.com"})

@app.get("/{districtname}")
async def pervez(districtname):
    if(districtname in district_dict.keys()):
        return(RUN(districtname))
    else:
        return({"Credits":"API developed by SAYAD PERVEZ - sayadpervez.b.2019.ece@rajalakshmi.edu.in / pervez2504@gmail.com","Exception":"Invalid District"})
