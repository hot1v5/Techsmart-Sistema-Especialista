# 💻 TechSmart - Sistema Especialista

Sistema Especialista desenvolvido em Python e Streamlit para recomendar computadores com base no perfil, necessidades e orçamento do usuário.

🎓 Contexto acadêmico
Projeto desenvolvido para a disciplina de Programação de Sistemas Especialistas, no curso de Ciência da Computação da Universidade Veiga de Almeida.

## 🎯 Objetivo

Auxiliar clientes de uma loja de informática na escolha de um computador adequado às suas necessidades.

## 🧠 Como funciona

O sistema utiliza:

- Base de fatos;
- 25 regras;
- Motor de inferência;
- Encadeamento para frente;
- Prioridade entre recomendações;
- Módulo de explicação.

Fluxo:

```text
Usuário
   ↓
Interface Streamlit
   ↓
Fatos
   ↓
Regras
   ↓
Motor de inferência
   ↓
Recomendação
```

## 📸 Interface do sistema

### Tela inicial

<img width="760" height="908" alt="tela Principal" src="https://github.com/user-attachments/assets/aa1ab4b9-b661-4fb2-863d-ccdb1b2e40f3" />



### Resultado da recomendação

<img width="793" height="812" alt="configuração sugerida" src="https://github.com/user-attachments/assets/b65b7366-4dbd-4294-9778-3d953968a3bf" />



💻 O sistema considera
- Orçamento
- Finalidade de uso
- Jogos
- Programação
- Edição de vídeo
- Multitarefa
- Armazenamento
- Desempenho
- Máquinas virtuais
- Ferramentas pesadas
- Arquivos grandes
  
🛠️ Tecnologias
- Python
- Streamlit
- Git
- GitHub

▶️ Como executar
1. Clone o repositório
git clone https://github.com/hot1v5/Techsmart-Sistema-Especialista.git

2. Entre na pasta
cd Techsmart-Sistema-Especialista

3. Crie um ambiente virtual
Windows:
python -m venv .venv

4. Ative o ambiente virtual
PowerShell:
.\.venv\Scripts\Activate.ps1

5. Instale as dependências
python -m pip install -r requirements.txt

6. Execute a aplicação
python -m streamlit run app.py

Após a execução, o Streamlit disponibilizará um endereço local, normalmente:
http://localhost:8501

🧪 Testes
O sistema foi testado nos seguintes cenários:
- Computador básico
- Trabalho com multitarefa
- Programação profissional
- Jogos pesados
- Edição profissional
- Orçamento insuficiente
- Caso sem conclusão

