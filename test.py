import box
import tkinter as tk
import random
"""
def OpenCrystal():
    cav = box.CavCrystal("Cavalier Crystal", pool)
    champ = cav.spin()
    print(champ[0].pic_id)
    window.photo = tk.PhotoImage(file="assets/data/images/portraits/" + champ[0].pic_id + ".png")
    pic.configure(image=window.photo)
    pic["image"] = window.photo

    n_text = champ[0].name, champ[1]
    title["text"] = n_text
    window.update_idletasks()


# open tkinter window
window = tk.Tk()

# must init the total pool of items that can be pulled
pool = box.mcoclootpool()

cav_photo = tk.PhotoImage(file="assets/data/images/crystals/crystal_multi_dim_purple.png")
cav_button = tk.Button(image=cav_photo, command=OpenCrystal)
cav_button.pack(fill=tk.BOTH)

window.photo = tk.PhotoImage(file="assets/data/images/portraits/aegon.png")
pic = tk.Label(image=window.photo)
pic.pack(fill=tk.BOTH)
title = tk.Label(text="Champ Name, Rarity")
title.pack(fill=tk.BOTH)

window.mainloop()
"""

pool = box.Pool(0)
cav = box.CavCrystal("Cavalier Crystal")
print(cav.spin(pool.droptable))
