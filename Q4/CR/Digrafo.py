import pandas as pd
import networkx as nx
import glob
import matplotlib.pyplot as plt
import json
from pathlib import Path

# Caminhos fixos do projeto
CAMINHO_DADOS = "Q4\\CR\\Dados"
ARQUIVO_HISTORICO = Path(CAMINHO_DADOS) / "nomes_similares.json"

# -------- Carregamento e Construção do Grafo --------

def carregar_dados():
    arquivos_xls = glob.glob(f"{CAMINHO_DADOS}/*.xls")
    dfs = []
    for arquivo in arquivos_xls:
        print(f"Lendo: {arquivo}")
        df = pd.read_excel(arquivo, skiprows=2)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

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

# -------- Filtro --------

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

    return {
        "grau_entrada_ponderado": grau_entrada_ponderado,
        "grau_saida_ponderado": grau_saida_ponderado,
        "pagerank": pagerank,
        "densidade": densidade,
        "diametro": diametro,
        "caminho_diametro": caminho_diametro
    }

# -------- Visualização --------

def desenhar_grafo(G, grau_minimo=None):
    plt.figure(figsize=(14,10))
    pos = nx.spring_layout(G)
    labels = {n: str(i+1) for i, n in enumerate(G.nodes)}

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
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

# -------- Histórico e verificação interativa --------

def carregar_historico():
    if ARQUIVO_HISTORICO.exists():
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_historico(historico):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)

def verificar_nomes_similares_interativo(nomes, historico):
    agrupamentos = {}
    ignorados = set()
    for i in range(len(nomes)):
        for j in range(i+1, len(nomes)):
            nome1 = nomes[i].strip().upper()
            nome2 = nomes[j].strip().upper()
            par = tuple(sorted([nome1, nome2]))
            if str(par) in historico and historico[str(par)] in ("s","n"):
                continue
            if nome1 in nome2 or nome2 in nome1:
                print(f"\nPossível duplicata:")
                print(f"1: {nome1}")
                print(f"2: {nome2}")
                print("Eles representam o mesmo ponto?")
                print("[s] Sim    [n] Não    [x] Não sei")
                resp = input("Sua resposta: ").strip().lower()
                if resp not in {"s","n","x"}:
                    print("Resposta inválida recebida. Encerrando a verificação sem salvar alterações.")
                    return agrupamentos, ignorados, historico
                if resp == "s":
                    historico[str(par)] = "s"
                    agrupamentos.setdefault(nome1, []).append(nome2)
                elif resp == "n":
                    historico[str(par)] = "n"
                    ignorados.add(par)
                else:
                    print("Entendido. Esse par será perguntado novamente na próxima execução.")
    return agrupamentos, ignorados, historico

# -------- Entrada do Grau Mínimo --------

def solicitar_grau_minimo():
    print("\nDeseja visualizar o grafo completo ou aplicar um filtro por grau mínimo?")
    print("[1] Visualizar grafo completo")
    print("[2] Definir grau mínimo para filtrar nós")

    escolha = input("Escolha uma opção [1/2]: ").strip()

    if escolha == "1":
        return None  # Nenhum filtro aplicado
    elif escolha == "2":
        while True:
            try:
                grau_minimo = int(input("Digite o grau mínimo desejado (número inteiro >= 2): ").strip())
                if grau_minimo >= 2:
                    return grau_minimo
                else:
                    print("Por favor, insira um número inteiro maior ou igual a 2.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    else:
        print("Opção inválida. Considerando grafo completo.")
        return None

# -------- Função principal --------

def main():
    df_total = carregar_dados()
    G = construir_grafo(df_total)

    grau_minimo = solicitar_grau_minimo()

    if grau_minimo is None:
        G_analisado = G
        print(f"\nAnalisando o grafo completo com {len(G.nodes())} nós.")
    else:
        G_analisado = filtrar_grafo_por_grau(G, grau_minimo)

    desenhar_grafo(G_analisado, grau_minimo=grau_minimo)
    metricas = calcular_metricas(G_analisado)

    print(f"\nDensidade do grafo: {metricas['densidade']:.6f}")

    if metricas["diametro"] is not None:
        print(f"\nDiâmetro do grafo direcionado (número máximo de baldeações): {metricas['diametro']}")
        caminho_formatado = " -> ".join(metricas["caminho_diametro"])
        print(f"Caminho do diâmetro ({metricas['diametro']} arestas):\n{caminho_formatado}")
    else:
        print("Diâmetro não foi calculado.")

    print("\nGrau de Entrada Ponderado (exemplo das 5 maiores estações):")
    for no, val in sorted(metricas["grau_entrada_ponderado"].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f" - {no}: {val:.2f}")

    print("\nGrau de Saída Ponderado (exemplo das 5 maiores estações):")
    for no, val in sorted(metricas["grau_saida_ponderado"].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f" - {no}: {val:.2f}")

    print("\nCentralidade PageRank (exemplo das 5 maiores estações):")
    for no, val in sorted(metricas["pagerank"].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f" - {no}: {val:.4f}")

    historico = carregar_historico()
    agrupamentos, ignorados, historico = verificar_nomes_similares_interativo(list(G_analisado.nodes), historico)
    salvar_historico(historico)

    print("\nFinalizado.\n")

    labels = {str(i+1): n for i, n in enumerate(G_analisado.nodes)}
    while True:
        entrada = input("\nDigite o número do nó para saber o nome da estação (ou 'sair' para encerrar): ").strip()
        if entrada.lower() == "sair":
            print("Encerrando o programa.")
            break
        if entrada not in labels:
            print("Entrada inválida. Encerrando o programa.")
            break
        print(f"Nó {entrada} corresponde à estação: {labels[entrada]}")

if __name__ == "__main__":
    main()