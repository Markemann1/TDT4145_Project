import sqlite3
from datetime import datetime
from datetime import timedelta



#Funksjonalitet som skal programmeres:
#*   For en stasjon som oppgis, skal bruker få ut alle togruter som er innom stasjonen en gitt ukedag. Denne funksjonaliteten skal programmeres.
#*   Bruker skal kunne søke etter togruter som går mellom en startstasjon og en sluttstasjon, med utgangspunkt i en dato og et klokkeslett. Alle ruter den samme dagen og den neste skal returneres, sortert på tid. Denne funksjonaliteten skal programmeres.
#*   En bruker skal kunne registrere seg i kunderegisteret. Denne funksjonaliteten skal programmeres.
#*   Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute og kjøpe de billettene hen ønsker. Denne funksjonaliteten skal programmeres. Pass på at dere bare selger ledige plasser
# *   For en bruker skal man kunne finne all informasjon om de kjøpene hen har gjort for fremtidige reiser. Denne funksjonaliteten skal programmeres.

#Eksempel på kode for å utføre en spørring til en SQL-database:
#con = sqlite3.connect("prosjekt_P1.sql")
#cursor=con.cursor()
#cursor.execute("SELECT * FROM Togrute")
#con.close()



def interface():
    print("Hei! Velkommen til togdatabasen! Hva ønsker du å gjøre?\n"+
        "1. Se togruter for en gitt dag og stasjon \n"+
        "2. Søke etter togruter mellom to stasjoner \n"+
        "3. Logge inn i kunderegisteret")
    valg=input("Skriv inn et tall fra 1-3: ")
    if valg=="1":
        togrute_dag_stasjon() 
    elif valg=="2":
        togrute_to_stasjoner()
    elif valg=="3":
        kunderegister()


def togrute_dag_stasjon():
    st=input("Skriv inn ønsket stasjon: ")
    dg=input("Skriv inn ønsket ukedag: ")
    con = sqlite3.connect("../togdatabase.db")
    cursor=con.cursor()
    cursor.execute(f"SELECT DISTINCT Togrute.TogruteID, Togrute.Rutenavn FROM (Togrute INNER JOIN StrekningIRute ON (Togrute.TogruteID=StrekningIRute.Rutenavn)) INNER JOIN Delstrekning ON (StrekningIRute.StrekningsID=Delstrekning.StrekningsID) WHERE Avgangsdag='{dg}' AND (Delstrekning.Startstasjon='{st}' OR Delstrekning.Endestasjon='{st}')")
    rows=cursor.fetchall()
    con.close()
    print("Følgende togruter ble funnet:")
    for i in rows:
        print("TogruteID: ",i[0],'\n',"Togrutenavn: ",i[1])


def togrute_to_stasjoner():
    st1=input("Skriv inn ønsket startstasjon: ")
    st2=input("Skriv inn ønsket endestasjon: ")
    st3=input("Dato (DD.MM.YYYY): ")
    st4=input("Klokkeslett: ")
    st5=(datetime.strptime(st3, '%d.%m.%Y') + timedelta(days=1))
 #   print(st5)
    str5=st5.strftime('%d.%m.%Y')
#    print(str5)
    con = sqlite3.connect("../togdatabase.db")
    cursor=con.cursor()
    cursor.execute(f"SELECT DISTINCT Togrute.TogruteID, Togrute.Rutenavn, Togruteforekomst.Dato, StasjonPåRute.Ankomsttid FROM (((Togrute INNER JOIN StrekningIRute ON (Togrute.TogruteID=StrekningIRute.Rutenavn)) INNER JOIN Delstrekning ON (StrekningIRute.StrekningsID=Delstrekning.StrekningsID)) INNER JOIN Togruteforekomst on (Togrute.TogruteID=Togruteforekomst.TogruteID)) INNER JOIN StasjonPåRute ON (Togrute.TogruteID=StasjonPåRute.TogruteID) WHERE Delstrekning.startstasjon='{st1}' AND Delstrekning.endestasjon='{st2}' AND StasjonPåRute.Stasjonsnavn='{st1}' AND ((Togruteforekomst.Dato='{st3}'AND StasjonPåRute.Avgangstid BETWEEN '{st4}' AND '23:59') OR Togruteforekomst.Dato='{str5}') ORDER BY Togruteforekomst.Dato, StasjonPåRute.Avgangstid")
    rows=cursor.fetchall()
    con.close()
    print("Følgende togruter ble funnet:")
    for i in rows:
        temp=datetime.strptime(str(i[3]), '%H:%M') + timedelta(minutes=2)
        avg=temp.strftime('%H:%M')
        print("TogruteID: ",i[0],'\n',"Togrutenavn: ",i[1],'\n', "Dato toget kjører fra første stasjon: ",i[2],'\n', f"Avgangstid fra {st1}: ",avg)


def kunderegister():
    ch1=input("Vil du logge inn (1) eller registrere deg (2)? ")
    if ch1=='2':
        nv=input("Hva er navnet ditt? ")
        ep=input("Hva er e-posten din? ")
        tlf=input("Hva er telefonnummeret ditt? ")
        con = sqlite3.connect("../togdatabase.db")  
        cursor=con.cursor()
        cursor.execute("SELECT Kunde.Kundenummer FROM Kunde")
        rows=cursor.fetchall()
        if len(rows)==0:
            knr=1
        else:
            knr=len(rows)+1
        print(f"Kundenummeret ditt er {knr}. Bruk det for å logge inn senere.")
        cursor.execute(f"INSERT INTO Kunde VALUES ({knr},'{nv}','{ep}',{tlf})")
        con.commit()
        con.close()
    elif ch1=='1':
        nv=input("Hva er kundenummeret ditt? ")
        ch2=input("Velkommen tilbake! Hva ønsker du å gjøre?\n"
        "1. Kjøpe togbilletter\n"
        "2. Se tidligere kjøp\n")
        if ch1=='1':
            togr=input("Hva er togrute-ID-en til togruten du vil reise med?\n"
            "Hvis du er usikker, skriv '1', så blir du sendt til søkefunksjonaliteten: ")
            if togr=="1":
                togrute_to_stasjoner()
            st1=input("Hvor skal du reise fra? ")
            st2=input("Hvor skal du reise til? ")
            ant=input("Hvor mange billetter ønsker du? ")


        
#    st3=input("Dato: ")
#    st4=input("Klokkeslett: ")
#    con = sqlite3.connect("../togdatabase.db")
#    cursor=con.cursor()
#    cursor.execute(f"SELECT Togrute.Rutenavn, Avgangsdag, Avgangstid FROM Togrute INNER JOIN Delstrekning WHERE Delstrekning.startstasjon='{st1}' AND Delstrekning.endestasjon='{st2}' AND (Avngangsdag BETWEEN '{st3}' AND '{st3}'+'1 day') AND (Avgangstid BETWEEN '{st4}' AND '23:59')")
#    rows=cursor.fetchall()
#    con.close()
#    print("Følgende togruter ble funnet:")
#    print(rows)
#    return rows


#def kunderegister():
    #Spørre om kunden vil logge inn eller registrere seg
    #Mulighet for å kjøpe billett
    #Mulighet for å se eksisterende kjøp

def search_and_buy():
    """
    Registrerte kunder skal:
    Finne ledige billetter for en valgt togrute
    Og kjøpe hvilke billetter de vil
    - også lagre det til deres kundenummer
    """
    togruter = togrute_to_stasjoner()
    for row in togruter:
        print(row)

    # Prompt the user to select a row
    selected_row = int(input("Enter the row number you want to select: "))

    # Retrieve the selected row from the list
    if selected_row > 0 and selected_row <= len(togruter):
        reise = togruter[selected_row - 1]
        print("Selected trainride:", reise)
    else:
        print("Invalid selection")


    """Ta valget togruter[Reise-1], og finn frem ledige seter fra databasen"""
    con = sqlite3.connect("../togdatabase.db")
    cursor=con.cursor()
    cursor.execute(f"SELECT Togrute.Rutenavn FROM Togrute WHERE Togrute.Rutenavn='{togruter[reise-1]}'")


def myTickets():
    """
    En registrert kunde burde kunne skrive inn (kundenummeret?) sitt, og få alle fremtidige billetter linket til den brukeren
    """


#Kjører funksjonaliteten:
interface()
