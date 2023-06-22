
This repository contains the solution of one of the groups participating in [the LDAC2023 hackathon](https://github.com/SSoLDAC-2023). 

# Group 2

## Challenge name: Data Dictionaries
## Group name: "Be as DoDos"
## Idea
When adding content to the bSDD you can link your classes and definitions to existing resources. However, many content creators do not link their terms -- they may not even be aware which similar terms have been defined elsewhere. In this solution we provide code to suggest related terms within bSDD in three ways:
1. Within a term's description, identify potential hyperlinks to bSDD terms.
2. Identify similar terms based on its `name` and `description`:
  * Semantic similarity, which relies on `sentence-transformers/all-mpnet-base-v2` embeddings
  * Span overlap similarity, following some work on [Intelligent Regulatory Compliancy (iReC)](https://github.com/rubenkruiper/irec)


## Group members
* [Rebekka Benfer](https://www.th-koeln.de/personen/rebekka.benfer/)
* [Aaron Costin](https://dcp.ufl.edu/faculties/costin-aaron/)
* [Ruben Kruiper](https://www.rubenkruiper.com/)
* [Giulia Maslov](https://www.researchgate.net/profile/Giulia-Maslov)
* [Artur Tomczak](https://www.ntnu.edu/employees/artur.b.tomczak)


## Challenge-related links with more information towards bSDD:
bSDD page:  http://bsdd.buildingsmart.org/ 
Documentation:  https://github.com/buildingSMART/bSDD
Data model:  https://github.com/buildingSMART/bSDD/.../bSDD
Search GUI:  https://search.bsdd.buildingSMART.org 
API docs:  https://app.swaggerhub.com/apis/buildingSMART/Dictionaries/v1
Management platform:  https://manage.bsdd.buildingsmart.org/
Same three on test server:
- https://search-test.bsdd.buildingsmart.org/
- https://test.bsdd.buildingsmart.org/swagger/index.html
- https://manage-test.bsdd.buildingsmart.org/
Forum:  https://forums.buildingsmart.org/c/users/bsdd/14 
Support mail:  bsdd_support@buildingsmart.org
Validation service:  https://validate.buildingsmart.org/
