#Creación de nodos

CREATE CONSTRAINT ON (a:Article) ASSERT a.id IS UNIQUE

USING PERIODIC COMMIT 10000 LOAD CSV WITH HEADERS FROM "file:///C:/wiki-topcats-page-names.csv" AS ROW FIELDTERMINATOR ';' CREATE (a:Article { id:toInt(ROW.id), PageName: ROW.PageName});

#Relaciones

USING PERIODIC COMMIT 10000 LOAD CSV WITH HEADERS FROM "file:///C:/wiki-topcats.csv" AS ROW FIELDTERMINATOR ';' MATCH (a:Article {id:toInt(ROW.id1)}) MATCH (b:Article {id: toInt(ROW.id2)}) CREATE (a)-[:Hyperlink]->(b);

#Añadir categorias a los nodos

USING PERIODIC COMMIT 10000 LOAD CSV WITH HEADERS FROM "file:///C:/wiki-topcats-categories.csv" AS ROW FIELDTERMINATOR ';' MATCH (a:Article {id:toInt(ROW.id)}) SET a.Category = ROW.Category