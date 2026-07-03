import os
import pandas as pd
import matplotlib.pyplot as plt

RODADAS = "./gini_stake_rodadas.csv"

PASTA = "./graficos/gini"
os.makedirs(PASTA, exist_ok=True)

# ============================================================
# LEITURA
# ============================================================

rod = pd.read_csv(RODADAS)

# ============================================================
# 1) GINI POR RODADA x REINVESTIMENTO
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(rod["n_rodadas"].unique()):

    dados = (
        rod[rod["n_rodadas"] == r]
        .groupby(["reinveste_recompensa","rodada"])
        .agg(
            media=("gini","mean"),
            ic95=("gini","sem")
        )
        .reset_index()
    )

    dados = (
        dados.groupby("reinveste_recompensa")
        .last()
        .reset_index()
    )

    plt.errorbar(
        dados["reinveste_recompensa"],
        dados["media"],
        yerr=1.96*dados["ic95"],
        marker="o",
        capsize=5,
        label=f"Rodadas={r}"
    )

plt.xlabel("Reinvestimento da recompensa")
plt.ylabel("Gini (última rodada)")
plt.title("Gini × Reinvestimento das recompensas")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_reinvestimento.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 2) GINI x PARETO
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(rod["n_rodadas"].unique()):

    dados = (
        rod[rod["n_rodadas"] == r]
        .groupby(["parametro_dist","rodada"])
        .agg(
            media=("gini","mean"),
            ic95=("gini","sem")
        )
        .reset_index()
    )

    dados = (
        dados.groupby("parametro_dist")
        .last()
        .reset_index()
    )

    plt.errorbar(
        dados["parametro_dist"],
        dados["media"],
        yerr=1.96*dados["ic95"],
        marker="o",
        capsize=5,
        label=f"Rodadas={r}"
    )

plt.xlabel("Parâmetro de Pareto")
plt.ylabel("Gini (última rodada)")
plt.title("Gini × Parâmetro de Pareto")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_pareto.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 3) GINI x NÚMERO DE HOLDERS
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(rod["n_rodadas"].unique()):

    dados = (
        rod[rod["n_rodadas"] == r]
        .groupby(["n_holders","rodada"])
        .agg(
            media=("gini","mean"),
            ic95=("gini","sem")
        )
        .reset_index()
    )

    dados = (
        dados.groupby("n_holders")
        .last()
        .reset_index()
    )

    plt.errorbar(
        dados["n_holders"],
        dados["media"],
        yerr=1.96*dados["ic95"],
        marker="o",
        capsize=5,
        label=f"Rodadas={r}"
    )

plt.xlabel("Número de holders")
plt.ylabel("Gini (última rodada)")
plt.title("Gini × Número de holders")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_holders.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráficos gerados com sucesso!")

# ============================================================
# 4) EVOLUÇÃO DO GINI AO LONGO DAS RODADAS
# (uma curva para cada taxa de reinvestimento)
# ============================================================

plt.figure(figsize=(8,5))

for reinv in sorted(rod["reinveste_recompensa"].unique()):

    dados = (
        rod[rod["reinveste_recompensa"] == reinv]
        .groupby("rodada")
        .agg(
            media=("gini", "mean"),
            desvio=("gini", "std"),
            n=("gini", "count")
        )
        .reset_index()
    )

    dados["ic95"] = 1.96 * dados["desvio"] / (dados["n"] ** 0.5)

    plt.errorbar(
        dados["rodada"],
        dados["media"],
        yerr=dados["ic95"],
        marker="o",
        capsize=5,
        label=f"Reinv. = {reinv}"
    )

plt.xlabel("Rodada")
plt.ylabel("Coeficiente de Gini")
plt.title("Evolução do Gini ao longo das rodadas")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/gini_rodadas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()