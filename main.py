from neo4j import GraphDatabase

uri = "bolt://localhost"
driver = GraphDatabase.driver(uri, auth=("neo4j", "12345"))

def menu():
    choice = '0'
    while choice == '0':
        print("Selecciona una opción")
        print("\t1) Nodos que tengan relacion de Hyperlink con la página List of Missouri highways")
        print("\t2) Nodos que pertenezcan a la categoría Mammals_of_Mexico")
        print("\t3) Paginas que su título incluya el nombre Samantha")
        print("\t4) Salir")
        choice = input("Opción: ")
        if choice=="1":
            print("Seleccionaste el query 1")
            return 1
        elif choice=="2":
            print("Seleccionaste el query 2")
            return 2
        elif choice=="3":
            print("Seleccionaste el query 3")
            return 3
        elif choice=="4":
            print("Adiós!")
            return 4
        else:
            print("Opción inválida")
            choice='0'

#Nodos que tengan relacion de Hyperlink con la página "List of Missouri highways"
#MATCH (n:Article {PageName:"List of Missouri highways"}) <-[:Hyperlink]-> (b) RETURN b.PageName, b.id, b.Category ORDER BY b.id
def queryOne(tx):
    print("Resultado del query:\n\tMATCH (n:Article {PageName:\"List of Missouri highways\"}) <-[:Hyperlink]-> (b) RETURN b.PageName, b.id, b.Category ORDER BY b.id")
    print("ID\tPageName\t\tCategory")
    for record in tx.run("MATCH (n:Article {PageName:\"List of Missouri highways\"}) <-[:Hyperlink]-> (b) RETURN b.PageName, b.id, b.Category ORDER BY b.id"):
        print(str(record["b.id"])+"\t"+record["b.PageName"]+"\t\t"+record["b.Category"])
    print("\n")
    return


#Nodos que pertenezcan a la categoría Mammals_of_Mexico
#MATCH (n:Article {Category:"Mammals_of_Mexico"}) return n.PageName, n.id ORDER BY n.id
def queryTwo(tx):
    print("Resultado del query:\n\tMATCH (n:Article {Category:\"Mammals_of_Mexico\"}) return n.PageName, n.id ORDER BY n.id")
    print("ID\tPageName")
    for record in tx.run("MATCH (n:Article {Category:\"Mammals_of_Mexico\"}) return n.PageName, n.id ORDER BY n.id"):
        print(str(record["n.id"])+"\t"+record["n.PageName"])
    print("\n")
    return


#Paginas que su título incluya el nombre Samantha
#MATCH (n:Article) WHERE n.PageName CONTAINS 'Samantha' RETURN n.id, n.PageName, n.Category ORDER BY n.id
def queryThree(tx):
    print("Resultado del query:\n\tMATCH (n:Article) WHERE n.PageName CONTAINS 'Samantha' RETURN n.id, n.PageName, n.Category ORDER BY n.id")
    print("ID\tPageName\t\tCategory")
    for record in tx.run("MATCH (n:Article) WHERE n.PageName CONTAINS 'Samantha' RETURN n.id, n.PageName, n.Category ORDER BY n.id"):
        print(str(record["n.id"])+"\t"+record["n.PageName"]+"\t\t"+str(record["n.Category"]))
    print("\n")
    return

choice = 0
while choice != 4:
    choice = menu()
    if choice == 1:
        with driver.session() as session:
            session.read_transaction(queryOne)
    elif choice == 2:
        with driver.session() as session:
            session.read_transaction(queryTwo)
    elif choice == 3:
        with driver.session() as session:
            session.read_transaction(queryThree)