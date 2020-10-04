import json
import xmltodict

with open("books.xml") as xmlfile:
	data_dict=xmltodict.parse(xmlfile.read())
	xmlfile.close()
json_data=json.dumps(data_dict)

with open("xml2json.json","w") as jsonfile:
	jsonfile.write(json_data)
jsonfile.close()