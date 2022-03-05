import json
str1 = '{"taskCodeList":["invite_win_plant_level1","invite_win_plant_level2","send_vip_invite_register"],"userActiviyStatus":""}'

data_json = json.loads(str1)
print(data_json)