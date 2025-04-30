VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
ACTIVATE = $(VENV_DIR)/bin/activate

.PHONY: help venv install run clean freeze activate deactivate

help:
	@echo "Comandos disponíveis:"
	@echo "  make venv     - Cria o ambiente virtual"
	@echo "  make install  - Instala as dependências do projeto"
	@echo "  make run      - Executa o script do bot"
	@echo "  make clean    - Remove o ambiente virtual"
	@echo "  make freeze   - Gera o arquivo requirements.txt"

venv:
	@echo "Criando ambiente virtual..."
	python3 -m venv $(VENV_DIR)

install: venv
	@echo "Instalando dependências..."
	$(PIP) install -r requirements.txt

freeze:
	@echo "Gerando requirements.txt..."
	$(PIP) freeze > requirements.txt

run:
	@echo "Rodando o bot..."
	PYTHONPATH=./src $(PYTHON) src/main.py

clean:
	@echo "Removendo ambiente virtual..."
	rm -rf $(VENV_DIR)
