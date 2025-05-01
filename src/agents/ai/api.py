from google import genai
from settings import GEMINI_API_KEY
import re

client = genai.Client(api_key=GEMINI_API_KEY)

def resumir_issues(issues: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=f"Resuma as seguintes issues do GitHub:\n{issues}"
    )
    return response.text

def analisar_issue(issue):
    prompt = f"""
Analise a seguinte issue do GitHub e determine:
- Se é um bug real
- Qual a prioridade (Crítica, Alta, Média, Baixa)
- Sugira uma ação ou encaminhamento.

Issue:
Título: {issue.get('title')}
Descrição: {issue.get('body') or 'Sem descrição.'}
"""

    response = client.models.generate_content(
        model="gemini-2.0-pro",
        contents=prompt
    )
    texto = response.text.strip()
    return processar_resposta(texto)

def processar_resposta(texto):
    analise_match = re.search(r'### Análise:\n(.+?)(?=\n###|\Z)', texto, re.DOTALL)
    sugestao_match = re.search(r'### Sugestão:\n(.+)', texto, re.DOTALL)

    analise = analise_match.group(1).strip() if analise_match else "Análise não disponível."
    sugestao = sugestao_match.group(1).strip() if sugestao_match else "Sugestão não disponível."

    return analise, sugestao
