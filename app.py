import streamlit as st

from recomendador import (
    motor_inferencia,
    escolher_recomendacao_principal
)

st.set_page_config(page_title="TechSmart Informática", page_icon="💻", layout="wide")

# CSS da página
st.markdown("""
<style>
.stApp { background-color: #0b1437; color: white; }
.block-container { max-width: 1000px; padding-top: 2rem; }
#MainMenu, footer, header { visibility: hidden; }
.stApp p, .stApp label, .stApp span, .stApp li { color: white; }

.topo {
    background: linear-gradient(135deg, #1d4ed8, #7c3aed);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}
.topo h1 { color: white; margin: 0; font-size: 2.3rem; }
.topo h3 { color: #e0e7ff; margin: 0.3rem 0 1rem 0; }

.card {
    background-color: #131c42;
    border: 1px solid #25316b;
    border-radius: 16px;
    padding: 1.2rem;
    margin-bottom: 1rem;
}
.destaque {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
}
.destaque h2 { color: white; margin: 0; }
.regra {
    background-color: #0e1740;
    border-left: 4px solid #7c3aed;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    margin-bottom: 0.5rem;
}
.rodape { text-align: center; color: #b6c0e8; margin-top: 2rem; font-size: 0.85rem; }

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-size: 1.1rem;
    font-weight: bold;
    border: none;
    border-radius: 14px;
    padding: 0.8rem;
}

@media (max-width: 768px) {
    .topo h1 { font-size: 1.6rem; }
}
</style>
""", unsafe_allow_html=True)

# Opções das perguntas (o valor interno é o número que o motor espera)
finalidades = {"1": "Estudos", "2": "Trabalho", "3": "Programação", "4": "Jogos", "5": "Edição de vídeo"}
niveis_jogos = {"1": "Não jogo", "2": "Jogos leves", "3": "Jogos intermediários", "4": "Jogos pesados"}
niveis_programacao = {"1": "Não programo", "2": "Programação básica", "3": "Programação profissional"}
niveis_edicao = {"1": "Não edito", "2": "Edição básica", "3": "Edição profissional"}
niveis = {"1": "Baixa", "2": "Média", "3": "Alta"}
resolucoes = {"1": "Não se aplica", "2": "Full HD", "3": "1440p ou superior"}
desempenhos = {"1": "Básico", "2": "Intermediário", "3": "Alto"}
sim_nao = {"1": "Não", "2": "Sim"}


def mostrar(opcoes):
    # usada no format_func para exibir o texto em vez do número
    return lambda chave: opcoes[chave]


# Cabeçalho
st.markdown("""
<div class="topo">
    <p>💻 TechSmart Informática</p>
    <h1>Encontre o computador ideal para você</h1>
    <h3>Sistema Especialista de Recomendação de Computadores</h3>
    <p>Nosso sistema especialista analisa seu perfil, necessidades e orçamento
    utilizando uma base de conhecimento composta por regras de recomendação.</p>
    <p>Você responde às perguntas, o sistema aplica as regras e mostra a
    recomendação junto com a explicação do raciocínio.</p>
</div>
""", unsafe_allow_html=True)

# Seção 1
st.subheader("Perfil do Cliente")
col1, col2 = st.columns(2)
with col1:
    orcamento = st.number_input("Orçamento disponível (R$)", min_value=0, value=3000, step=100)
with col2:
    finalidade = st.selectbox("Finalidade principal", list(finalidades), format_func=mostrar(finalidades))

# Seção 2
st.subheader("Uso e Finalidade")
col1, col2 = st.columns(2)
with col1:
    jogos = st.selectbox("Você joga?", list(niveis_jogos), format_func=mostrar(niveis_jogos))
    programacao = st.selectbox("Você programa?", list(niveis_programacao), format_func=mostrar(niveis_programacao))
with col2:
    edicao = st.selectbox("Você edita vídeos ou imagens?", list(niveis_edicao), format_func=mostrar(niveis_edicao))
    multitarefa = st.radio("Nível de multitarefa", list(niveis), format_func=mostrar(niveis), horizontal=True)

# Seção 3
st.subheader("Necessidades Técnicas")
col1, col2 = st.columns(2)
with col1:
    resolucao = st.selectbox("Resolução de tela", list(resolucoes), format_func=mostrar(resolucoes))
    armazenamento = st.radio("Necessidade de armazenamento", list(niveis), format_func=mostrar(niveis), horizontal=True)
    desempenho = st.radio("Desempenho esperado", list(desempenhos), format_func=mostrar(desempenhos), horizontal=True)
with col2:
    maquina_virtual = st.radio("Vai usar máquinas virtuais?", list(sim_nao), format_func=mostrar(sim_nao), horizontal=True)
    ferramentas_pesadas = st.radio("Vai usar ferramentas pesadas?", list(sim_nao), format_func=mostrar(sim_nao), horizontal=True)
    arquivos_grandes = st.radio("Vai trabalhar com arquivos grandes?", list(sim_nao), format_func=mostrar(sim_nao), horizontal=True)

st.write("")
botao = st.button("Analisar perfil e recomendar computador")

if botao:
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

    # Atenção: ajustar esta linha se o motor devolver os dados em outra ordem
    recomendacoes_principais, complementares, regras_ativadas = motor_inferencia(dados_cliente)

    # remove repetidas mantendo a ordem
    recomendacoes_principais = list(dict.fromkeys(recomendacoes_principais))

    if len(recomendacoes_principais) == 0:
        st.markdown("""
        <div class="card">
            <b>Não encontramos uma recomendação para esse perfil.</b><br>
            Tente alterar algumas respostas, como orçamento ou desempenho, e analise novamente.
        </div>
        """, unsafe_allow_html=True)
    else:
        principal = escolher_recomendacao_principal(recomendacoes_principais)

        st.markdown(f"""
        <div class="destaque">
            <p>RECOMENDAÇÃO PRINCIPAL</p>
            <h2>{principal}</h2>
        </div>
        """, unsafe_allow_html=True)

        if complementares:
            itens = "".join(f"<li>{item}</li>" for item in complementares)
            st.markdown(f"""
            <div class="card">
                <b>CONFIGURAÇÃO / RECOMENDAÇÕES COMPLEMENTARES</b>
                <ul>{itens}</ul>
            </div>
            """, unsafe_allow_html=True)

        with st.expander("Como o sistema chegou a essa conclusão?"):
            for regra in regras_ativadas:
                st.markdown(f"<div class='regra'>{regra}</div>", unsafe_allow_html=True)

    # Resumo do que o usuário informou
    st.subheader("Resumo dos fatos informados")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Orçamento:** R$ {orcamento}")
        st.write(f"**Finalidade:** {finalidades[finalidade]}")
        st.write(f"**Jogos:** {niveis_jogos[jogos]}")
        st.write(f"**Programação:** {niveis_programacao[programacao]}")
        st.write(f"**Edição:** {niveis_edicao[edicao]}")
        st.write(f"**Multitarefa:** {niveis[multitarefa]}")
    with col2:
        st.write(f"**Resolução:** {resolucoes[resolucao]}")
        st.write(f"**Armazenamento:** {niveis[armazenamento]}")
        st.write(f"**Desempenho:** {desempenhos[desempenho]}")
        st.write(f"**Máquina virtual:** {sim_nao[maquina_virtual]}")
        st.write(f"**Ferramentas pesadas:** {sim_nao[ferramentas_pesadas]}")
        st.write(f"**Arquivos grandes:** {sim_nao[arquivos_grandes]}")

st.markdown(
    "<div class='rodape'>TechSmart Informática • Sistema Especialista desenvolvido para fins acadêmicos</div>",
    unsafe_allow_html=True
)