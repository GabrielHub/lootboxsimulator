import box
import tkinter as tk


def OpenCrystal():
    cav = box.CavCrystal()
    champ = cav.spin(pool.droptable)

    p_id = pool.mcocgetpotrait(champ[0])
    window.photo = tk.PhotoImage(file="assets/data/images/portraits/" + p_id + ".png")
    pic.configure(image=window.photo)
    pic["image"] = window.photo

    title["text"] = champ
    window.update_idletasks()


# open tkinter window
window = tk.Tk()

# must init the total pool of items that can be pulled
pool = box.Pool(0)


cav_button = tk.Button(text="Cavalier Crystal", fg="white", bg="#a442f5", command=OpenCrystal)
cav_button.pack(fill=tk.BOTH, side=tk.LEFT)

window.photo = tk.PhotoImage(file="assets/data/images/portraits/aegon.png")
pic = tk.Label(image=window.photo)
pic.pack(fill=tk.BOTH)
title = tk.Label(text="Champ Name, Rarity")
title.pack(fill=tk.BOTH)

window.mainloop()
"""
print("MCOC Crystal Examples: ")

pool = box.Pool(0)

gmc = box.GMC()
print(gmc.name, " result: ", gmc.spin(pool.droptable))

cav = box.CavCrystal()
print(cav.name, " result: ", cav.spin(pool.droptable))

basic4 = box.Box("4* Basic", {"4star": 1})
print(basic4.name, " result: ", basic4.spin(pool.droptable))

basic5 = box.Box("5* Basic", {"5basic": 1})
print(basic5.name, " result: ", basic5.spin(pool.droptable))

feat5 = box.Box("5* Featured", {"5feature": 1})
print(feat5.name, " result: ", feat5.spin(pool.droptable))

basic6 = box.Box("6* Basic", {"6basic": 1})
print(basic6.name, " result: ", basic6.spin(pool.droptable))

feat6 = box.Box("6* Featured", {"6feature": 1})
print(feat6.name, " result: ", feat6.spin(pool.droptable))
"""
