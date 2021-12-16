note=[4.5, 5.5]  #
anzahl=len(note)
summe=0
for n in note:
    summe=summe+n
print("Notendurchschnitt" + str(summe/anzahl))
