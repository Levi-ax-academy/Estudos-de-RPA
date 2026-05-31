# RPA & Inteligência Artificial

Bem-vindo ao repositório central dos meus estudos e anotações referentes a **Robotic Process Automation (RPA)** e **Inteligência Artificial (IA)**. 

Este material está sendo desenvolvido e continuamente atualizado durante a minha participação no curso de capacitação **AIX_ACADEMY**, servindo tanto como um portfólio de aprendizado quanto como uma base de consulta para implementações e conceitos técnicos.

---

## 🏗️ Arquitetura e Boas Práticas

Um dos principais focos deste repositório é manter um código limpo, escalável e de fácil manutenção. Para isso, o desenvolvimento dos scripts de automação e IA busca seguir rigorosamente as boas práticas e princípios de engenharia de software:

* **Princípios SOLID:** A estrutura de pastas e a separação de responsabilidades dos scripts tentam refletir os conceitos do SOLID, garantindo que as classes e funções tenham propósitos únicos e bem definidos.
* **Programação Orientada a Objetos (POO):** Alguns dos módulos centrais estão estruturados em POO para facilitar o encapsulamento, o reaproveitamento de código e a manutenção lógica das automações.

---

## 📂 Estrutura do Repositório

O repositório está organizado de forma hierárquica por assunto. Dentro de cada tema de estudo, a arquitetura interna segue a padronização abaixo para isolar as lógicas de negócio, utilitários e recursos compartilhados:

```text
📁 [Nome do Assunto ou Projeto]/
└── 📁 src/
    ├── 📁 modulos/
    │   └── 📁 [nome_do_modulo]/
    │       └── (Arquivos, classes e pastas específicas geradas conforme o módulo evolui)
    ├── 📁 shared/       # Recursos, interfaces ou dados compartilhados entre múltiplos módulos
    └── 📁 utils/        # Funções utilitárias e scripts auxiliares (ex: formatação, manipulação de arquivos)
