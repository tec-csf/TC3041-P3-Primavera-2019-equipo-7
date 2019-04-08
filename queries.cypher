#Nodos que tengan relacion de Hyperlink con la página "List of Missouri highways"
MATCH (n:Article {PageName:"List of Missouri highways"}) <-[:Hyperlink]-> (b) RETURN b

#Nodos que pertenezcan a la categoría Mammals_of_Mexico
MATCH (n:Article {Category:"Mammals_of_Mexico"}) return n

#Paginas que su nombre incluya la palabra "Samantha"
MATCH (n:Article) WHERE n.PageName CONTAINS 'Samantha' RETURN n