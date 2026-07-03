import os
import pandas as pd
import matplotlib.pyplot as plt

RESULTADOS = "./nakamoto_resultados.csv"

PASTA = "./graficos/nakamoto"
os.makedirs(PASTA, exist_ok=True)


# ============================================================
# LEITURA
# ============================================================

res = pd.read_csv(RESULTADOS)

nc = res[res["metrica"] == "coef_nakamoto"]


# ============================================================
# 1) NAKAMOTO x REINVESTIMENTO (por numero de rodadas)
# ============================================================

plt.figure(figsize=(8, 5))

for r in sorted(nc["n_rodadas"].unique()):

    dados = (
        nc[nc["n_rodadas"] == r]
        .groupby("reinveste_recompensa")
        .agg(
            media=("media", "mean"),
            ic95=("ic95", "mean")
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

plt.xlabel("Reinvestimento da recompensa")
plt.ylabel("Coeficiente de Nakamoto")
plt.title("Coeficiente de Nakamoto × Reinvestimento")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/nakamoto_reinvestimento.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 2) NAKAMOTO x PARETO (por numero de rodadas)
# ============================================================

plt.figure(figsize=(8, 5))

for r in sorted(nc["n_rodadas"].unique()):

    dados = (
        nc[nc["n_rodadas"] == r]
        .groupby("parametro_dist")
        .agg(
            media=("media", "mean"),
            ic95=("ic95", "mean")
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

plt.xlabel("Parâmetro de Pareto")
plt.ylabel("Coeficiente de Nakamoto")
plt.title("Coeficiente de Nakamoto × Parâmetro de Pareto")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/nakamoto_pareto.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 3) NAKAMOTO x NUMERO DE HOLDERS (por numero de rodadas)
# ============================================================

plt.figure(figsize=(8, 5))

for r in sorted(nc["n_rodadas"].unique()):

    dados = (
        nc[nc["n_rodadas"] == r]
        .groupby("n_holders")
        .agg(
            media=("media", "mean"),
            ic95=("ic95", "mean")
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
plt.ylabel("Coeficiente de Nakamoto")
plt.title("Coeficiente de Nakamoto × Número de holders")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/nakamoto_holders.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 4) NAKAMOTO POR CAMADA (stake / eleito / produzido)
# ============================================================

plt.figure(figsize=(8, 5))

for camada in ["stake", "eleito", "produzido"]:

    dados = (
        res[
            (res["metrica"] == "coef_nakamoto") &
            (res["camada"] == camada)
        ]
        .groupby("reinveste_recompensa")
        .agg(
            media=("media", "mean"),
            ic95=("ic95", "mean")
        )
        .reset_index()
    )

    plt.errorbar(
        dados["reinveste_recompensa"],
        dados["media"],
        yerr=dados["ic95"],
        marker="o",
        capsize=5,
        label=camada
    )

plt.xlabel("Reinvestimento")
plt.ylabel("Coeficiente de Nakamoto")
plt.title("Coeficiente de Nakamoto por camada")
plt.grid(True)
plt.legend()

plt.savefig(
    f"{PASTA}/nakamoto_camadas.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Gráficos gerados com sucesso!")
