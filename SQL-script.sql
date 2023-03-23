#Brukerhistorier som trenger SQL-script:
#Databasen skal kunne registrere data om alle jernbanestrekninger i Norge. Dere skal legge inn data for Nordlandsbanen (som vist i figuren). Dette kan gjøres med et skript, dere trenger ikke å programmere støtte for denne funksjonaliteten.
#Dere skal kunne registrere data om togruter. Dere skal legge inn data for de tre togrutene på Nordlandsbanen som er beskrevet i vedlegget til denne oppgave. Dette kan gjøres med et skript, dere trenger ikke å programmere støtte for denne funksjonaliteten.
#Det skal legges inn nødvendige data slik at systemet kan håndtere billettkjøp for de tre togrutene på Nordlandsbanen, mandag 3. april og tirsdag 4. april i år. Dette kan gjøres med et skript, dere trenger ikke å programmere støtte for denne funksjonaliteten.


#Følgende data om jernbanestrekninger ble lagt til i databasen:
.open togdatabase
INSERT INTO Delstrekning VALUES ("TRD-STK", "01:52:00", 120, "dobbeltspor", "Trondheim", "Steinkjer");
INSERT INTO Delstrekning VALUES ("STK-MSJ", "03:29:00", 280, "enkeltspor", "Steinkjer", "Mosjøen");
INSERT INTO Delstrekning VALUES ("MSJ-MIR", "01:11:00", 90, "enkeltspor", "Mosjøen", "Mo I Rana");
INSERT INTO Delstrekning VALUES ("MIR-FSK", "02:18:00", 170, "enkeltspor", "Mo I Rana", "Fauske");
INSERT INTO Delstrekning VALUES ("FSK-BOD", "00:45:00", 60, "enkeltspor", "Fauske", "Bodø");
INSERT INTO Delstrekning VALUES ("STK-TRD", "01:52:00", 120, "dobbeltspor", "Steinkjer","Trondheim");
INSERT INTO Delstrekning VALUES ("MSJ-STK", "03:29:00", 280, "enkeltspor", "Mosjøen","Steinkjer");
INSERT INTO Delstrekning VALUES ("MIR-MSJ", "01:11:00", 90, "enkeltspor", "Mo I Rana","Mosjøen");
INSERT INTO Delstrekning VALUES ("FSK-MIR", "02:18:00", 170, "enkeltspor", "Fauske","Mo I Rana");
INSERT INTO Delstrekning VALUES ("BOD-FSK", "00:45:00", 60, "enkeltspor", "Bodø","Fauske");
INSERT INTO Stasjon VALUES ("Trondheim", 5);
INSERT INTO Stasjon VALUES ("Steinkjer", 4);
INSERT INTO Stasjon VALUES ("Mosjøen", 7);
INSERT INTO Stasjon VALUES ("Mo i Rana", 4);
INSERT INTO Stasjon VALUES ("Fauske", 34);
INSERT INTO Stasjon VALUES ("Bodø", 4);
INSERT INTO Togrute VALUES ("TRD-BOD-dag-man", "Dagtog Trondheim-Bodø", "07:49:00", "Mandag", "Trondheim", "Bodø", "SJ", "Nordlandsbanen");
INSERT INTO Togrute VALUES ("TRD-BOD-natt-man", "Nattog Trondheim-Bodø", "23:05:00", "Mandag", "Trondheim", "Bodø", "SJ", "Nordlandsbanen");
INSERT INTO Togruteforekomst VALUES ("TRD-BOD-dag-man", "03.04.2023");
INSERT INTO Togruteforekomst VALUES ("TRD-BOD-natt-man", "03.04.2023");
INSERT INTO Togoperatør VALUES ("SJ", 20, 12);
INSERT INTO Sete VALUES (1,1);
INSERT INTO Sete VALUES (2,1);
INSERT INTO Sete VALUES (3,1);
INSERT INTO Sete VALUES (4,1);
INSERT INTO Sete VALUES (5,1);
INSERT INTO Sete VALUES (6,1);
INSERT INTO Sete VALUES (7,1);
INSERT INTO Sete VALUES (8,1);
INSERT INTO Sete VALUES (9,1);
INSERT INTO Sete VALUES (10,1);
INSERT INTO Sete VALUES (11,1);
INSERT INTO Sete VALUES (12,1);
INSERT INTO Seng VALUES (1,1);
INSERT INTO Seng VALUES (2,1);
INSERT INTO Seng VALUES (3,1);
INSERT INTO Seng VALUES (4,1);
INSERT INTO Seng VALUES (5,1);
INSERT INTO Seng VALUES (6,1);
INSERT INTO Seng VALUES (7,1);
INSERT INTO Seng VALUES (8,1);
INSERT INTO Sovevogn VALUES (1,4,8);
INSERT INTO Sittevogn VALUES (1,6,12);
INSERT INTO DelAvStrekning VALUES ("Nordlandsbanen", "TRD-STK");
INSERT INTO DelAvStrekning VALUES ("Nordlandsbanen", "STK-MSJ");
INSERT INTO DelAvStrekning VALUES ("Nordlandsbanen", "MSJ-MIR");
INSERT INTO DelAvStrekning VALUES ("Nordlandsbanen", "MIR-FSK");
INSERT INTO DelAvStrekning VALUES ("Nordlandsbanen", "FSK-BOD");
INSERT INTO Togrute VALUES ("MIR-TRD-mor-man", "Morgentog Mo i Rana - Trondheim", "08:11:00", "Mandag", "Mo i Rana", "Trondheim", "SJ", "Nordlandsbanen"); 
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-man", "TRD-STK");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-man", "STK-MSJ");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-man", "MSJ-MIR");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-man", "MIR-FSK");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-man", "FSK-BOD");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-man", "FSK-BOD");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-man", "MIR-FSK");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-man", "MSJ-MIR");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-man", "STK-MSJ");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-man", "TRD-STK");
INSERT INTO StrekningIRute VALUES ("MIR-TRD-mor-man", "STK-TRD");
INSERT INTO StrekningIRute VALUES ("MIR-TRD-mor-man", "MSJ-STK");
INSERT INTO StrekningIRute VALUES ("MIR-TRD-mor-man", "MIR-MSJ");
INSERT INTO Togruteforekomst VALUES ("MIR-TRD-mor-man", "03.04.2023");
INSERT INTO Togrute VALUES ("MIR-TRD-mor-tir", "Morgentog Mo i Rana - Trondheim", "08:11:00", "Tirsdag", "Mo i Rana", "Trondheim", "SJ", "Nordlandsbanen");
INSERT INTO Togrute VALUES ("TRD-BOD-dag-tir", "Dagtog Trondheim-Bodø", "07:49:00", "Tirsdag", "Trondheim", "Bodø", "SJ", "Nordlandsbanen");
INSERT INTO Togrute VALUES ("TRD-BOD-natt-tir", "Nattog Trondheim-Bodø", "23:05:00", "Tirsdag", "Trondheim", "Bodø", "SJ", "Nordlandsbanen");
INSERT INTO Togruteforekomst VALUES ("MIR-TRD-mor-tir", "04.04.2023");
INSERT INTO Togruteforekomst VALUES ("TRD-BOD-dag-tir", "04.04.2023");
INSERT INTO Togruteforekomst VALUES ("TRD-BOD-natt-tir", "04.04.2023");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-tir", "TRD-STK");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-tir", "STK-MSJ");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-tir", "MSJ-MIR");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-tir", "MIR-FSK");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-dag-tir", "FSK-BOD");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-tir", "FSK-BOD");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-tir", "MIR-FSK");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-tir", "MSJ-MIR");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-tir", "STK-MSJ");
INSERT INTO StrekningIRute VALUES ("TRD-BOD-natt-tir", "TRD-STK");
INSERT INTO StrekningIRute VALUES ("MIR-TRD-mor-tir", "STK-TRD");
INSERT INTO StrekningIRute VALUES ("MIR-TRD-mor-tir", "MSJ-STK");
INSERT INTO StrekningIRute VALUES ("MIR-TRD-mor-tir", "MIR-MSJ");
CREATE TABLE StasjonPåRute (
  TogruteID VARCHAR(30) NOT NULL,
  Stasjonsnavn VARCHAR(30) NOT NULL,
  Avgangstid TIME,
  Ankomsttid TIME,
  CONSTRAINT StasjonPåRute_PK PRIMARY KEY (TogruteID, Stasjonsnavn),
  CONSTRAINT StasjonPåRute_FK1 FOREIGN KEY (TogruteID) REFERENCES Togrute(TogruteID) ON UPDATE CASCADE,
  CONSTRAINT StasjonPåRute_FK2 FOREIGN KEY (Stasjonsnavn) REFERENCES Stasjon(Navn) ON UPDATE CASCADE
);
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-man', 'Trondheim', "07:47", "07:49");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-man', 'Steinkjer', "09:49", "09:51");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-man', 'Mosjøen', "13:18", "13:20");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-man','Mo i Rana', "14:29", "14:31");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-man', 'Fauske', "16:47", "16:49");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-man', 'Bodø', "17:34", NULL);
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-tir', 'Trondheim', "07:47", "07:49");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-tir', 'Steinkjer', "09:49", "09:51");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-tir', 'Mosjøen', "13:18", "13:20");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-tir','Mo i Rana', "14:29", "14:31");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-tir', 'Fauske', "16:47", "16:49");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-dag-tir', 'Bodø', "17:34", NULL);
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-man', 'Trondheim', "23:03", "23:05");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-man', 'Steinkjer', "00:55", "00:57");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-man', 'Mosjøen', "04:39", "04:41");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-man','Mo i Rana', "05:53", "05:55");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-man', 'Fauske', "08:17", "08:19");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-man', 'Bodø',"09:05", NULL);
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-tir', 'Trondheim', "23:03", "23:05");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-tir', 'Steinkjer', "00:55", "00:57");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-tir', 'Mosjøen', "04:39", "04:41");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-tir','Mo i Rana', "05:53", "05:55");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-tir', 'Fauske', "08:17", "08:19");
INSERT INTO StasjonPåRute VALUES ('TRD-BOD-natt-tir', 'Bodø',"09:05", NULL);
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-man', 'Mo i Rana', "08:09", "08:11");
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-man', 'Mosjøen', "09:12", "09:14");
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-man', 'Steinkjer', "12:29", "12:31");
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-man', 'Trondheim', "14:13", NULL);
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-tir', 'Mo i Rana', "08:09", "08:11");
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-tir', 'Mosjøen', "09:12", "09:14");
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-tir', 'Steinkjer', "12:29", "12:31");
INSERT INTO StasjonPåRute VALUES ('MIR-TRD-mor-tir', 'Trondheim', "14:13", NULL);
.quit



