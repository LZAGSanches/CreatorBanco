import psycopg2
import pandas as pds
from sqlalchemy import create_engine
import os
import sys
import re
# CONEXÃO BANCO LOCALHOST POSTGRES
alchemyEngine   = create_engine('sqlite:///C:\\Users\\andre\\AppData\\Local\\Poup\\bdpoup.db', pool_recycle=3600);
# CONEXÃO BANCO SQLITE
alchemyEngine2 = create_engine('postgresql+psycopg2://postgres:poupaqui@SRV_FTP/postgres', pool_recycle=3600);
# EXECUTA A CONEXÃO
dbConnection = alchemyEngine.connect();
dbConnection2 = alchemyEngine2.connect();
# CRIA UM DATAFRAME DO SELECT
dataFrame=pds.read_sql('select * from LOJA', dbConnection);
pds.set_option('display.expand_frame_repr', False);

conn = dbConnection2.connect();
#INSERT NO OUTRO BANCO
dataFrame.to_sql('loja', con=conn, if_exists='replace', index=False);
#FECHA AS CONEXÕES
dbConnection.close();
dbConnection2.close();
conn.close();