# INFRASTRUCTURE DE CONTINOUS INTEGRATION ET DE CONTINOUS DELIVERY

## Installation

Il faut dans un premier temps s'assurer que le service docker est bien up.

Et verifier l'installation de docker, pour cela il faut ouvrir le terminal de son choix et saisir la commande suivante :
```
docker version
```

Ainsi que l'installation de docker-compose en saisissant la commande suivante :
```
docker-compose version
```

### Demarrage

Configurez les mots de passe dans le fichier `.env`

```
.\ci-start.py
```

### Configuration d'un gitlab runner

Accéder à [Gitlab](http://localhost:80)
Connectez-vous avec l'identifiant par défaut `root` 
et le mot de passe définit précedemment dans le fichier `.env`
dans la variable `GITLAB_ROOT_PASSWORD`

Créez votre projet GitLab.
Allez dans votre projet GitLab.

Pour créer un Token d'enregistrement pour le Runner:
Dans le menu à gauche, accédez à **Settings > CI / CD > Runners.**
Notez le token affiché sous la section **"Set up a specific Runner manually"**.

Créez un fichier `gitlab-runner/config/config.toml` et remplacez **GITLAB_TOKEN** par le token généré précédemment.
```
[[runners]]
    name = "shell"
    url = "http://gitlab/"
    token = "GITLAB_TOKEN"
    limit = 2
    executor = "shell"
    builds_dir = ""
    shell = "bash"
```

Vérifier l'enregistrement
Retournez dans l'interface web de GitLab, allez dans votre projet, puis dans 
**Settings > CI / CD > Runners**. Vous devriez voir votre runner enregistré dans la liste.

### Configuration de sonar

Accéder à [Sonarqube](http://localhost:9000)
Connectez-vous avec l'identifiant par défaut `admin`
et le mot de passe `admin`

### Arret
```
.\ci-stop.py
```
