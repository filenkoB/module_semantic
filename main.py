# Task 1
from rdflib import Graph, RDF, Namespace

def calculate_area(continent, graph):
    area = 0
    for country in graph.subjects(default["part_of_continent"], continent):
        area = area + float(graph.value(country, default["area_in_sq_km"]))
    return area

default = Namespace("http://example.com/demo/")

graph = Graph()
graph.parse("./countrues_info.ttl")
result = []

for continent in graph.subjects(RDF.type, default["Continent"]):
    continent_name = str(graph.value(continent, default["continent_name"]))
    total_area = calculate_area(continent, graph)
    result.append([continent_name, total_area])

print(result)

# #Task 3
# from SPARQLWrapper import SPARQLWrapper, JSON
#
# sparql = SPARQLWrapper('https://dbpedia.org/sparql')
# query = '''
#     SELECT ?country ?country_name ?population
#     WHERE {
#         ?country rdf:type dbo:Country ;
#             dbo:language dbr:English_language ;
#             rdfs:label ?country_name ;
#             dbo:populationTotal ?population .
#         FILTER(LANG(?country_name) = 'uk') .
#     }
#     ORDER BY DESC (?population)
# '''
#
# sparql.setQuery(query)
# sparql.setReturnFormat(JSON)
#
# query_res = sparql.query().convert()
# for country in query_res["results"]["bindings"]:
#     print(country["country"]["value"], country["country_name"]["value"], country["population"]["value"], sep=" --- ")
