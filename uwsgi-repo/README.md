# uwsgi-repo

uwsgi application


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
|   |   |-- emperor.ini ------------> uWSGI config file ( emperor mode )
|   |   |-- bottle-sample-01.ini ---> uWSGI application config file
|   |   `-- bottle-sample-02.ini ---> uWSGI application config file
|   `-- tmpl
|       |-- configmap.tmpl ---------> configmap template ( deploy/config/* -> deploy/02config_*.yaml)
|       |-- deployment -------------> deployment template
|       |-- environment ------------> environment template
|       |-- ingress ----------------> ingress template
|       `-- service ----------------> service template
`-- uwsgi
    |-- bottle-sample-01 -----------> uWSGI application resources
    |   |-- main.py
    |   |-- static
    |   |   `-- table.js
    |   `-- views
    |       `-- index.html
    `-- bottle-sample-02 -----------> uWSGI application resources
        `-- main.py
```

