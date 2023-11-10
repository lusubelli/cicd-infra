import subprocess

# Commande Docker Compose
docker_compose_command = ["docker-compose", "-f", "ci-infra.yml", "up", "-d"]

# Exécutez la commande Docker Compose
subprocess.run(docker_compose_command)