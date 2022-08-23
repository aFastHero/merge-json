import sys
import json
import os

folder_name = sys.argv[1]
new_file_name = sys.argv[2]

def main():

    fileList = []
    for filenames in os.walk(folder_name):
        
        fileList.append(filenames)

    data_list = []
    for i in range(len(filenames[2])):
        
        try:

            data = json.load(open(folder_name + '/' + filenames[2][i], encoding='utf-8'))
            data_final = dict((k, data[k]) for k in ("attributes","image","name","description"))

            attributes = []
            for i in range(len(data_final["attributes"])):

                try:
                    
                    props = attributes[i]
                    props_final = dict((k,props[k]) for k in ("trait_type","value"))
                    
                    trait_list = []
                    for i in range(len(attributes)):
                        trait_list.append(props_final["trait_type"][i]["value"])
                    props_final["trait_type"] = trait_list

                    attributes.append(props_final)
                except Exception:
                    pass

                attributes.append(data_final["attributes"][i])
            data_final["attributes"] = attributes

            data_list.append(data_final)
        except Exception:
            pass

    out_file = open(new_file_name + ".json", "w")
    json.dump(data_list, out_file, indent=2)
    out_file.close()


if __name__ == '__main__':
    main()