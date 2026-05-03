import repository as rep
import app as app
class action_items:

    def __init__(self, id:str = "", title:str = "", status = "", remark = ""):
        self.record_id = id
        self.record_title = title
        self.record_status = status
        self.record_remark = remark

    def fetch_all_records(self):
        file_access_mode = "r"
        file = rep.json_file_handle(file_access_mode,"")
        raw_data = file.read_json()
        return raw_data

    def get_all_records(self):
        return self.__processed_get_data(self.fetch_all_records())
    
    def get_one_record(self):
        return self.__processed_get_data(self.__find_record(self.fetch_all_records()))

    def post_new_record(self):
        modified_data = self.fetch_all_records()
        new_data = self.__mapdata()
        modified_data.append(new_data)
        file_access_mode = "w"
        file = rep.json_file_handle(file_access_mode, modified_data)
        return file.write_to_json()

    def __mapdata(self):
        new_data = {}
        new_data["id"] = self.create_new_id()
        new_data["title"] = self.record_title
        if (self.record_status == "Blocked" and self.record_remark == ""):
            print("please help to add the remark for why the status of the to_do task is blocked...")
            self.record_remark = input("You can enter the remark below")
            if (self.record_remark == ""):
                 again = app.to_do()
                 again.add_new_todo()
        new_data["status"] = self.record_status
        new_data["remark"] = self.record_remark
        return new_data

    def create_new_id(self):
        records = self.fetch_all_records()
        existing_ids = []
        if records != []:
            for record in records:
                existing_ids.append(record["id"])
        else:
            return 1
        print(existing_ids)
        return max(existing_ids)+1

    def __find_record(self, raw_data:list):
        for value in raw_data:
            if (self.record_id != "" and self.record_title == ""):
                #7print(value)
                print(self.record_id)
                print(value["id"])
                if value["id"] == int(self.record_id):
                    return value
            elif (self.record_id == "" and self.record_title != ""):
                if value["title"] == self.record_title:
                    return value
            else:
                return {}
        
    def __processed_get_data(self, raw_data):
        # print(raw_data)
        processed_data = []
        if raw_data == None or raw_data==[] or raw_data == {}:
            print("raw_data==> none or [] or '{'}")
            return processed_data
        elif (type(raw_data) == dict):
            content = f"TO_DO - ID: {raw_data.get("id")} || title: {raw_data.get("title")} || status = {raw_data.get("status")} || remark = {raw_data.get("remark")}"
            processed_data.append(content)
        else:    
            for data in raw_data:
                content = f"TO_DO - ID: {data["id"]} || title: {data["title"]} || status = {data["status"]} || remark = {data["remark"]}"
                processed_data.append(content)
        return processed_data
    

if __name__ == '__main__':
    testing = action_items("","testing 1", "pending", "")
    id = testing.create_new_id()
    print (id)