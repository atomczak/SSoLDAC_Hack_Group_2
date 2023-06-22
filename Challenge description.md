# Challenge: Data Dictionary

## Champions
- Artur Tomczak, buildingSMART International 
- Vladimir Alexiev, Ontotext  

## Challenge description
### Background 
Data dictionaries are repositories of concepts, their meaning, properties to describe them, and relations between self and other dictionaries. Data dictionaries can be considered ontologies with relations to other ontologies. 
The bSDD - buildingSMART Data Dictionary - is a free service for hosting such data dictionaries. It is a common reference library in the AEC industry. There are many applications that integrate with bSDD, providing meaning to BIM data and supporting the enrichment of IFC models. 

bSDD content can be browsed using the search page [1], but the primary interface to bSDD is a REST API [3]. The API can return all data in JSON or HTML format, and the classifications can also be requested as JSON or RDF/Turtle entities using their semantic URL. There is also a prototype of a GraphQL API available [4]. 

Ontotext has reviewed bSDD, and made a report on the limitations and possibilities for improvement of the JSON, RDF and GraphQL options, and proposed an improved GraphQL API and SPARQL endpoint for bSDD, available for testing [5]. 

### Objectives 

Some dictionaries might contain overlapping or similar concepts. For example, there could be two that have a concept of a “wall”. If two such dictionaries are not directly related but both of them are related to another, third dictionary, we can say they are indirectly related. In other words, the two dictionaries can be represented with a joint graph. An example could be a ‘wall’ that is in both Uniclass and CCI classification. Even though they are not directly related, both have relations to IfcWall class. 
Right now, it is difficult to find indirect relations in bSDD. Using data available in bSDD, we would like you to demonstrate how Semantic technologies can support finding such relations between dictionaries. You can also use SPARQL or SHACL to find data quality problems, and propose or implement fixes. 
While working on solving the challenge, please note the limitations and possible improvements that you would like to propose to the bSDD project. In the Ontotext report you will see an initial list of what has already been proposed, and in the “future-work” section what else could be improved. Trying to address some of the aspects in your solution, will be of additional value. 

## Challenger research questions
- How can we analyze how data dictionaries are (in)directly related to each other? 
- Is such analysis possible without downloading all related dictionaries to a triple store, but with the API available today? 

### Additional
- Can we use this solution to create new mappings between data dictionaries?  
- Can we use this solution to find incorrect/contradictory relationships?  
- How can we perform quality checks on bSDD data using linked data technology? 
- What could be improved in the bSDD service to make it easier or more useful? 
- What could make bSDD more F.A.I.R. [6]? 

## Datasets
https://bsdd.buildingsmart.org 
https://bsdd.ontotext.com/ 

In particular, here are the examples mentioned above: 
- IFC namespace: https://identifier.buildingsmart.org/uri/buildingsmart/ifc-4.3/  
- IFC IfcWall page: https://search.bsdd.buildingsmart.org/Classification/Index/71147 
- Uniclass namespace: https://identifier.buildingsmart.org/uri/nbs/uniclass2015-1/ 
- Uniclass “Wall and barrier elements”: https://search.bsdd.buildingsmart.org/Classification/Index/6670 
- CCI Construction namespace: https://identifier.buildingsmart.org/uri/molio/cciconstruction-1.0/  
-- CCI Construction wall page: https://search.bsdd.buildingsmart.org/Classification/Index/75100  

## Supplementary Resources

1. Search page of bSDD https://search.bsdd.buildingsmart.org/  
2. bSDD documentation on github: https://github.com/buildingSMART/bSDD    
3. bSDD Rest API (interactive) documentation: https://test.bsdd.buildingsmart.org/swagger/index.html   
4. bSDD GraphQL API interactive console: https://test.bsdd.buildingsmart.org/graphiql/   
5. Ontotext report “Semantic bSDD” https://bsdd.ontotext.com/ with detailed analysis of possible improvements, prototypes of new SPARQL endpoint, GraphQL endpoint, schema and graph visualizations. See https://bsdd.ontotext.com/README.html for detailed description, and https://bsdd.ontotext.com/README.html#future-work for further improvement ideas. 
6. FAIR data principles: https://www.go-fair.org/fair-principles/    
7. Draft bSDD ontology: https://github.com/buildingSMART/bSDD/blob/master/RDF/preview-bsdd-rdfs-0.4.ttl  
