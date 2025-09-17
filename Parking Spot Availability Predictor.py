import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LogisticRegression

X=[[9,1],[10,0],[15,1],[20,0],[12,1]]
y=[1,0,1,0,1]

model=LogisticRegression()
model.fit(X,y)

def predict_parking():
    hour=int(hour_entry.get())
    day=int(day_entry.get())
    prediction=model.predict([[hour,day]])[0]
    status="Free" if prediction==1 else "Occupied"
    messagebox.showinfo("Prediction",f"Parking spot will be: {status}")

root=tk.Tk()
root.title("Parking Spot Availability Predictor")
tk.Label(root,text="Hour of Day (0-23):").pack()
hour_entry=tk.Entry(root); hour_entry.pack()
tk.Label(root,text="Day Type (1-Weekday,0-Weekend):").pack()
day_entry=tk.Entry(root); day_entry.pack()
tk.Button(root,text="Predict",command=predict_parking).pack()
root.mainloop()
