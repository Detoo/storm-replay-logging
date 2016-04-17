build_topology:
	docker-compose run --rm pyleus-env pyleus -v build -s topology.yml

debug_topology:
	docker-compose run --rm pyleus-env pyleus local app.jar
