import sqlite3




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
    cursor.execute(f"SELECT DISTINCT Togrute.Rutenavn FROM Togrute INNER JOIN Delstrekning WHERE Avgangsdag='{dg}' AND (Delstrekning.Startstasjon='{st}' OR Delstrekning.Endestasjon='{st}')")
    rows=cursor.fetchall()
    con.close()
    print("Følgende togruter ble funnet:")
    print(rows)


def togrute_to_stasjoner():
    st1=input("Skriv inn ønsket startstasjon: ")
    st2=input("Skriv inn ønsket endestasjon: ")
    con = sqlite3.connect("../togdatabase.db")
    cursor=con.cursor()
    cursor.execute(f"SELECT * FROM Togrute INNER JOIN Delstrekning WHERE (Delstrekning.startstasjon='{st1}' AND Delstrekning.endestasjon='{st2}') OR (Delstrekning.startstasjon='{st2}' AND Delstrekning.endestasjon='{st1}')")
    rows=cursor.fetchall()
    con.close()
    print("Følgende togruter ble funnet:")
    print(rows)


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
            

        
    #Spørre om kunden vil logge inn eller registrere seg
    #Mulighet for å kjøpe billett
    #Mulighet for å se eksisterende kjøp


#Kjører funksjonaliteten:
interface()