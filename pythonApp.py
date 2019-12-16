import sqlite3 as lite

class DatabaseManage(object):
    def __init__(self):
        global conn
        try:
            conn = lite.connect('fileDB.db')
            with conn:
                curr = conn.cursor()
                curr.execute("CREATE TABLE IF NOT EXISTS test(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1 )")
        except Exception as e:
            print("Unable to create a DB !")
    
    def insert_data(self, data):
        try:
            with conn:
                curr = conn.cursor()
                curr.execute(
                    "INSERT INTO test (name, description, price, is_private) VALUES (?,?,?,?)",
                    data
                    )
                return True
        except Exception as identifier:
            return False
    def fetch_data(self):
        try:
            with conn:
                curr = conn.cursor()
                curr.execute("SELECT * FROM test")
                return curr.fetchall()
        except Exception as identifier:
            return False
    def delete_data(self, id):
        try:
            with conn:
                curr = conn.cursor()
                sql = "DELETE FROM test WHERE id = ?"
                curr.execute(sql, [id])
                return True
        except Exception as identifier:
            return False

def main():
    print("*"*40)
    print("\n:: Course Management :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\n1. Insert a new Course\n')
    print('2. Show all courses\n')
    print('3. Delete a course (NEED ID OF COURSE)\n')
    print("#"*40)
    

    choice = input("Enter a choice: ")
    
    while(True):

        if choice == "1":
            name = input("Enter course name: ")
            desc = input("Enter course description: ")
            price = input("Enter course price: ")
            private = input("Is this course private(0/1): ")

            if db.insert_data([name, desc, price, private]):
                print("Course was inserted successfully")
            else:
                print("OOPS SOMETHING IS WRONG")

        elif choice == "2":
            print(":: Course List ::")
            for index, course in enumerate(db.fetch_data()):
                print("Serial no. : ", str(index+1))
                print("Course ID : ", str(course[0]))
                print("Course Name : ", str(course[1]))
                print("Course Description : ", str(course[2]))
                print("Course Price : ", str(course[3]))
                private = 'Yes' if course[4] else 'No'
                print("Is Private : ", private)
                print("\n")
               
        elif choice == "3":
            record_id = input("Enter the course ID: ")

            if db.delete_data(record_id):
                print("Course was successfully deleted")
            else:
                print("OOPS SOMETHING WENT WRONG")

        else:
            print("BAD CHOICE")

        
        choice = input("Enter Choice or enter 4 to exit : ")
        if choice == "4":
            break
        else:
            continue

if __name__ == "__main__":
    main()   
    