# Pydantic client example

Example of microservices application that uses generated client library 
for interservice communication. Client library employs **pydantic**-based DTO classes 
from a shared library and is generated using 
https://github.com/ivasio/fastapi_client/tree/develop .

When developing several applications in the same language (and sometimes the same tech 
stack) it is common to move DTO (Data Transfer Object) classes to separate package. It 
may be useful to build rich domain model based on shared DTO classes with further 
possible extension in individual applications (microservices in this case). But usually 
when using OpenAPI-based code generation for client libraries new DTO classes are 
generated every time "from scratch" which discourages using shared DTOs with common 
logic.

Approach presented in https://github.com/ivasio/fastapi_client/tree/develop is based on 
following "optimistic" assumption: given an OpenAPI model with a certain name, if class 
with the **same name** is present in DTOs module, it is used by the client library. 
Otherwise, new class is generated. 

## Project contents

Client code generation util is located in 
https://github.com/ivasio/fastapi_client/tree/develop . Illustration presented in 
current project consists of
- **common_models** package with pydantic DTO classes (located in common)
- 2 microservices
    - **petstore** - microservice that is being requested (located in 
      microservices/petstore)
    - **personal page**  - microservice that requests **petstore** (located in 
      microservices/personal_page)
- **petstore_httpx_client** - generated client library used to reqest **petstore** 
  microservice (located in 
  microservices/petstore/client-python-httpx/petstore_httpx_client)

**petstore_httpx_client** generation takes OpenAPI spec of **petstore** service as an
input (located in microservices/petstore/swagger.json). For every OpenAPI model 
DTO model from **common_models** is imported. In case of its absence new pydantic 
model is generated in client library code

**personal page** service serves as a proxy to **petstore** service and implements 
2 methods:
- **GET /orders** - retrieves the information about all placed orders
- **PUT /orders** - places new order by invoking **POST /orders** method of 
  **petstore** service

Implementations of these methods are purely illustrative

