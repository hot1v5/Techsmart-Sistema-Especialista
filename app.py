import streamlit as st

from recomendador import (
    motor_inferencia,
    escolher_recomendacao_principal,
    obter_configuracao
)


# Configuração inicial da página
st.set_page_config(
    page_title="TechSmart Informática",
    page_icon="💻",
    layout="wide"
)


# Estilo da aplicação
st.markdown("""
<style>

.stApp {
    background-color: #0b1437;
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.stApp p,
.stApp label,
.stApp li {
    color: white;
}


/* Cabeçalho */

.topo {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
}

.topo h1 {
    color: white;
    margin: 0;
    font-size: 2.4rem;
}

.topo h3 {
    color: #e0e7ff;
    margin-top: 0.5rem;
}

.topo p {
    line-height: 1.5;
}


/* Card usado nas recomendações */

.card {
    background-color: #131c42;
    border: 1px solid #25316b;
    border-radius: 15px;
    padding: 1.2rem;
    margin: 1rem 0;
}


/* Resultado principal */

.destaque {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    border-radius: 18px;
    padding: 2rem;
    margin: 1.5rem 0;
}

.destaque h2 {
    color: white;
    margin: 0;
}


/* Botão */

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 0.8rem;
}

.stButton > button:hover {
    color: white;
}


/* Explicação */

div[data-testid="stExpander"] {
    background-color: #111a3d;
    border: 1px solid #25316b;
    border-radius: 12px;
}


/* Rodapé */

.rodape {
    text-align: center;
    color: #b6c0e8;
    margin-top: 3rem;
    font-size: 0.85rem;
}


/* Ajustes para celular */

@media (max-width: 768px) {

    .block-container {
        padding-left: 0.8rem;
        padding-right: 0.8rem;
        padding-top: 1rem;
    }

    .topo {
        padding: 1.3rem;
        border-radius: 15px;
    }

    .topo h1 {
        font-size: 1.7rem;
    }

    .topo h3 {
        font-size: 1rem;
    }

    .topo p {
        font-size: 0.9rem;
    }

    .destaque {
        padding: 1.3rem;
    }

    .destaque h2 {
        font-size: 1.4rem;
    }

    /* Coloca as colunas uma embaixo da outra */
    div[data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
    }

    div[data-testid="column"] {
        width: 100% !important;
        min-width: 100% !important;
        flex: 1 1 100% !important;
    }

    /* Permite que os radios quebrem linha */
    div[role="radiogroup"] {
        flex-wrap: wrap !important;
    }
}

</style>
""", unsafe_allow_html=True)


# Opções usadas nas perguntas
finalidades = {
    "1": "Estudos",
    "2": "Trabalho",
    "3": "Programação",
    "4": "Jogos",
    "5": "Edição de vídeo"
}

niveis_jogos = {
    "1": "Não jogo",
    "2": "Jogos leves",
    "3": "Jogos intermediários",
    "4": "Jogos pesados"
}

niveis_programacao = {
    "1": "Não programo",
    "2": "Programação básica",
    "3": "Programação profissional"
}

niveis_edicao = {
    "1": "Não edito",
    "2": "Edição básica",
    "3": "Edição profissional"
}

niveis = {
    "1": "Baixa",
    "2": "Média",
    "3": "Alta"
}

resolucoes = {
    "1": "Não se aplica",
    "2": "Full HD",
    "3": "1440p ou superior"
}

desempenhos = {
    "1": "Básico",
    "2": "Intermediário",
    "3": "Alto"
}

sim_nao = {
    "1": "Não",
    "2": "Sim"
}


# Essa função faz o Streamlit mostrar o texto
# no lugar dos números usados internamente
def mostrar(opcoes):
    return lambda valor: opcoes[valor]


# Cabeçalho
st.markdown("""
<div class="topo">
<p>💻 <b>TechSmart Informática</b></p>
<h1>Encontre o computador ideal para você</h1>
<h3>Sistema Especialista de Recomendação de Computadores</h3>
<p>
O sistema analisa seu perfil, suas necessidades e seu orçamento
para indicar uma configuração de computador adequada.
</p>
<p>
As respostas são analisadas através de uma base de regras
e o sistema também explica como chegou à recomendação.
</p>
</div>
""", unsafe_allow_html=True)


# Perfil do cliente
st.subheader("👤 Perfil do Cliente")

col1, col2 = st.columns(2)

with col1:
    orcamento = st.number_input(
        "Orçamento disponível (R$)",
        min_value=0,
        value=3000,
        step=100
    )

with col2:
    finalidade = st.selectbox(
        "Finalidade principal",
        list(finalidades),
        format_func=mostrar(finalidades)
    )


# Uso
st.subheader("🎯 Uso e Finalidade")

col1, col2 = st.columns(2)

with col1:
    jogos = st.selectbox(
        "Você joga?",
        list(niveis_jogos),
        format_func=mostrar(niveis_jogos)
    )

    programacao = st.selectbox(
        "Você programa?",
        list(niveis_programacao),
        format_func=mostrar(niveis_programacao)
    )

with col2:
    edicao = st.selectbox(
        "Você edita vídeos ou imagens?",
        list(niveis_edicao),
        format_func=mostrar(niveis_edicao)
    )

    multitarefa = st.radio(
        "Nível de multitarefa",
        list(niveis),
        format_func=mostrar(niveis),
        horizontal=True
    )


# Necessidades técnicas
st.subheader("⚙️ Necessidades Técnicas")

col1, col2 = st.columns(2)

with col1:
    resolucao = st.selectbox(
        "Resolução de tela",
        list(resolucoes),
        format_func=mostrar(resolucoes)
    )

    armazenamento = st.radio(
        "Necessidade de armazenamento",
        list(niveis),
        format_func=mostrar(niveis),
        horizontal=True
    )

    desempenho = st.radio(
        "Desempenho esperado",
        list(desempenhos),
        format_func=mostrar(desempenhos),
        horizontal=True
    )

with col2:
    maquina_virtual = st.radio(
        "Vai usar máquinas virtuais?",
        list(sim_nao),
        format_func=mostrar(sim_nao),
        horizontal=True
    )

    ferramentas_pesadas = st.radio(
        "Vai usar ferramentas pesadas?",
        list(sim_nao),
        format_func=mostrar(sim_nao),
        horizontal=True
    )

    arquivos_grandes = st.radio(
        "Vai trabalhar com arquivos grandes?",
        list(sim_nao),
        format_func=mostrar(sim_nao),
        horizontal=True
    )


st.write("")

botao = st.button(
    "🔍 Analisar perfil e recomendar computador",
    use_container_width=True
)


# A análise só acontece quando o usuário clica no botão
if botao:

    # Junta as respostas do usuário
    dados_cliente = {
        "orcamento": orcamento,
        "finalidade": finalidade,
        "jogos": jogos,
        "programacao": programacao,
        "edicao": edicao,
        "multitarefa": multitarefa,
        "resolucao": resolucao,
        "armazenamento": armazenamento,
        "desempenho": desempenho,
        "maquina_virtual": maquina_virtual,
        "ferramentas_pesadas": ferramentas_pesadas,
        "arquivos_grandes": arquivos_grandes
    }

    # Envia os dados para o motor de inferência
    recomendacoes, complementares, regras_ativadas = motor_inferencia(
        dados_cliente
    )

    # Evita mostrar recomendações repetidas
    recomendacoes = list(dict.fromkeys(recomendacoes))
    complementares = list(dict.fromkeys(complementares))


    # Caso nenhuma regra principal seja ativada
    if not recomendacoes:

        st.warning(
            "⚠️ Não encontramos uma recomendação para esse perfil. "
            "Tente alterar algumas respostas e faça uma nova análise."
        )


    else:

        # Escolhe a recomendação com maior prioridade
        principal = escolher_recomendacao_principal(
            recomendacoes
        )

        configuracao = obter_configuracao(
            principal
        )


        # Recomendação principal
        st.markdown(
            f"""
<div class="destaque">
<p>RECOMENDAÇÃO PRINCIPAL</p>
<h2>{principal}</h2>
</div>
""",
            unsafe_allow_html=True
        )


        # Configuração indicada
        if configuracao:

            st.subheader("🖥️ Configuração sugerida")

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"**Processador:** "
                    f"{configuracao['Processador']}"
                )

                st.write(
                    f"**Memória RAM:** "
                    f"{configuracao['Memória RAM']}"
                )

                st.write(
                    f"**Armazenamento:** "
                    f"{configuracao['Armazenamento']}"
                )

            with col2:
                st.write(
                    f"**Placa de vídeo:** "
                    f"{configuracao['Placa de vídeo']}"
                )

                st.write(
                    f"**Perfil:** "
                    f"{configuracao['Perfil']}"
                )


        # Recomendações extras
        if complementares:

            lista = "".join(
                f"<li>{item}</li>"
                for item in complementares
            )

            st.markdown(
                f"""
<div class="card">
<b>Recomendações complementares</b>
<ul>
{lista}
</ul>
</div>
""",
                unsafe_allow_html=True
            )


        # Mostra as regras usadas pelo sistema
        with st.expander(
            "🧠 Como o sistema chegou a essa conclusão?",
            expanded=True
        ):

            st.write(
                "Regras ativadas durante a análise:"
            )

            for regra in regras_ativadas:
                st.info(regra)


        # Resumo das respostas
        st.subheader("📋 Resumo dos fatos informados")

        col1, col2 = st.columns(2)

        with col1:
            st.write(
                f"**Orçamento:** R$ {orcamento:,.2f}"
            )

            st.write(
                f"**Finalidade:** {finalidades[finalidade]}"
            )

            st.write(
                f"**Jogos:** {niveis_jogos[jogos]}"
            )

            st.write(
                f"**Programação:** "
                f"{niveis_programacao[programacao]}"
            )

            st.write(
                f"**Edição:** {niveis_edicao[edicao]}"
            )

            st.write(
                f"**Multitarefa:** {niveis[multitarefa]}"
            )

        with col2:
            st.write(
                f"**Resolução:** {resolucoes[resolucao]}"
            )

            st.write(
                f"**Armazenamento:** {niveis[armazenamento]}"
            )

            st.write(
                f"**Desempenho:** {desempenhos[desempenho]}"
            )

            st.write(
                f"**Máquina virtual:** "
                f"{sim_nao[maquina_virtual]}"
            )

            st.write(
                f"**Ferramentas pesadas:** "
                f"{sim_nao[ferramentas_pesadas]}"
            )

            st.write(
                f"**Arquivos grandes:** "
                f"{sim_nao[arquivos_grandes]}"
            )


# Rodapé
st.markdown("""
<div class="rodape">
TechSmart Informática • Sistema Especialista desenvolvido para fins acadêmicos
</div>
""", unsafe_allow_html=True)