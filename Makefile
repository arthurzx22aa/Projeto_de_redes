PYTHON = python3

start:

	@echo "iniciando servidores"
	$(PYTHON) -m servers.name_server &
	@sleep 1
	
	$(PYTHON) -m servers.udp_server &
	@sleep 1

	$(PYTHON) -m servers.tcp_server &
	@sleep 1

	@echo "Iniciando clientes"
	$(PYTHON) -m clients.inexistent_client
	$(PYTHON) -m clients.udp_client
	$(PYTHON) -m clients.tcp_client


	@pkill -f "[s]ervers\."