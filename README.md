# GitHub AI Agent

Um agente simples em Python que consulta issues de um repositório GitHub, resume usando IA (Google Gemini) e envia notificações para o Discord. O objetivo deste projeto é didático: aprender mais sobre integração entre APIs, IA generativa e automação via cron jobs.

## 📑 Índice

- [Funcionalidades](#funcionalidades)
- [Como começar](#como-começar)
- [Exemplo de uso](#exemplo-de-uso)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 📦 Funcionalidades

- [x] Consultar issues de um repositório no GitHub
- [x] Resumir issues com IA (Gemini API)
- [x] Enviar mensagens no Discord
- [x] Agendamento automático via cron job
- [ ] Suporte a discussões do GitHub
- [ ] Integração com outras ferramentas (e-mail, Telegram, etc.)

## 🚀 Como começar

### Pré-requisitos

- Python 3.9+
- Ambiente virtual (recomendado)
- Conta e token do Discord
- Chave de API do Google Gemini
- Token de acesso do GitHub

### Executando o projeto

1. Configurando o Ambiente

```bash
# clona o projeto e acessa o diretorio
git clone https://github.com/seu-usuario/ai-github-agent.git
cd repository-agent

# cria um ambiente virtual e atova
make venv
source venv/bin/activate

# instala as dependencias
make install
```

2. Configure suas variáveis em [.env](.env) usando como exemplo o [.env.example](.env.example)

3. Execute manualmente

```bash
make run
```

4. Ou configure o cron job

```bash
make add-cron
```

## 📖 Exemplo de uso

Toda vez que o agente rodar, ele:

- Consulta as issues abertas no GitHub.
- Resume o conteúdo via Gemini.
- Envia a notificação no Discord.
- Loga a execução no arquivo jobs/monitor/log.log.

## 🤝 Contribuindo
Contribuições são bem-vindas! Se tiver sugestões, melhorias ou quiser adicionar novas integrações, fique à vontade para abrir uma issue ou pull request.

## 📜 Licença
Este projeto está sob a licença [MIT](LICENSE). Veja o arquivo LICENSE para mais detalhes.