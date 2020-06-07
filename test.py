import box
import tkinter as tk


def OpenCrystal(crystal, pic, text):
    champ = crystal.spin(pool.droptable)

    # process of converting champ name to picture id -> picture file name
    p_id = pool.mcocgetpotrait(champ[0])
    window.photo = tk.PhotoImage(
        file="assets/data/images/portraits/" + p_id + ".png")
    pic.configure(image=window.photo)
    pic["image"] = window.photo

    text["text"] = champ
    window.update_idletasks()


def OpenCav():
    OpenCrystal(box.CavCrystal(), cav_pic, cav_title)


# open tkinter window
window = tk.Tk()

# must init the total pool of items that can be pulled
pool = box.Pool(0)

# Cav Crystal Example
window.photo = tk.PhotoImage(file="assets/data/images/crystals/crystal_multi_alliance.png")
cav_pic = tk.Label(image=window.photo)

cav_title = tk.Label(text="Champ Name, Rarity")

cav_button = tk.Button(text="Cavalier Crystal", fg="white", bg="#a442f5", command=OpenCav)
cav_button.pack(fill=tk.BOTH, side=tk.LEFT)

cav_pic.pack(fill=tk.BOTH)
cav_title.pack(fill=tk.BOTH)

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
