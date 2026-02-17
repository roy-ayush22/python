todos = []

try:
     with open("todos.txt", "r") as file:
          for line in file:
               todos.append(line.strip())
except FileNotFoundError:
     pass

def main():
    show_menu()
    handle_task()
    

def handle_task():
            while True:
                choice = int(input("enter choice: "))
                if choice == 1:
                    task = input("enter task: ")
                    todos.append(task)
                    save_todos()
                    print("todo added!")
                
                elif choice == 2:
                    if len(todos) == 0:
                        print("no todos yet")
                    else:
                        for i in range(len(todos)):
                            print(f"{i+1}. {todos[i]}")

                elif choice == 3:
                    print("goodbye")
                    break
                    
def show_menu():
    print("1. add todo")
    print("2. view todo")
    print("3. exit")

def save_todos():
     with open("todos.txt", "w") as file:
          for todo in todos:
               file.write(todo + "\n")
        

main()