import os

import pandas as pd
import matplotlib.pyplot as plt


RESULTADOS = "./resultados.csv"
RODADAS = "./gini_stake_rodadas.csv"

PASTA = "graficos_gini"
os.makedirs(PASTA, exist_ok=True)


# ============================================================
# LEITURA
# ============================================================

res = pd.read_csv(RESULTADOS)
rod = pd.read_csv(RODADAS)


# ============================================================
# 1) GINI FINAL x REINVESTIMENTO
# ============================================================

g = (
    res.groupby(["reinveste_recompensa"])
    .agg(
        media=("media", "mean"),
        ic95=("ic95", "mean")
    )
    .reset_index()
)

plt.figure(figsize=(7,5))
plt.errorbar(
    g["reinveste_recompensa"],
    g["media"],
    yerr=g["ic95"],
    marker="o",
    capsize=5
)

plt.xlabel("Reinvestimento da recompensa")
plt.ylabel("Gini final")
plt.title("Gini final × Reinvestimento")
plt.grid(True)

plt.savefig(
    f"{PASTA}/gini_final_reinvestimento.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ============================================================
# 2) GINI FINAL x PARETO
# ============================================================

g = (
    res.groupby(["parametro_dist"])
    .agg(
        media=("media","mean"),
        ic95=("ic95","mean")
    )
    .reset_index()
)

plt.figure(figsize=(7,5))
plt.errorbar(
    g["parametro_dist"],
    g["media"],
    yerr=g["ic95"],
    marker="o",
    capsize=5
)

plt.xlabel("Parâmetro de Pareto")
plt.ylabel("Gini final")
plt.title("Gini final × Parâmetro de Pareto")
plt.grid(True)

plt.savefig(
    f"{PASTA}/gini_final_pareto.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ============================================================
# 3) GINI FINAL x NÚMERO DE HOLDERS
# ============================================================

g = (
    res.groupby(["n_holders"])
    .agg(
        media=("media","mean"),
        ic95=("ic95","mean")
    )
    .reset_index()
)

plt.figure(figsize=(7,5))
plt.errorbar(
    g["n_holders"],
    g["media"],
    yerr=g["ic95"],
    marker="o",
    capsize=5
)

plt.xlabel("Número de holders")
plt.ylabel("Gini final")
plt.title("Gini final × Número de holders")
plt.grid(True)

plt.savefig(
    f"{PASTA}/gini_final_holders.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ============================================================
# 4) EVOLUÇÃO DO GINI NAS RODADAS (uma linha para cada reinvestimento)
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(rod["reinveste_recompensa"].unique()):

    dados = (
        rod[rod["reinveste_recompensa"] == r]
        .groupby("rodada")["gini"]
        .mean()
        .reset_index()
    )

    plt.plot(
        dados["rodada"],
        dados["gini"],
        marker="o",
        label=f"reinv={r}"
    )

plt.xlabel("Rodada")
plt.ylabel("Gini")
plt.title("Evolução do Gini por reinvestimento")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_rodadas_reinvestimento.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ============================================================
# 5) EVOLUÇÃO DO GINI POR PARETO
# ============================================================

plt.figure(figsize=(8,5))

for p in sorted(rod["parametro_dist"].unique()):

    dados = (
        rod[rod["parametro_dist"] == p]
        .groupby("rodada")["gini"]
        .mean()
        .reset_index()
    )

    plt.plot(
        dados["rodada"],
        dados["gini"],
        marker="o",
        label=f"Pareto={p}"
    )

plt.xlabel("Rodada")
plt.ylabel("Gini")
plt.title("Evolução do Gini por parâmetro de Pareto")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_rodadas_pareto.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ============================================================
# 6) EVOLUÇÃO DO GINI POR NÚMERO DE HOLDERS
# ============================================================

plt.figure(figsize=(8,5))

for h in sorted(rod["n_holders"].unique()):

    dados = (
        rod[rod["n_holders"] == h]
        .groupby("rodada")["gini"]
        .mean()
        .reset_index()
    )

    plt.plot(
        dados["rodada"],
        dados["gini"],
        marker="o",
        label=f"{h} holders"
    )

plt.xlabel("Rodada")
plt.ylabel("Gini")
plt.title("Evolução do Gini por número de holders")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_rodadas_holders.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("Gráficos gerados com sucesso!")