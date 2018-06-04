from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlWrapper(object):
    @classmethod
    def insert(self, query_url):
            sparql = SPARQLWrapper("http://"+str(query_url)+":3030/factory/update")
            sparql.setQuery("""
           PREFIX factory: <http://0.0.0.0/factory#>
            INSERT DATA{ 
                    factory:sensor107  a     factory:sensor ;
                    factory:id       "107" ;
                    factory:version  "0.1" .
            } 
            """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            for result in results["results"]["bindings"]:
                print(result["label"]["value"])
            return str(results)

    @classmethod
    def request(self,query_url):
            sparql = SPARQLWrapper("http://"+str(query_url)+":3030/factory/query")
            sparql.setQuery("""
                PREFIX factory: <http://0.0.0.0/factory#>
                SELECT *
                WHERE { 
                    { 
                    ?sensor a factory:sensor.
                    ?sensor factory:id ?sensor_id.
                    ?sensor factory:version ?sensor_version
                    }
                } 
            """)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            for result in results["results"]["bindings"]:
                print(result["label"]["value"])
            return results
