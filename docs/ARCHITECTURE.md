# SixTech Workspace Architecture

## Visão Geral

SixTech Workspace é uma plataforma multiagente baseada em IA.

## Arquitetura

Usuário
    │
    ▼
Open WebUI
    │
    ▼
Super Agent (CrewAI)
    │
 ┌──┼─────────┬─────────┬─────────┐
 ▼  ▼         ▼         ▼         ▼

Developer
Research
Legal
Designer
Documents

## Componentes

### Open WebUI

Interface principal.

### Super Agent

Orquestrador dos agentes.

Baseado em CrewAI.

### Developer Agent

Baseado em OpenHands.

### Research Agent

Pesquisa profunda.

### Legal Agent

Contratos e documentos jurídicos.

### Designer Agent

Design, UI/UX e imagens.
### Documents Agent

PDFs, Word, relatórios e propostas.
