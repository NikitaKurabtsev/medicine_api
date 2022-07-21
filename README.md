Medicine API

## API CRUD operations with Company and Medicine objects

### Collections/Resources

* Company

| Verb   | URL                   | Descripton                                         | Scope                    |
|--------|-----------------------|----------------------------------------------------|--------------------------|
| GET    | /api/v1/companies/    | Get the collection of Companies by ascending order | Company Collection       |
| GET    | /api/v1/companies/id/ | Get a single Company by id                         | Company                  |
| PUT    | /api/v1/companies/id/ | Update a single Company by id                      | Company                  |
| PATCH  | /api/v1/companies/id/ | Update one or more fields of an existing Company   | Company                  |
| DELETE | /api/v1/companies/id/ | Delete a single Company by id                      | Company                  |
| POST   | /api/v1/companies/    | Create a new Company in the collection             | Company                  |

* Medicine

| Verb   | URL                   | Descripton                                         | Scope                    |
|--------|-----------------------|----------------------------------------------------|--------------------------|
| GET    | /api/v1/medicines/    | Get the collection of Medicines by ascending order | Medicine Collection      |
| GET    | /api/v1/medicines/id/ | Get a single Medicine by id                        | Medicine                 |
| PUT    | /api/v1/medicines/id/ | Update a single Medicine by id                     | Medicine                 |
| PATCH  | /api/v1/medicines/id/ | Update one or more fields of an existing Medicine  | Medicine                 |
| DELETE | /api/v1/medicines/id/ | Delete a single Medicine by id                     | Medicine                 |
| POST   | /api/v1/medicines/    | Create a new Medicine in the collection            | Medicine                 |


### Flow of data
**GET** -> Model -> Serializer -> JSONRenderer -> Response

**POST/PUT** -> JSONParser(request) -> Serializer -> Model -> JSONRenderer -> Response
