BACKUP_DBS = bank injectengine scoreengine
DOCKER_RUN = docker run --rm --network lockdown_default
FILES_DIR = $(PWD)/files
TIMESTAMP = $(shell date +%Y-%m-%d--%H-%M-%S)

all: run

run:
	docker stack deploy -c stack.yml lockdown

stop:
	docker stack rm lockdown

backups:
	mkdir -p backups
	for db in $(BACKUP_DBS) ; do \
		$(DOCKER_RUN) \
		       mariadb \
		       mysqldump -h database -u root -pchangeme $$db > backups/$$db--$(TIMESTAMP).sql & \
	done

setup: setup-bank setup-ie2 setup-se2

setup-bank:
	$(DOCKER_RUN) \
		-v $(FILES_DIR)/bank_config.py:/opt/bank-api/config.py \
		ubnetdef/bank-api \
		python setup.py

setup-ie2:
	$(DOCKER_RUN) \
		-v $(FILES_DIR)/ie2.env:/srv/ie2/.env \
		ubnetdef/ie2 \
		app/Console/cake engine install

setup-se2:
	$(DOCKER_RUN) \
		-v $(FILES_DIR)/se2_config.yml:/opt/scoreengine2/config.yml \
		ubnetdef/scoreengine2 \
		db init

.PHONY: all run stop backups setup setup-bank setup-ie2 setup-se2
