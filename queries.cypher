#Nodos que tengan relacion de Hyperlink con la página "List of Missouri highways"
MATCH (n:Article {PageName:"List of Missouri highways"}) <-[:Hyperlink]-> (b) RETURN b.PageName, b.id, b.Category ORDER BY b.id

#Nodos que pertenezcan a la categoría Mammals_of_Mexico
MATCH (n:Article {Category:"Mammals_of_Mexico"}) return n.PageName, n.id ORDER BY n.id

#Paginas que su nombre incluya la palabra "Samantha"
MATCH (n:Article) WHERE n.PageName CONTAINS 'Samantha' RETURN n.id, n.PageName, n.Category ORDER BY n.id