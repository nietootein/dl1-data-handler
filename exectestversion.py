from dl1_data_handler.version import get_version
import json 
  
aux = get_version(pep440=False)
print('aux')
print(aux)
details = {'version': aux}  
with open('dl1_data_handler/testversion.py', 'w') as convert_file: 
     convert_file.write(json.dumps(details))
