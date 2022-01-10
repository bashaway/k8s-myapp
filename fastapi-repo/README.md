# fastapi-repo

## Additional Status Code

from starlette/status.py

https://github.com/encode/starlette/blob/master/starlette/status.py

```
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
```

# directory structure

```
.
|-- Dockerfile
|-- README.md
|-- _build
|   |-- docker_build.sh ------------> publish private docker registry
|   |-- k8s_makeyaml.sh ------------> make yaml files from deploy/tmpl directory
|   |-- k8s_deploy.sh --------------> deploy deploy/*.yaml files
|   `-- k8s_delete.sh --------------> delete deploy/*.yaml files
|-- deploy
|   |-- config
|   |   |-- init.sql ---------------> ( optional ) database initial data
|   |   `-- my.cnf -----------------> ( optional ) mysql config
|   `-- tmpl
|       |-- configmap.tmpl ---------> configmap template ( deploy/config/* -> deploy/02config_*.yaml)
|       |-- deployment -------------> deployment template
|       |-- environment ------------> environment template
|       |-- ingress ----------------> ingress template
|       `-- service ----------------> service template
`-- fastapi
    |-- db.py ----------------------> database connection info
    |-- _generator -----------------> code generator
    `-- xxx ------------------------> generated code
        |-- router.py ----------------> path routing 
        |-- crud.py ------------------> database functions
        `-- model.py -----------------> SQLModel model
```

# debug

## sample database

https://dev.mysql.com/doc/index-other.html

https://downloads.mysql.com/docs/world-db.tar.gz

https://downloads.mysql.com/docs/world_x-db.tar.gz

https://downloads.mysql.com/docs/sakila-db.tar.gz

https://downloads.mysql.com/docs/menagerie-db.tar.gz

