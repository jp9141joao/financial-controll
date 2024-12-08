# 💸 **Controle de Contas** 🏦

Um programa interativo para gerenciar finanças pessoais, incluindo gastos, ganhos, controle de saldo, extratos e exclusão de registros. Ideal para quem deseja organizar seu orçamento de maneira simples e eficiente.

---

## 🚀 **Visão Geral do Projeto**

O programa implementa funcionalidades essenciais para gerenciamento financeiro:

- **Adicionar Gastos e Ganhos:** Classificação por tipo (essencial, supérfluo, constante, ou inconstante).
- **Mostrar Gastos e Ganhos:** Visualização de resumos financeiros.
- **Excluir Registros:** Permite a remoção de gastos ou ganhos, ajustando o saldo automaticamente.
- **Mostrar Extrato:** Exibição completa das transações realizadas com saldo atualizado.
- **Gerenciamento de Crédito:** Opção de adicionar crédito ao saldo principal.

---

## 🛠️ **Recursos Principais**

### Funcionalidades:
- **Adicionar Gasto:** Divisão entre gastos essenciais (ex.: aluguel, saúde) e gastos supérfluos (ex.: entretenimento).
- **Adicionar Ganho:** Registros com diferenciação entre ganhos constantes e ganhos variáveis.
- **Resumo de Gastos e Ganhos:** Exibição detalhada de todos os gastos e ganhos.
- **Excluir Gastos/Ganhos:** Remove transações com ajuste no saldo automaticamente.
- **Extrato Completo:** Apresenta todos os lançamentos realizados com seu impacto no saldo.
- **Gerenciamento de Crédito:** Ajuste do saldo com base em um limite de crédito configurado no início.

---

## ⚙️ **Configuração**

### Pré-requisitos
- Python 3.x deve estar instalado no sistema.

---

## ▶️ **Como Executar**

1. Clone este repositório no seu ambiente local:
```bash
git clone https://github.com/seu-usuario/gerenciador-financas.git
```

2. Instale qualquer dependência necessária caso necessário (não há dependências externas para este código).

3. Execute o código no terminal com:
```bash
python seu_arquivo.py
```

---

## 🎮 **Como Funciona**

### Menu Principal:

Após iniciar, o usuário verá o seguinte menu:

```
Menu:
1 - Adicionar gastos
2 - Adicionar ganhos
3 - Mostrar gastos
4 - Mostrar ganhos
5 - Mostrar extrato
6 - Sair
```

### Opções:

1. **Adicionar Gastos:**  
   Inclui gastos essenciais ou supérfluos com ajuste automático no saldo.

2. **Adicionar Ganhos:**  
   Inclui ganhos como salário ou investimento com opção de classificar se é constante ou inconstante.

3. **Mostrar Gastos:**  
   Exibe uma lista com todos os gastos categorizados.

4. **Mostrar Ganhos:**  
   Exibe uma lista com todos os ganhos categorizados.

5. **Mostrar Extrato:**  
   Exibe todas as transações (gastos e ganhos) e exibe o saldo atualizado.

6. **Sair:**  
   Encerra o programa.

---

## 💬 **Tecnologias Utilizadas**

- **Python 3.x**: Lógica central do programa.
- Manipulação de dados com listas simples.
- Limpeza da tela com `os.system('cls')` para experiência amigável no console.

---

## 📊 **Exemplo de Uso**

Após iniciar o programa, você verá opções interativas no console:

```
Digite o saldo da sua conta: R$1000
Sua conta possui crédito?
1- Sim
2- Não
R: 1
Digite o limite da sua conta: R$500
Saldo + crédito configurado.
```

Menu principal com opções:

```
Menu:
1 - Adicionar gastos
2 - Adicionar ganhos
3 - Mostrar gastos
4 - Mostrar ganhos
5 - Mostrar extrato
6 - Sair
```

---

Agora você pode organizar suas finanças de forma prática com este gerenciador! 💡✨