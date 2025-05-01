from dtos.issue import IssueDTO

def template_issue(issue_dto: IssueDTO) -> str:
    return f"""
## Issue #{issue_dto.id}: {issue_dto.title}

**Link:** {issue_dto.url}
**Criado por:** {issue_dto.assignee or 'Não atribuído'}
**Data de Criação:** {issue_dto.created_at}
**Labels:** {', '.join(issue_dto.labels) if issue_dto.labels else 'Nenhum rótulo'}

### Descrição:
{issue_dto.body or "Sem descrição."}

### Análise:
{issue_dto.analise}

### Sugestão:
{issue_dto.sugestao}
""".strip()
