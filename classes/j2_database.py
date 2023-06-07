#!/usr/bin/env python3
# coding: utf-8

import os
import sqlite3
from sqlite3 import Error






class J2_Database:
    """ A Class for Databases """
    def __init__(self) -> None:    
        super().__init__()
        self.ClassVersion = "1.0.0.dev"
        self.database = r"projectionist.db"
        self.query1 = r"CREATE TABLE IF NOT EXISTS apps ( \
        rowid INTEGER PRIMARY KEY AUTOINCREMENT, \
        app text NOT NULL INDEX, \
        alias text NOT NULL INDEX, \
        location text NOT NULL, \
        version text NOT NULL, \
        type text NOT NULL INDEX);"
        self.query2 = r"SELECT COUNT(*) from apps"

        
    
    def getClassVersion(self) -> str:
        """ The Version String of this Class """
        return self.ClassVersion   
    
    def createDatabaseSQLite3(self) -> bool:
        result = False
        try:
            self.dbconnection = sqlite3.connect(self.database)
            result = True

        except Error as err:
            print(f'createDatabaseSQLite3 Query Failed: Error: {str(err)}')
            result = False

        except Exception as err:
            print(f'createDatabaseSQLite3 Query Failed: Exception: {str(err)}')
            result = False

        finally:
            print(f"createDatabaseSQLite3 =  {self.dbconnection}")
            self.dbconnection.close()
#           time.sleep(1)
            return result
    
    def dropDatabaseSQLite3(self) -> bool:
        result = False
        try: 
            if os.path.exists(self.database):
                os.remove(self.database)
                result = True

        except Error as err:
            print(f'dropDatabaseSQLite3 Query Failed: Error: {str(err)}')
            result = False

        except Exception as err:
            print(f'dropDatabaseSQLite3 Query Failed: Exception: {str(err)}')
            result = False

        finally:
            print(f"dropDatabaseSQLite3 =  {result}")
 #           time.sleep(1)
            return result    
        
    def createTableSQLite3(self) -> bool:  # sourcery skip: class-extract-method
        result = False
        try:
            self.dbconnection = sqlite3.connect(self.database)
            self.cursor = self.dbconnection.cursor()
            self.cursor.execute(self.query1)
            self.dbconnection.commit()
            result = True
            print(f'{self.query1}')

        except Error as err:
            print(f'createTableSQLite3 Query Failed: Error: {str(err)}')
            result = False

        except Exception as err:
            print(f'createTableSQLite3 Query Failed: Exception: {str(err)}')
            result = False

        finally:
            print(f"createTableSQLite3 = {result}")            
            self.dbconnection.close()
#            time.sleep(1)
            return result      
        
        
    def countRowsSQLIte3(self) -> int:
        result = 0
        try:
            self.dbconnection = sqlite3.connect(self.database)
            self.cursor = self.dbconnection.cursor()
            self.cursor.execute(self.query2)
            
            result = self.cursor.fetchone()
            result = result[0]
            
        except Error as err:
            print(f'countRowsSQLIte3 Query Failed: Error: {str(err)}')
            result = False

        except Exception as err:
            print(f'countRowsSQLIte3 Query Failed: Exception: {str(err)}')
            result = False

        finally:
            print(f"countRowsSQLIte3 = {result}")            
            self.dbconnection.close()
#            time.sleep(1)
            return result  
        
    def upsertRowSQLite3(self, values) -> bool: # type: ignore
        result = False    
        try:
            self.upsertquery = r"INSERT INTO apps \
                (app, alias, location, version, type) \
                VALUES(values[0], values[1], values[2], values[3], values[4]) \
                ON CONFLICT (app) DO UPDATE SET \
                    alias=excluded.alias, \
                    location=excluded.location, \
                    version=excluded.version, \
                    type=excluded.type \
                    WHERE 1;"
            self.dbconnection = sqlite3.connect(self.database)
            self.cursor = self.dbconnection.cursor() 
            self.cursor.execute(self.upsertquery)           
            self.dbconnection.commit()
            result = True
            print(f'{self.upsertquery}')
        
        except Error as err:
            print(f'upsertRowSQLite3 Query Failed: Error: {str(err)}')
            result = False

        except Exception as err:
            print(f'upsertRowSQLite3 Query Failed: Exception: {str(err)}')
            result = False

        finally:
            print(f"upsertRowSQLite3 = {result}")            
            self.dbconnection.close()
#            time.sleep(1)
            return result              
            
            
        
        
        
        
        
        
        
        
        return result