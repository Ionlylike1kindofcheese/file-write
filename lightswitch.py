import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
lightstatus = "off"
window.config(bg="black")
button.config(text="Switch light on")

def showMsg():
    global lightstatus
    if lightstatus == "off":
        button.config(text="Switch light " + lightstatus)
        lightstatus = "on"
        window.config(bg="yellow")
    elif lightstatus == "on":
        button.config(text="Switch light " + lightstatus)
        lightstatus = "off"
        window.config(bg="black")
    logfile = open('actions.log', 'a')
    writevar = ("Light is " + lightstatus)
    logfile.write(writevar)
    logfile.write('\n')
    logfile.close()
        
button.config(command=showMsg)
    
# schijf hier tussen je code

window.mainloop()