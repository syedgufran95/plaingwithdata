import csv
import json

#y=json.loads(file)
f=csv.writer(open("test30.csv","w"),delimiter=",")
jsonfile=open("aneurysm.json","r")
jsondata=json.load(jsonfile)

jsond=jsondata["aneurysm"]


count=0
data=[]
#for x in jsondata:
#	f.writerow(x.values())

for x in jsondata["aneurysm"]:
	


	if x=="have_had":

		
		for y in jsondata["aneurysm"]["have_had"].keys():
			
			data.append([jsondata["aneurysm"]["have_had"][y]["cui"],
						jsondata["aneurysm"]["have_had"][y]["score"],
						jsondata["aneurysm"]["have_had"][y]["label_semantic_types"],
						jsondata["aneurysm"]["have_had"][y]["label_ncts_counts"],
						[jsondata["aneurysm"]["have_had"][y]["ncts"]]])
			#data.append(jsondata["aneurysm"]["have_had"][y]["score"])
			#data.append([jsondata["aneurysm"]["have_had"][y]["label_semantic_types"]])
			#data.append([jsondata["aneurysm"]["have_had"][y]["label_ncts_counts"]])
			#data.append([jsondata["aneurysm"]["have_had"][y]["ncts"]])
			
for x in data:

	f.writerow(x)
			
	# if x=="looking_for":
	# 	for y in jsondata["aneurysm"]["looking_for"].keys():
			
	# 		data.append([jsondata["aneurysm"]["looking_for"][y]["cui"]])
	# 		data.append([jsondata["aneurysm"]["looking_for"][y]["score"]])
	# 		data.append([jsondata["aneurysm"]["looking_for"][y]["label_semantic_types"]])
	# 		data.append([jsondata["aneurysm"]["looking_for"][y]["label_ncts_counts"]])
	# 		data.append([jsondata["aneurysm"]["looking_for"][y]["ncts"]])
	# 		f.writerow(x for x in data)
	# 		data.clear()
# with open("test30.csv","a") as c:
# 	writer=csv.writer(c)
# 	for x in data:
# 		writer.writerow(x)
# c.close

#f.writerow(["condition","condition_cui","label",
#			"label_cui","label_score","label_semantic_types",
#			"label_ncts","label_bucket","label_ncts_count"])
#print(data)

#for x in data:
	