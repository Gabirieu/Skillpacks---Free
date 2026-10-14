# Code Review Rubric Architect - guia de uso

## Objetivo

Use when creating code review rubrics, decision standards, escalation rules, and coaching structure for engineering teams.

## Quando acionar

- the task needs senior-level structure, tradeoffs, and execution guidance
- ownership, risk, rollout, or compatibility concerns are significant
- the work must end in something reviewable and operationally usable

## Quando evitar

- the task is a tiny isolated tweak with no real architectural, operational, or governance consequence
- generic advice is enough and no domain-specific judgment is required

## Entradas úteis

- current delivery workflow, bottlenecks, and team pain points
- toolchain, CI/CD design, and environment model
- approval, compliance, and evidence requirements

## Exemplos de invocação

- `/code-review-rubric-architect audite este cenário, identifique riscos principais, proponha direção recomendada e plano de rollout`
- `/code-review-rubric-architect revise esta implementação e devolva uma versão mais profissional, segura e operacional`
- `/code-review-rubric-architect monte um checklist de validação, rollout, riscos e critérios de aceite`

## Saída esperada

- diagnóstico, direção recomendada, execução e validação

## Observações

- Use o nome exato da skill ao invocar.
- Anexe logs, arquivos, prints, layout, consultas ou trechos de código quando houver.
- Declare o formato desejado da resposta: plano, parecer, checklist, arquitetura, auditoria, rollout ou correção.
