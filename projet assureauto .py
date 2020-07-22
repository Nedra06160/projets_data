# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import sqlalchemy
from sqlalchemy import create_engine
#engine = create_engine('mysql+pymysql://nedra:nedra123!@localhost:3306/SIMPLON')
engine= create_engine('mysql+pymysql://nedra:nedra123!@localhost:3306/Assuranceauto')
import pandas as pd
#engine = create_engine('mysql+pymysql://nedra:nedra123!@localhost:3306/SIMPLON')
#data=pd.read_sql_query('select * from jeux_video', engine)
#print(data)

#data=pd.read_sql_query('select * from  CLIENTS', engine)
#print(data) 
CL_ID=pd.read_sql_query("select max(CL_ID) as max from CLIENTS",engine)
CL_ID=CL_ID.iloc[0,0]+1
 
CL_NOM=str.upper(input("veuillez saisir un nom : "))
print(CL_NOM)
CL_PRENOM = input("veuillez saisir un prenom : ")

CL_ADDRESSE= input("veuillez saisir une adresse : ")

CL_VILLE=input("veuillez saisir une ville : ")

CL_COORDONNEES = input("veillez saisir un numéro de tel")

engine.execute('INSERT INTO CLIENTS (CL_ID, CL_NOM, CL_PRENOM, CL_ADDRESSE, CL_VILLE, CL_COORDONNEES )VALUES (%s,"%s","%s","%s","%s","%s");' %(CL_ID, CL_NOM, CL_PRENOM, CL_ADDRESSE, CL_VILLE, CL_COORDONNEES ))
CO_ID=pd.read_sql_query("select max(CO_ID) as max from CONTRAT",engine)

CO_ID=CO_ID.iloc[0,0]+1

CO_CATEGORIES='Tiers'
CO_BONUS=''
CO_MALUS=''
CO_CLIENTS_FK=1
CO_ID = pd.read_sql_query("SELECT max(CO_ID) as max2 FROM CONTRAT;", engine)['max2'].values
CO_ID = CO_ID[0]+1
CO_BONUS = ''
CO_MALUS = ''
CO_CATEGORIE = 'Tiers'
CO_AGENCE_FK = 1

while len(CO_BONUS) == 0 or len(CO_MALUS) == 0 :


    if len(CO_BONUS) == 0:
        CO_BONUS = input('veuillez entrer un BONUS :')

    elif len(CO_MALUS) == 0:
       CO_MALUS = input('veuillez entrer un MALUS :')

   


engine.execute('INSERT INTO CONTRAT (CO_ID, CO_DATE, CO_BONUS, CO_MALUS, CO_CATEGORIE, CO_CLIENTS_FK,)'
               'VALUES(%s,"%s","%s","%s","%s",%s);'%(CO_ID,,CO_BONUS,CO_MALUS,CO_CATEGORIE, CO_CLIENTS_FK,))
