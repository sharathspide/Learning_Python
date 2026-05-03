import json

class json_file_handle():

    def __init__(self, file_access_mode: str, data_context: any = ""):
        self.file_name = "to_do_data.json"
        self.file_location = None
        self.file_access_mode = file_access_mode
        self.data_context = data_context

    def read_json(self):
        try:
            if (self.file_access_mode == "r"):
                filename = self.fileNameMaker()
                with open(filename, self.file_access_mode) as file:
                    return json.load(file)
        except:
            print("something went wrong while trying to read the json file...")
    
    def write_to_json(self):
        if(self.file_access_mode == "w" or self.file_access_mode == "a"):
            filename = self.fileNameMaker()
            with open(filename, self.file_access_mode) as file:
                json.dump(self.data_context, file)
                acknowledgement = "Data Inserted successfully..."
                return acknowledgement

    
    def fileNameMaker(self):
        if (self.file_location != None):
            #print(self.file_location+"testing")
            filename = self.file_location+"/"+self.file_name
            return filename
        else:
            filename = self.file_name
            return filename
        
if __name__ == "__main__":
    file = json_file_handle("r","")
    test_get_data = file.read_json()
    print (test_get_data)




