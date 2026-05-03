import action as act

class to_do:
    def __init__(self):
        pass

    def add_new_todo(self):
        print("Need few informations while creating the list....")
        user_input_title = input("Enter the title of the to_do: ")
        user_input_status = input("Enter the status of the to_do: ")
        user_input_remark = input("Enter the remark for the to_do (remark cannot be empty for status blocked): ")
        data = act.action_items("", user_input_title, user_input_status, user_input_remark)
        
        post_data = data.post_new_record()
        print("Acknowledgement: "+ post_data)
        print("created new to_do and updated in the Local DB")

    def get_all_todo(self):
        data = act.action_items()
        data_context = data.get_all_records()
        data_count = len(data_context)
        if data_count>1:
            self.output_format(data_context)
        else:
            print("Currently there are no data stored in the DB")
        print("Fetched all the to_do in the local DB")

    def get_one_todo(self):
        user_getbyid, user_getbytitle = "",""
        print("would you like to search by id or title:")
        print("press 1 for get to_do by id \npress 2 for get to_do by title")
        user_input = int(input("Press the respective number: "))
        if user_input == 1:
            user_getbyid = input("Enter the to_do id: ")
        elif(user_input == 2):
            user_getbytitle = input("Enter the to_do title: ")
        data = act.action_items(user_getbyid, user_getbytitle)
        self.output_format(data.get_one_record())
        print("Fetched the desired to_do from the lost of to_do")

    def output_format(self, raw_formated_data):
        for value in raw_formated_data:
            print(value)

    def update_one_todo(self):
        print("Updated the specific To_do")

    def delete_one_todo(self):
        print("Deleted the To_do")

    def delete_all_todo(self):
        print("Deleted all the to_do")


if __name__ == "__main__":

    print("Welcome to local To_DO app...")
    print("*"*20)
    while True:
        print("\nPlease find the action options from below\n")
        print("1. Get all to_do's \n2. Get a specific to_do \n3. Create a new to_do \n4. Update an existing to_do \n5. Delete a to_do \n6. Delete all to_do \n7. Exit application")
        try:
            user_action_input = int(input("Please enter what you choose choose by selecting the correct choise between 1-7: "))
        except(ValueError):
            print("we Expect only the numbers as our input. Hence next time please choose the option by entering the number")
        except(NameError):
            print("Entered choice is not exactly correct please check your input")
        todo_actions = to_do()
        if (user_action_input == 1):
            print ("Getting all the to_do's ...")
            todo_actions.get_all_todo()
        
        elif (user_action_input == 2):
            print ("Getting a specific to_do ...")
            todo_actions.get_one_todo()

        elif (user_action_input == 3):
            print ("Creating a new to_do ...")
            todo_actions.add_new_todo()

        elif (user_action_input == 4):
            print ("Updating a specific to_do ...")
            todo_actions.update_one_todo()

        elif (user_action_input == 5):
            print ("Deleting a specific to_do ...")
            todo_actions.delete_one_todo()

        elif (user_action_input == 6):
            print ("Deleting all to_do ...")
            todo_actions.delete_one_todo()

        elif (user_action_input == 7):
            print("*"*20)
            print("please come back later...")
            print("Thanks")
            print("*"*20)
            break
        else:
            print("Wrong choice remember enter the number between 1-7 to perform the exact action....")
            continue
        

        