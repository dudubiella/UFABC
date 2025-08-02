import pandas as pd
import networkx as nx
import glob
import matplotlib.pyplot as plt
import json
from pathlib import Path
from community import community_louvain
import numpy as np
import matplotlib.colors as mcolors

# -------- Configurações e caminhos --------

CAMINHO_DADOS = "Q4\\CR\\Dados"
ARQUIVO_TERMINAIS_UNIFICADOS = Path(CAMINHO_DADOS) / "terminais_unificados.json"
ARQUIVO_REGIOES = Path(CAMINHO_DADOS) / "regioes_estacoes.json"

# -------- Carregamento de dados --------

def carregar_dados():
    arquivos_xls = glob.glob(f"{CAMINHO_DADOS}/*.xls")
    dfs = []
    for arquivo in arquivos_xls:
        print(f"Lendo: {arquivo}")
        df = pd.read_excel(arquivo, skiprows=2)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def carregar_terminais_unificados():
    if ARQUIVO_TERMINAIS_UNIFICADOS.exists():
        with open(ARQUIVO_TERMINAIS_UNIFICADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print(f"Aviso: arquivo {ARQUIVO_TERMINAIS_UNIFICADOS} não encontrado.")
        return {}

# -------- Construção do grafo --------

def extrair_origem_destino(linha_str):
    if not isinstance(linha_str, str):
        return None, None
    if " - " in linha_str:
        rota = linha_str.split(" - ", 1)[1]
    else:
        rota = linha_str
    if "/" in rota:
        origem, destino = rota.split("/", 1)
    else:
        return rota.strip().upper(), None
    return origem.strip().upper(), destino.strip().upper()

def construir_grafo(df, peso_coluna='Tot Passageiros Transportados'):
    G = nx.DiGraph()
    df_local = df.copy()
    df_local[peso_coluna] = pd.to_numeric(df_local[peso_coluna], errors='coerce').fillna(0)

    for _, row in df_local.iterrows():
        origem, destino = extrair_origem_destino(row['Linha'])
        peso = row[peso_coluna]

        if origem and destino:
            if G.has_edge(origem, destino):
                G[origem][destino]['weight'] += peso
            else:
                G.add_edge(origem, destino, weight=peso)

    return G

def construir_grafo_filtrado(G_original, mapeamento_duplicados):
    G_novo = nx.DiGraph()

    for u, v, data in G_original.edges(data=True):
        u_mapeado = mapeamento_duplicados.get(u, u)
        v_mapeado = mapeamento_duplicados.get(v, v)

        if G_novo.has_edge(u_mapeado, v_mapeado):
            G_novo[u_mapeado][v_mapeado]['weight'] += data.get('weight', 0)
        else:
            G_novo.add_edge(u_mapeado, v_mapeado, weight=data.get('weight', 0))

    return G_novo

# -------- Filtros --------

def filtrar_grafo_por_grau(G, grau_minimo):
    graus_entrada = dict(G.in_degree())
    graus_saida = dict(G.out_degree())
    grau_total = {no: graus_entrada.get(no, 0) + graus_saida.get(no, 0) for no in G.nodes()}

    nos_filtrados = [no for no in G.nodes() if grau_total[no] >= grau_minimo]

    print(f"\nTotal de nós antes do filtro: {len(G.nodes())}")
    print(f"Total de nós após o filtro (grau >= {grau_minimo}): {len(nos_filtrados)}")

    return G.subgraph(nos_filtrados).copy()

# -------- Cálculo das Métricas --------

def calcular_grau_ponderado(G):
    grau_entrada_ponderado = {}
    grau_saida_ponderado = {}

    for no in G.nodes():
        in_edges = G.in_edges(no, data=True)
        out_edges = G.out_edges(no, data=True)
        grau_entrada_ponderado[no] = sum(d.get('weight', 0) for _, _, d in in_edges)
        grau_saida_ponderado[no] = sum(d.get('weight', 0) for _, _, d in out_edges)

    return grau_entrada_ponderado, grau_saida_ponderado

def calcular_pagerank(G):
    return nx.pagerank(G, weight='weight')

def calcular_densidade(G):
    return nx.density(G)

def calcular_diametro_direcionado(G):
    if not nx.is_strongly_connected(G):
        componentes = list(nx.strongly_connected_components(G))
        maior_componente = max(componentes, key=len)
        G_sub = G.subgraph(maior_componente).copy()
        print(f"\nGrafo não fortemente conexo: analisando maior componente com {len(G_sub.nodes())} nós.")
    else:
        G_sub = G

    all_shortest_paths = dict(nx.all_pairs_shortest_path(G_sub))

    diametro = 0
    caminho_diametro = []

    for origem, caminhos in all_shortest_paths.items():
        for destino, caminho in caminhos.items():
            comprimento = len(caminho) - 1
            if comprimento > diametro:
                diametro = comprimento
                caminho_diametro = caminho

    return diametro, caminho_diametro

def calcular_metricas(G):
    print("\nCalculando métricas de centralidade...")

    grau_entrada_ponderado, grau_saida_ponderado = calcular_grau_ponderado(G)

    try:
        pagerank = calcular_pagerank(G)
    except Exception as e:
        print(f"Erro ao calcular PageRank: {e}")
        pagerank = {}

    densidade = calcular_densidade(G)
    diametro, caminho_diametro = calcular_diametro_direcionado(G)

    print("\nCalculando outras centralidades...")

    centralidade_grau = nx.degree_centrality(G)
    centralidade_intermediacao = nx.betweenness_centrality(G)
    centralidade_proximidade = nx.closeness_centrality(G)
    try:
        if nx.is_connected(G.to_undirected()):
            centralidade_autovetor = nx.eigenvector_centrality(G.to_undirected(), max_iter=1000)
        else:
            centralidade_autovetor = {}
            print("Grafo desconectado: autovetor não calculado.")
    except Exception as e:
        centralidade_autovetor = {}
        print(f"Erro ao calcular centralidade de autovetor: {e}")

    return {
        "grau_entrada_ponderado": grau_entrada_ponderado,
        "grau_saida_ponderado": grau_saida_ponderado,
        "pagerank": pagerank,
        "densidade": densidade,
        "diametro": diametro,
        "caminho_diametro": caminho_diametro,
        "grau": centralidade_grau,
        "intermediacao": centralidade_intermediacao,
        "proximidade": centralidade_proximidade,
        "autovetor": centralidade_autovetor
    }

def analisar_mundo_pequeno(G):
    G_und = G.to_undirected()
    if not nx.is_connected(G_und):
        maior_cc = max(nx.connected_components(G_und), key=len)
        G_und = G_und.subgraph(maior_cc)
        print(f"\nGrafo desconectado. Usando maior componente com {len(G_und)} nós.")

    clustering = nx.average_clustering(G_und)
    path_length = nx.average_shortest_path_length(G_und)

    print("\n--- Mundo Pequeno ---")
    print(f"Coeficiente de Clusterização Médio: {clustering:.4f}")
    print(f"Caminho Médio entre Nós: {path_length:.4f}")

def plotar_distribuicao_grau(G):
    graus = [G.degree(n) for n in G.nodes()]
    plt.figure(figsize=(8,5))
    plt.hist(graus, bins=30, color="cornflowerblue")
    plt.title("Distribuição de Grau")
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8,5))
    grau_series = pd.Series(graus).value_counts().sort_index()
    plt.loglog(grau_series.index, grau_series.values, 'o', color='darkred')
    plt.title("Distribuição de Grau (Escala Log-Log)")
    plt.xlabel("Grau (k)")
    plt.ylabel("P(k)")
    plt.grid(True)
    plt.show()

def calcular_assortatividade(G):
    G_und = G.to_undirected()
    r = nx.degree_assortativity_coefficient(G_und)
    print(f"\n--- Assortatividade ---")
    print(f"Coeficiente de Assortatividade: {r:.4f}")
    if r < 0:
        print("A rede é dissortativa (hubs se conectam a pontos periféricos).")
    elif r > 0:
        print("A rede é assortativa (hubs se conectam com hubs).")
    else:
        print("A rede não apresenta tendência de assortatividade.")

def detectar_comunidades(G):
    G_und = G.to_undirected()
    particao = community_louvain.best_partition(G_und)
    num_comunidades = max(particao.values()) + 1

    print(f"\n--- Comunidades (Louvain) ---")
    print(f"Número de comunidades encontradas: {num_comunidades}")

    pos = nx.spring_layout(G_und, seed=42)

    cmap = plt.colormaps.get_cmap("tab20")
    cores = [cmap(particao[n] % cmap.N) for n in G_und.nodes()]

    plt.figure(figsize=(12,8))
    nx.draw_networkx_nodes(G_und, pos, node_color=cores, node_size=100)
    nx.draw_networkx_edges(G_und, pos, alpha=0.4)
    plt.title("Comunidades Detectadas (Louvain)")
    plt.axis("off")
    plt.show()

def analisar_robustez(G, proporcao=0.1):
    G_und = G.to_undirected()
    n_remover = int(len(G_und.nodes()) * proporcao)

    # Falha aleatória
    aleatorios = list(G_und.nodes())
    np.random.shuffle(aleatorios)

    comp_random = []
    G_temp = G_und.copy()
    for i in range(n_remover):
        G_temp.remove_node(aleatorios[i])
        if G_temp.number_of_nodes() > 0:
            maior = max(nx.connected_components(G_temp), key=len)
            comp_random.append(len(maior))
        else:
            comp_random.append(0)

    # Ataque dirigido
    por_grau = sorted(G_und.degree, key=lambda x: x[1], reverse=True)
    hubs = [n for n, _ in por_grau]
    comp_dirigido = []
    G_temp = G_und.copy()
    for i in range(n_remover):
        G_temp.remove_node(hubs[i])
        if G_temp.number_of_nodes() > 0:
            maior = max(nx.connected_components(G_temp), key=len)
            comp_dirigido.append(len(maior))
        else:
            comp_dirigido.append(0)

    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(range(n_remover), comp_random, label="Falha Aleatória")
    plt.plot(range(n_remover), comp_dirigido, label="Ataque Direcionado (Hubs)")
    plt.xlabel("Nós Removidos")
    plt.ylabel("Tamanho do Maior Componente")
    plt.title("Robustez da Rede")
    plt.legend()
    plt.grid(True)
    plt.show()

# -------- Visualização --------

def desenhar_grafo(G, grau_minimo=None):
    plt.figure(figsize=(14,10))
    pos = nx.spring_layout(G, seed=42)  # Para consistência na disposição dos nós

    # Dicionário de cores para regiões (adicione conforme suas regiões reais)
    cores_regiao = {
        "Zona Leste": "orange",
        "Centro": "green",
        "Zona Oeste": "purple",
        "Zona Norte": "blue",
        "Zona Sul": "red"
    }

    # Para cada nó, pegar a cor da sua região
    node_colors = []
    for n in G.nodes:
        regiao = G.nodes[n].get("regiao", None)
        if regiao is None:
            cor = "lightgray"  # cor padrão para nós sem região
        else:
            cor = cores_regiao.get(regiao, "lightgray")  # se a região não está no dicionário, padrão
        node_colors.append(cor)

    labels = {n: str(i+1) for i, n in enumerate(G.nodes)}

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=12, edge_color='gray')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    titulo = "Grafo Direcionado das Linhas de Ônibus (Pesos = Passageiros)"
    if grau_minimo is not None:
        titulo += f" | Grau mínimo: {grau_minimo}"
    plt.title(titulo)
    plt.axis('off')
    plt.show()

# -------- Carregamento de terminais unificados com região --------

def carregar_terminais_unificados():
    if ARQUIVO_TERMINAIS_UNIFICADOS.exists():
        with open(ARQUIVO_TERMINAIS_UNIFICADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print(f"Aviso: arquivo {ARQUIVO_TERMINAIS_UNIFICADOS} não encontrado.")
        return {}

# -------- Construção do mapeamento duplicados --------

def atualizar_terminais_unificados(G, terminais_unificados):
    # Conjunto de todos os nomes já registrados (principais e pseudônimos)
    todos_os_nomes = set()
    for principal, info in terminais_unificados.items():
        todos_os_nomes.add(principal)
        if isinstance(info, dict):
            todos_os_nomes.update(info.get("pseudonimos", []))

    novas_estacoes = []

    for estacao in G.nodes:
        if estacao in todos_os_nomes:
            continue  # já está presente, como principal ou pseudônimo

        # Não adicionar como terminal principal se já é pseudônimo de alguém
        ja_e_pseudonimo = False
        for info in terminais_unificados.values():
            if isinstance(info, dict) and estacao in info.get("pseudonimos", []):
                ja_e_pseudonimo = True
                break
        if ja_e_pseudonimo:
            continue  # já está como pseudônimo, não adicionar novamente

        # Adiciona novo terminal com região indefinida e sem pseudônimos
        terminais_unificados[estacao] = {"pseudonimos": [], "regiao": None}
        novas_estacoes.append(estacao)

    if novas_estacoes:
        print(f"Arquivo {ARQUIVO_TERMINAIS_UNIFICADOS.name} atualizado com {len(novas_estacoes)} novas estações.")
        salvar_terminais_unificados(terminais_unificados)

def construir_mapeamento_duplicados(terminais_unificados):
    mapeamento = {}
    for principal, info in terminais_unificados.items():
        mapeamento[principal] = principal
        for pseudo in info.get("pseudonimos", []):
            mapeamento[pseudo] = principal
    return mapeamento

# -------- Obter região da estação (busca direta nos terminais unificados) --------

def obter_regiao_estacao(estacao, terminais_unificados):
    # Se for terminal principal
    if estacao in terminais_unificados:
        return terminais_unificados[estacao].get("regiao", None)
    # Se for pseudônimo, retorna a região do terminal principal
    for principal, info in terminais_unificados.items():
        if estacao in info.get("pseudonimos", []):
            return info.get("regiao", None)
    return None

# -------- Classificação interativa atualizada para alterar a região dos terminais unificados --------

def salvar_terminais_unificados(terminais_unificados):
    # Cria uma cópia limpa antes de salvar
    copia = {}

    # Conjunto de todos os pseudônimos já registrados
    todos_pseudonimos = set()
    for info in terminais_unificados.values():
        if isinstance(info, dict):
            pseudos = info.get("pseudonimos", [])
            todos_pseudonimos.update(pseudos)

    for terminal, info in terminais_unificados.items():
        if terminal in todos_pseudonimos:
            print(f"[Aviso] Ignorando '{terminal}' porque já está como pseudônimo de outro terminal.")
            continue  # não adiciona esse terminal principal pois é pseudônimo
        copia[terminal] = info

    with open(ARQUIVO_TERMINAIS_UNIFICADOS, "w", encoding="utf-8") as f:
        json.dump(copia, f, indent=2, ensure_ascii=False)

# -------- Função principal --------

def main():
    df_total = carregar_dados()

    terminais_unificados = carregar_terminais_unificados()

    # Carrega e constrói grafo bruto para descobrir estações faltantes
    G = construir_grafo(df_total)
    
    # Atualiza terminais_unificados com estações ainda não mapeadas
    atualizar_terminais_unificados(G, terminais_unificados)

    mapeamento_duplicados = construir_mapeamento_duplicados(terminais_unificados)

    G_filtrado = construir_grafo_filtrado(G, mapeamento_duplicados)

    # Atribuir a região como atributo de cada nó no grafo filtrado
    for estacao in G_filtrado.nodes:
        regiao = obter_regiao_estacao(estacao, terminais_unificados)
        G_filtrado.nodes[estacao]["regiao"] = regiao

    G_analisado = G_filtrado  # Sem filtro por grau mínimo
    print(f"\nAnalisando o grafo filtrado completo com {len(G_analisado.nodes())} nós.")

    desenhar_grafo(G_analisado)

    metricas = calcular_metricas(G_analisado)

    print(f"\nDensidade do grafo: {metricas['densidade']:.6f}")

    if metricas["diametro"] is not None:
        print(f"\nDiâmetro do grafo direcionado (número máximo de baldeações): {metricas['diametro']}")
        caminho_formatado = " -> ".join(metricas["caminho_diametro"])
        print(f"Caminho do diâmetro ({metricas['diametro']} arestas):\n{caminho_formatado}")
    else:
        print("Diâmetro não foi calculado.")

    print("\nGrau de Entrada Ponderado (exemplo das 10 maiores estações):")
    for no, val in sorted(metricas["grau_entrada_ponderado"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f" - {no}: {val:.2f}")

    print("\nGrau de Saída Ponderado (exemplo das 10 maiores estações):")
    for no, val in sorted(metricas["grau_saida_ponderado"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f" - {no}: {val:.2f}")

    print("\nCentralidade PageRank (exemplo das 10 maiores estações):")
    for no, val in sorted(metricas["pagerank"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f" - {no}: {val:.4f}")
    
    print("\nCentralidade de Grau (Top 10):")
    for no, val in sorted(metricas["grau"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f" - {no}: {val:.4f}")

    print("\nCentralidade de Intermediação (Top 10):")
    for no, val in sorted(metricas["intermediacao"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f" - {no}: {val:.4f}")

    print("\nCentralidade de Proximidade (Top 10):")
    for no, val in sorted(metricas["proximidade"].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f" - {no}: {val:.4f}")

    if metricas["autovetor"]:
        print("\nCentralidade de Autovetor (Top 10):")
        for no, val in sorted(metricas["autovetor"].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f" - {no}: {val:.4f}")

    analisar_mundo_pequeno(G_analisado)
    plotar_distribuicao_grau(G_analisado)
    calcular_assortatividade(G_analisado)
    detectar_comunidades(G_analisado)
    analisar_robustez(G_analisado, proporcao=0.1)

    print("\nAnálise finalizada.\n")

if __name__ == "__main__":
    main()