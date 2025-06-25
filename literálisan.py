from playsound import playsound
be = True
while be == True:
    valasz = int(input("""
    Írd be az általad kiválasztott kinyilatkoztatás számát:
    0: kilépés, a program leáll
    1: literálisan testvéremsz
    2: csao papikám
    3: 1.5 hónapja tettem le a kólát
    4: 7-24 az utcán voltam
    5: amúgy... ja
    6: annyit drogoztunk...
    7: baszni is szeretek amúgy
    8: bazdmeeg
    9: bulizok, meg baszok
    10: kéttannyelvű C1-es angol nyelvvizsga
    11: *catchy beatbox*
    12: bennem van ez a csibész vér
    13: drogdílerkedés miatt hagytad ott az egyetemet
    14: literálisan hangyafasznyi fájdalom
    15: fenegyerek vagyok
    16: frontin, xanax, spuri, eki
    17: hú, cigány...
    18: literálisan hugy, szar
    19: hülyék vagyunk
    20: KDT jelentése
    21: *nagyon összeszedett gondolatmenet*
    22: mindenki kis pancser
    23: nem... igen... igen
    24: paprikasprézgetnek a kislányok
    25: rocksztárok vagyunk
    26: rocksztár vagyok
    27: meg kell baszni a színpadot
    28: szüleiddel élsz?
    29: föl van szopva a faszom tövig
    30: uuuuuu
    31: bónusz
    """))
    if valasz == 1:
        playsound(r"testveremsz.mp3")
    elif valasz == 2:
        playsound(r'csao papikam.mp3')
    elif valasz == 3:
        playsound(r'1.5 honap.mp3')
    elif valasz == 4:
        playsound(r'7_24.mp3')
    elif valasz == 5:
        playsound(r'amugy... ja.mp3')
    elif valasz == 6:
        playsound(r'annyit drogoztunk.mp3')
    elif valasz == 7:
        playsound(r'baszni is szeretek.mp3')
    elif valasz == 8:
        playsound(r'bazdmeeg.mp3')
    elif valasz == 9:
        playsound(r'bulizok baszok.mp3')
    elif valasz == 10:
        playsound(r'C1.mp3')
    elif valasz == 11:
        playsound(r'catchy.mp3')
    elif valasz == 12:
        playsound(r'csibesz ver.mp3')
    if valasz == 13:
        playsound(r"drog driller.mp3")
    elif valasz == 14:
        playsound(r'fajdalom.mp3')
    elif valasz == 15:
        playsound(r'fenegyerek.mp3')
    elif valasz == 16:
        playsound(r'frontin....mp3')
    elif valasz == 17:
        playsound(r'hu cigany.mp3')
    elif valasz == 18:
        playsound(r'hugy szar.mp3')
    elif valasz == 19:
        playsound(r'hulyek vagyunk.mp3')
    elif valasz == 20:
        playsound(r'KDT.mp3')
    elif valasz == 21:
        playsound(r'literalisan csokynak pl a csaki.mp3')
    elif valasz == 22:
        playsound(r'mindenki kis pancser.mp3')
    elif valasz == 23:
        playsound(r'nem... igen.mp3')
    elif valasz == 24:
        playsound(r'paprikaspre.mp3')
    elif valasz == 25:
        playsound(r'roxtar.mp3')
    elif valasz == 26:
        playsound(r'roxtar2.mp3')
    elif valasz == 27:
        playsound(r'szinpad baszas.mp3')
    elif valasz == 28:
        playsound(r'szuleiddel elsz.mp3')
    elif valasz == 29:
        playsound(r'tovig.mp3')
    elif valasz == 30:
        playsound(r'uuuuuu.mp3')
    elif valasz == 31:
        playsound(r'roxtar.mp3')
        playsound(r'szuleiddel elsz.mp3')
    elif valasz == 0:
        be = False
        playsound(r'kilepo.mp3')
        print('A program leáll')
    else: print('kurva anyád')



