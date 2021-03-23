# Operateur de composition de service
L'objectif du projet est de créer un opérateur de composition de service SaaS 
de type application et de service PaaS de type serveur apache.

On se base sur l'API Docker SDK for Python pour le créer


### prerequisite Installations
```
pip install docker

```

### Program execution

![executionShell](https://user-images.githubusercontent.com/56063183/112076071-fdc85380-8b79-11eb-98a0-add0619ae683.PNG)

The program is executed on the shell using this command line for example
```
python SaaS.py https://github.com/misterelgo/PHP-MySQL-CRUD-Web-Application.git misterelgo/saas

```
We have 3 arguments here handled by the module sys.argv: 
1. Program name: SaaS.py
2. Git application link
3. image name: misterelgo/saas

### Results
![resutlPushing](https://user-images.githubusercontent.com/56063183/112076045-ee490a80-8b79-11eb-9b9e-9b9394bb2f3c.PNG)
