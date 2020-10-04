import csv
import json
import os

def make_json(csvfilepath,jsonfilepath):
	data={}
	

	with open(csvfilepath,encoding='utf-8') as csvf:
		
		csvreader=csv.DictReader(csvf)
		for index,row in enumerate(csvreader):
			condition=row["condition"]
			condition_cui=row["condition_cui"]
			if(index==0):
				data[condition]={}
				data[condition]["cui"]=condition_cui
				data[condition]["have_had"]={}
				data[condition]["looking_for"]={}

			data[condition][row["label_bucket"]][row["label"]]={}
			data[condition][row["label_bucket"]][row["label"]]["cui"]=row["label_cui"]
			data[condition][row["label_bucket"]][row["label"]]["score"]=row["label_score"]
			data[condition][row["label_bucket"]][row["label"]]["label_semantic_types"]=row["label_semantic_types"]
			data[condition][row["label_bucket"]][row["label"]]["label_ncts_counts"]=row["label_ncts_count"]
			data[condition][row["label_bucket"]][row["label"]]["ncts"]=row["label_ncts"]
	#print(data)
	return data	
	#json.dumps(data)

file_names=os.listdir(r'csvfiles/')

	
working_dir=r'csvfiles/'
data={}
for x in file_names:
	
	csvfilepath=os.path.join(working_dir,x)
	print(csvfilepath)
	jsonfilepath='convertedfiles/my{}.json'.format(x)
	data.update(make_json(csvfilepath,jsonfilepath))
with open("combined.json",'w',encoding="utf-8") as js:
	js.write(json.dumps(data,sort_keys=True,indent=4))

#json.dump(data,out_file,indent=4)