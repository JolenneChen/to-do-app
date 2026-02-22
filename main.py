import tkinter as tk
from tkinter import messagebox

class TodoApp():
    def __init__(self,root:tk.Tk):

        self.root = root
        self.root.title = "Todo list"
        self.root.geometry("500x500")
        self.root.config(bg="#c9d6df")

        title = tk.Label(root, text="To Do list",font=("Helvetica",28,"bold"),bg="#c9d6df", fg="#275061")
        title.pack(pady=20)
        
        # input frame
        input_frame = tk.Frame(root,bg="#c9d6df")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Enter a Task",font=("Ariel",14,"bold"),bg="#c9b6df", fg="#275061").grid(row=0,column=0,padx=5)
        self.task_entry = tk.Entry(input_frame,width=10,font=("Ariel",14,"bold"))
        self.task_entry.grid(row =0,column=1,padx=10)

        # button frame
        button_frame = tk.Frame(root,bg="#c9d6df")
        button_frame.pack(pady= 15)
        add_button = tk.Button(button_frame,text="Add Task",width=12,bg="#4caf50",fg="white",font=("Arioel",12,"bold"),command= self.add_task)
        add_button.grid(row=0,column=0,padx=10)
        
        delete_button = tk.Button(button_frame,text="Delete Task",width=12,bg="#4caf50",fg="white",font=("Arioel",12,"bold"),command= self.delete_task)
        delete_button.grid(row=0,column=1,padx=10)

        # list box frame 
        list_frame = tk.Frame(root)
        list_frame.pack(pady=20)

        self.task_listbox = tk.Listbox(list_frame,width=40,height=10,font=("Ariel",14),bg="#2f5061",activestyle="none")
        self.task_listbox.pack(side=tk.LEFT)
        scroll_bar = tk.Scrollbar(list_frame)
        scroll_bar.pack(side=tk.RIGHT , fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.task_listbox.yview)


    def add_task(self):
        task = self.task_entry.get().strip()

        if task =="":
            messagebox.showerror("Error", "Task cannot be empty")
        else :
            self.task_listbox.insert(tk.END,task)
            self.task_entry.delete(0,tk.END)


    def delete_task(self):
        try:
            selected_index =self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        
        except IndexError:
            messagebox.showerror("Error","No item selected")

if  __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()




