import pyodbc
import time

def getDDx():

    # Supply and ip address or hostname of databases required to be extracted
    connection_list = ['<>']

    # Run through the connections with the appropriate credentials. SysProp recommended for security
    for connection in connection_list:
        connection_str = '<>'

        # Password may be offputting to the connection; be sure to end in ';'
        cnxn = pyodbc.connect(connection_str+';')
        cursor = cnxn.cursor()

        # Create a list or import a list of tables--recommended to come direct from
        # information schemas with the current cursor
        with open("<>.csv",'r') as PO_List:
            for i in PO_List.readlines():
                inTable = i.split(",")[0].replace("\n","")
                stmt = 'sp_helptext @objname=\''+inTable+'\''
                print(inTable)

                # Fetch and write the entire response of the stored procedure to
                # a file
                try:
                    with open("<>"+inTable+".sql",'a') as current_file:
                        cursor.execute(stmt)
                        for x in cursor.fetchall():
                            current_file.write(x[0])
                    print(inTable + " is complete.")
                except:
                    print(inTable + ' failed in error.')

if __name__ == "__main__":
    getDDx()
        
