# Vytvor list 'tyden' a uloz dny v tydnu v podobe stringu
tyden = ["pondeli","utery","streda","ctvrtek","patek","sobota","nedele"]

# Ziskej vyber dne od uzivatele
cislo_dne = int(input("Vyber den v tydnu dle jeho cisla, kde 1 je pondeli"))
if cislo_dne < 1 or cislo_dne > 7:
    print("Vybrali jste cislo mimo rozsah")
else:
    tip_prvniho_pismena = input("jake je prvni pismeno?")
# Ziskej den z listu na zaklade hodnoty ziskane od uzivatele
vybrany_den = tyden[cislo_dne - 1]
prvni_pismeno_dne = vybrany_den[0]

if prvni_pismeno_dne == tip_prvniho_pismena:
  print("Super, správný tip prvního písmene")
else:
  print("Špatný tip prvního písmene")
print("tohle je rychlá změna kódu")