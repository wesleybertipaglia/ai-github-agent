#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$SCRIPT_DIR/../../.."

echo "[$(date)] Iniciando execução do agente..." >> "$SCRIPT_DIR/log.log"

source "$PROJECT_DIR/venv/bin/activate"

make run

echo "[$(date)] Execução finalizada." >> "$SCRIPT_DIR/log.log"
