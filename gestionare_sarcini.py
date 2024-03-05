import pickle
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

# serialization, data is saved when the application is turned off
def save_data(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

# deserialization, data is saved when the application is turned on
def load_data():
    try:
        with open('tasks.pkl', 'rb') as f:
            tasks = pickle.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def print_menu():
    print("------ Menu ------")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Quit")

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("------ Tasks ------")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task['descriere']} - {task['data']} - {task['ora']}")
        print("--------------------")

def add_task():
    descriere = input("Type description: ")
    while True:
        data_str = input("Type data (DD-MM-YYYY): ")
        try:
            data = datetime.strptime(data_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Invalid format. The correct format is: (DD-MM-YYYY).")
    while True:
        ora_str = input("Type hour (HH:MM): ")
        try:
            ora = datetime.strptime(ora_str, "%H:%M").time()
            break
        except ValueError:
            print("Invalid format. The correct format is: (HH:MM).")

    task = {'descriere': descriere, 'data': data, 'ora': ora}
    tasks.append(task)
    print("Task has been successfully added.")

def update_task():
    view_tasks()
    if tasks:
        index = int(input("Type the number of task you want to update: ")) - 1
        if 0 <= index < len(tasks):
            descriere = input("Type new description: ")
            while True:
                data_str = input("Type new data (DD-MM-YYYY): ")
                try:
                    data = datetime.strptime(data_str, "%d-%m-%Y").date()
                    break
                except ValueError:
                    print("Invalid format. The correct format is: (DD-MM-YYYY).")
            while True:
                ora_str = input("Type new hour (HH:MM): ")
                try:
                    ora = datetime.strptime(ora_str, "%H:%M").time()
                    break
                except ValueError:
                    print("Invalid format. The correct format is: (HH:MM).")
            tasks[index]['descriere'] = descriere
            tasks[index]['data'] = data
            tasks[index]['ora'] = ora
            print("Task has been successfully updated.")
        else:
            print("The number of task doesn't exist.")

def delete_task():
    view_tasks()
    if tasks:
        index = int(input("Type the number of task you want to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task has been successfully deleted.")
        else:
            print("The number of task doesn't exist.")
    else:
        print("No tasks.")

def button1_click(root):
    new_window = tk.Toplevel(root)
    new_window.title("Application")
    new_window.geometry("600x400")
    listbox = tk.Listbox(new_window, width = 600, height = 400)
    listbox.place(x = 0, y = 0)
    if tasks:
        for task in tasks:
            task_info = f"{task['descriere']} - {task['data']} - {task['ora']}"
            listbox.insert(tk.END, task_info)
    else:
        label = tk.Label(new_window, text = "No tasks.")
        label.pack(padx=10, pady=10)

    button1 = tk.Button(new_window, text="Update a task", command=lambda lb=listbox: button3_click(lb, tasks, new_window), width=10, height=2)
    button1.place(x = 250, y = 270)
    button2 = tk.Button(new_window, text="Delete a task", command=lambda lb=listbox: button4_click(lb, tasks), width=10, height=2)
    button2.place(x = 250, y = 320)

def button2_click(root):
    new_window = tk.Toplevel(root)
    new_window.title("Application")
    new_window.geometry("400x400")

    label1 = tk.Label(new_window, text = "Type description:")
    label1.place(x = 152, y = 20)
    entry1 = tk.Entry(new_window, width = 20)
    entry1.place(x = 120, y = 40)
    label2 = tk.Label(new_window, text = "Type data(DD-MM-YYYY):")
    label2.place(x = 152, y = 65)
    entry2 = tk.Entry(new_window, width = 20)
    entry2.place(x = 120, y = 85)
    label3 = tk.Label(new_window, text = "Type hour(HH:MM):")
    label3.place(x = 152, y = 110)
    entry3 = tk.Entry(new_window, width = 20)
    entry3.place(x = 120, y = 130)
    button = tk.Button(new_window, text = "Add task", command = lambda: button5_click(entry1, entry2, entry3), width = 10, height = 2)
    button.place(x = 150, y = 170)

def button3_click(listbox, tasks, new_window):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No tasks.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]

            new_window = tk.Toplevel(new_window)
            new_window.title("Application")
            new_window.geometry("400x400")

            label1 = tk.Label(new_window, text = "Type description:")
            label1.place(x = 152, y = 20)
            entry1 = tk.Entry(new_window, width = 20)
            entry1.place(x = 120, y = 40)
            label2 = tk.Label(new_window, text = "Type data(DD-MM-YYYY):")
            label2.place(x = 152, y = 65)
            entry2 = tk.Entry(new_window, width = 20)
            entry2.place(x = 120, y = 85)
            label3 = tk.Label(new_window, text = "Type hour(HH:MM):")
            label3.place(x = 152, y = 110)
            entry3 = tk.Entry(new_window, width = 20)
            entry3.place(x = 120, y = 130)
            button = tk.Button(new_window, text = "Update task", command = lambda: button6_click(entry1, entry2, entry3, index), width = 10, height = 2)
            button.place(x = 150, y = 170)
        else:
            tk.messagebox.showinfo("Information", "No task selected to delete.")

def button4_click(listbox, tasks):
    if listbox.size() == 0:
        tk.messagebox.showinfo("Information", "No tasks.")
    else:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            listbox.delete(index)
            del tasks[index]
        else:
            tk.messagebox.showinfo("Information", "No task selected to delete.")

def button5_click(entry1, entry2, entry3):
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    try:
        text2_format = datetime.strptime(text2, "%d-%m-%Y").date()
        text3_format = datetime.strptime(text3, "%H:%M").time()
        task = {'descriere': text1, 'data': text2_format, 'ora': text3_format}
        tasks.append(task)
        tk.messagebox.showinfo("Information", "Task added.")
    except ValueError:
        tk.messagebox.showinfo("Information", "Invalid data or hour format.")

def button6_click(entry1, entry2, entry3, index):
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    try:
        text2_format = datetime.strptime(text2, "%d-%m-%Y").date()
        text3_format = datetime.strptime(text3, "%H:%M").time()
        tasks[index]['descriere'] = text1
        tasks[index]['data'] = text2_format
        tasks[index]['ora'] = text3_format
        tk.messagebox.showinfo("Information", "Task updated.")
    except ValueError:
        tk.messagebox.showinfo("Information", "Invalid data or hour format.")

def main():
    while True:
        print("How do you want to use this application?")
        print("1. Graphic interface")
        print("2. Terminal")
        print("3. Close the application")

        option_graphic = input()

        if option_graphic == '1':
            root = tk.Tk()
            root.title("Application")
            root.geometry("800x600")

            button1 = tk.Button(root, text = "View tasks", command = lambda: button1_click(root), width = 10, height = 2)
            button1.place(x = 350, y = 120)

            button2 = tk.Button(root, text = "Add a task", command = lambda: button2_click(root), width = 10, height = 2)
            button2.place(x = 350, y = 167)

            root.mainloop()
        elif option_graphic == '2':
            while True:
                print_menu()
                option_terminal = input("Choose an option: ")
                if option_terminal == '1':
                    view_tasks()
                elif option_terminal == '2':
                    add_task()
                elif option_terminal == '3':
                    update_task()
                elif option_terminal == '4':
                    delete_task()
                elif option_terminal == '5':
                    save_data(tasks)
                    return
                else:
                    print("Invalid option! Please, try again!")
        elif option_graphic == '3':
            save_data(tasks)
            return
        else:
            print("Invalid option! Please, try again!")

if __name__ == '__main__':
    tasks = load_data()
    main()
