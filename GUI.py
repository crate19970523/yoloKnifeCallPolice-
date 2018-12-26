def ui():
    r_image.show()#開啟圖片
    root=tk.Tk()
    root.title("可能發生搶案")
    if(path=='./imgtest/ltuschool.jpg'):
        address=tk.Label(root,text="台中市南屯區嶺東路1號",font=("Arial", 64))
        address.pack()
        root.wm_attributes('-topmost',1)
        root.mainloop()
if __name__ == "__main__":
    ui()