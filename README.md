# Gerenciador de Tarefas CLI (python)

Objetivo: gerenciar tarefas via terminal com persistência local (JSON).

Funcionalidades MVP:
- Adicionar tarefa (title, due, priority, tags)
- Listar tarefas (filtros por status, priority, tag)
- Marcar como concluida
- Editar
- Remover
- Exportar em JSON/CSV

Padrões:
- IDs curtos (8 hex)
- `due`no formato DD-MM-YYYY
- status: fazer | fazendo | feito
- priority: baixa | media | alta
