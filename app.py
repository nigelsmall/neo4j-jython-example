#!/usr/bin/env jython
# -*- encoding=utf8 -*-

from org.neo4j.graphdb.factory import GraphDatabaseFactory
from org.neo4j.index.lucene import LuceneIndexProvider
from org.neo4j.kernel import ListIndexIterable
from org.neo4j.kernel.impl.cache import SoftCacheProvider
from org.neo4j.cypher.javacompat import ExecutionEngine

cache_providers = [SoftCacheProvider()]

index_providers = ListIndexIterable()
index_providers.setIndexProviders([LuceneIndexProvider()])

factory = GraphDatabaseFactory()
factory.setCacheProviders(cache_providers)
factory.setIndexProviders(index_providers)

database = factory.newEmbeddedDatabase("data")
try:
    cypher = ExecutionEngine(database)
    result = cypher.execute('CREATE (a {name:"Alice"}) RETURN a', {})
    for row in result.iterator():
        for column in result.columns():
            print("{0} = {1}".format(column, row[column]))
finally:
    database.shutdown()

