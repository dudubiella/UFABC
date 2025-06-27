import pandas as pd
import networkx as nx
import glob
import matplotlib.pyplot as plt
import json
from pathlib import Path

CAMINHO_DADOS = "Q4\\CR\\Dados"
ARQUIVO_HISTORICO = Path(CAMINHO_DADOS) / "nomes_similares.json"

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

def construir_grafo(df):
    G = nx.DiGraph()
    origens_destinos = set()
    for _, row in df.iterrows():
        origem, destino = extrair_origem_destino(row['Linha'])
        if origem and destino:
            G.add_edge(origem, destino)
            origens_destinos.update([origem, destino])
    return G, list(origens_destinos)

def desenhar_grafo(G):
    plt.figure(figsize=(14,10))
    pos = nx.spring_layout(G, seed=42, k=0.8)
    labels = {n: str(i+1) for i, n in enumerate(G.nodes)}
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=12, edge_color='gray')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
    plt.title("Exemplo de Grafo Direcionado das Linhas de Ônibus")
    plt.axis('off')
    plt.show()

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

def main():
    df_total = carregar_dados()
    df_amostra = df_total.head(100)
    G, nomes = construir_grafo(df_amostra)
    desenhar_grafo(G)
    historico = carregar_historico()
    agrupamentos, ignorados, historico = verificar_nomes_similares_interativo(nomes, historico)
    salvar_historico(historico)
    print("\nFinalizado.\n")
    print(f"Resumo do grafo:")
    print(f"Total de nós: {G.number_of_nodes()}")
    print(f"Total de arestas: {G.number_of_edges()}")
    labels = {str(i+1): n for i, n in enumerate(G.nodes)}
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