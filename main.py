from Krokev import *
from tkinter import *

def counts():
    sirka_budovy = float(sirka_budovy_entry.get())
    stoupani = stoupani_entry.get()
    tloustka_hrebenoveho_tramu = float(tloustka_hrebenoveho_tramu_entry.get())
    vyska_hrebenoveho_tramu = float(vyska_hrebenoveho_tramu_entry.get())
    sirka_krokve = float(sirka_krokve_entry.get())
    delka_sedla_krokve = float(delka_sedla_krokve_entry.get())
    delka_presahu = float(delka_presahu_entry.get())

    k = Krokev(sirka_budovy,stoupani,tloustka_hrebenoveho_tramu,vyska_hrebenoveho_tramu,sirka_krokve,delka_sedla_krokve,delka_presahu)
    r1 = k.getRatio()[0]
    r2 = k.getRatio()[1]
    hreben = k.getRealRise()
    rafter_length = k.getRafterLength()
    rafter_overhang = k.getOverhang()
    total_rafter_length = k.getTotalRafterLength()
    board_length = k.getBoardLength()
    seat_depth = k.getSeatDepth()

    ratio_label["text"] = f"\nPoměr stoupání: {r1} : {r2}"
    hreben_label["text"] = f"Finální výška hřebene: {hreben} cm"
    rafter_length_label["text"] = f"Délka krokve bez přesahu: {rafter_length} cm"
    rafter_overhang_label["text"] = f"Délka přesahu krokve: {rafter_overhang} cm"
    total_rafter_length_label["text"] = f"Celková délka krokve s přesahem: {total_rafter_length} cm"
    seat_depth_label["text"] = f"Hloubka zářezu sedla: {seat_depth} cm"
    board_length_label["text"] = f"Potřebná délka trámu na vyřezání krokve: {board_length} cm"

def get_degrees():
    ratio_label["text"] = f"1:12 : 4.76\n2:12 : 9.46\n3:12 : 14.04\n4:12 : 18.43\n5:12 : 22.62\n6:12 : 26.57\n7:12 : 30.26\n8:12 : 33.69\n9:12 : 36.87\n10:12 : 39.81\n11:12 : 42.51\n12:12 : 45\n13:12 : 47.29\n14:12 : 49.4\n15:12 : 51.34"

win = Tk()
win.title("Rafter calculator - výpočet délky běžné krokve")
win.minsize(600,550)
win.resizable(False, False)
main_font = ("Sans Serif",11)

# definice rámů
load_frame = Frame(win)
load_frame.pack()
output_frame = Frame(win)
output_frame.pack()
button_frame = Frame(win)
button_frame.pack()

# vstupní část
sirka_budovy_title = Label(load_frame, text="Šířka budovy", width=10, font=main_font)
sirka_budovy_title.grid(row=0, column=0, padx=5, pady=5)
sirka_budovy_entry = Entry(load_frame, width=10, font=main_font)
sirka_budovy_entry.grid(row=0, column=1, padx=5, pady=5)
sirka_budovy_unit = Label(load_frame, text="m", width=1, font=main_font)
sirka_budovy_unit.grid(row=0, column=2, padx=5, pady=5)

stoupani_title = Label(load_frame, text="Stoupání (určuje sklon střechy)", width=25, font=main_font)
stoupani_title.grid(row=1, column=0, padx=5, pady=5)
stoupani_entry = Entry(load_frame, width=10, font=main_font)
stoupani_entry.grid(row=1, column=1, padx=5, pady=5)
stoupani_unit = Label(load_frame, text="palců (př. 4:12)", width=11, font=main_font)
stoupani_unit.grid(row=1, column=2, padx=5, pady=5)

tloustka_hrebenoveho_tramu_title = Label(load_frame, text="Tloušťka hřebenového trámu", width=20, font=main_font)
tloustka_hrebenoveho_tramu_title.grid(row=2, column=0, padx=5, pady=5)
tloustka_hrebenoveho_tramu_entry = Entry(load_frame, width=10, font=main_font)
tloustka_hrebenoveho_tramu_entry.grid(row=2, column=1, padx=5, pady=5)
tloustka_hrebenoveho_tramu_unit = Label(load_frame, text="cm", width=11, font=main_font)
tloustka_hrebenoveho_tramu_unit.grid(row=2, column=2, padx=5, pady=5)

vyska_hrebenoveho_tramu_title = Label(load_frame, text="Výška hřebenového trámu", width=20, font=main_font)
vyska_hrebenoveho_tramu_title.grid(row=3, column=0, padx=5, pady=5)
vyska_hrebenoveho_tramu_entry = Entry(load_frame, width=10, font=main_font)
vyska_hrebenoveho_tramu_entry.grid(row=3, column=1, padx=5, pady=5)
vyska_hrebenoveho_tramu_unit = Label(load_frame, text="cm", width=11, font=main_font)
vyska_hrebenoveho_tramu_unit.grid(row=3, column=2, padx=5, pady=5)

sirka_krokve_title = Label(load_frame, text="Šířka krokve", width=20, font=main_font)
sirka_krokve_title.grid(row=4, column=0, padx=5, pady=5)
sirka_krokve_entry = Entry(load_frame, width=10, font=main_font)
sirka_krokve_entry.grid(row=4, column=1, padx=5, pady=5)
sirka_krokve_unit = Label(load_frame, text="cm", width=11, font=main_font)
sirka_krokve_unit.grid(row=4, column=2, padx=5, pady=5)

delka_sedla_krokve_title = Label(load_frame, text="Délka sedla", width=20, font=main_font)
delka_sedla_krokve_title.grid(row=5, column=0, padx=5, pady=5)
delka_sedla_krokve_entry = Entry(load_frame, width=10, font=main_font)
delka_sedla_krokve_entry.grid(row=5, column=1, padx=5, pady=5)
delka_sedla_krokve_unit = Label(load_frame, text="cm", width=11, font=main_font)
delka_sedla_krokve_unit.grid(row=5, column=2, padx=5, pady=5)

delka_presahu_title = Label(load_frame, text="Přesah střechy", width=20, font=main_font)
delka_presahu_title.grid(row=6, column=0, padx=5, pady=5)
delka_presahu_entry = Entry(load_frame, width=10, font=main_font)
delka_presahu_entry.grid(row=6, column=1, padx=5, pady=5)
delka_presahu_unit = Label(load_frame, text="cm", width=11, font=main_font)
delka_presahu_unit.grid(row=6, column=2, padx=5, pady=5)

# button část
submit_button = Button(button_frame, text = "Vypočti", font=main_font, command=counts, bg="lightgray")
submit_button.grid(row=0, column=0, padx=5, pady=5, ipady=2, ipadx=3)
degrees_button = Button(button_frame, text = "Tabulka stoupání", font=main_font, command=get_degrees, bg="lightgray")
degrees_button.grid(row=0, column=1, padx=5, pady=5, ipady=2, ipadx=3)

# výstupní část
ratio_label = Label(output_frame, text="\n", font=main_font)
ratio_label.grid(row=0, column=0, padx=5, pady=5)
hreben_label = Label(output_frame, text="", font=main_font)
hreben_label.grid(row=1, column=0, padx=5, pady=5)
rafter_length_label = Label(output_frame, text="", font=main_font)
rafter_length_label.grid(row=2, column=0, padx=5, pady=5)
rafter_overhang_label = Label(output_frame, text="", font=main_font)
rafter_overhang_label.grid(row=3, column=0, padx=5, pady=5)
total_rafter_length_label = Label(output_frame, text="", font=main_font)
total_rafter_length_label.grid(row=4, column=0, padx=5, pady=5)
board_length_label = Label(output_frame, text="", font=main_font)
board_length_label.grid(row=5, column=0, padx=5, pady=5)
seat_depth_label = Label(output_frame, text="", font=main_font)
seat_depth_label.grid(row=6, column=0, padx=5, pady=5)

win.mainloop()