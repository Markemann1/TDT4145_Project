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
 #   elif valg=="3":
 #       kunderegister()


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
    st3=input("Dato: ")
    st4=input("Klokkeslett: ")
    con = sqlite3.connect("../togdatabase.db")
    cursor=con.cursor()
    cursor.execute(f"SELECT Togrute.Rutenavn, Avgangsdag, Avgangstid FROM Togrute INNER JOIN Delstrekning WHERE Delstrekning.startstasjon='{st1}' AND Delstrekning.endestasjon='{st2}' AND (Avngangsdag BETWEEN '{st3}' AND '{st3}'+'1 day') AND (Avgangstid BETWEEN '{st4}' AND '23:59')")
    rows=cursor.fetchall()
    con.close()
    print("Følgende togruter ble funnet:")
    print(rows)
    return rows


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
