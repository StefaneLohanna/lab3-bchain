import os
import pandas as pd
import matplotlib.pyplot as plt

RESULTADOS="./resultados.csv"

PASTA="./graficos/numeroEfetivo"
os.makedirs(PASTA, exist_ok=True)


# ============================================================
# LEITURA
# ============================================================

res=pd.read_csv(RESULTADOS)

ne=res[
    (res["metrica"]=="numero_efetivo") &
    (res["camada"]=="stake")
]

gini=res[
    (res["metrica"]=="gini") &
    (res["camada"]=="stake")
]


# ============================================================
# 1) NUMERO EFETIVO x REINVESTIMENTO
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(ne["n_rodadas"].unique()):

    dados=(
        ne[ne["n_rodadas"]==r]
        .groupby("reinveste_recompensa")
        .agg(
            media=("media","mean"),
            ic95=("ic95","mean")
        )
        .reset_index()
    )

    plt.errorbar(
        dados["reinveste_recompensa"],
        dados["media"],
        yerr=dados["ic95"],
        marker="o",
        capsize=5,
        label=f"{r} rodadas"
    )

plt.xlabel("Reinvestimento")
plt.ylabel("Número efetivo")
plt.title("Número efetivo × Reinvestimento")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/numeroEfetivo_reinvestimento.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# ============================================================
# 2) NUMERO EFETIVO x PARETO
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(ne["n_rodadas"].unique()):

    dados=(
        ne[ne["n_rodadas"]==r]
        .groupby("parametro_dist")
        .agg(
            media=("media","mean"),
            ic95=("ic95","mean")
        )
        .reset_index()
    )

    plt.errorbar(
        dados["parametro_dist"],
        dados["media"],
        yerr=dados["ic95"],
        marker="o",
        capsize=5,
        label=f"{r} rodadas"
    )

plt.xlabel("Parâmetro Pareto")
plt.ylabel("Número efetivo")
plt.title("Número efetivo × Pareto")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/numeroEfetivo_pareto.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()



# ============================================================
# 3) NUMERO EFETIVO x HOLDERS
# ============================================================

plt.figure(figsize=(8,5))

for r in sorted(ne["n_rodadas"].unique()):

    dados=(
        ne[ne["n_rodadas"]==r]
        .groupby("n_holders")
        .agg(
            media=("media","mean"),
            ic95=("ic95","mean")
        )
        .reset_index()
    )

    plt.errorbar(
        dados["n_holders"],
        dados["media"],
        yerr=dados["ic95"],
        marker="o",
        capsize=5,
        label=f"{r} rodadas"
    )

plt.xlabel("Número de holders")
plt.ylabel("Número efetivo")
plt.title("Número efetivo × Holders")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/numeroEfetivo_holders.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráficos gerados com sucesso!")