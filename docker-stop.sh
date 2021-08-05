cd docker-compose;
envsubst < docker-compose.yaml.template > docker-compose.yaml
docker-compose -f docker-compose.yaml down
