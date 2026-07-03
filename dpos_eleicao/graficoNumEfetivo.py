import pandas as pd
import matplotlib.pyplot as plt

# Ler resultados
df = pd.read_csv("resultados.csv")

# Filtrar número efetivo na camada stake
ne = df[
    (df["metrica"] == "numero_efetivo") &
    (df["camada"] == "stake")
]

n_holders_vals = sorted(ne["n_holders"].unique())

fig, axes = plt.subplots(1, len(n_holders_vals), figsize=(6*len(n_holders_vals), 5), sharey=True)
if len(n_holders_vals) == 1:
    axes = [axes]

for ax, nh in zip(axes, n_holders_vals):
    sub = ne[ne["n_holders"] == nh]

    for rodada in sorted(sub["n_rodadas"].unique()):
        subset = sub[sub["n_rodadas"] == rodada]

        # agrupa apenas por reinveste_recompensa (dentro de um n_holders fixo);
        # ainda mistura parametro_dist, então mostramos a dispersão real entre
        # esses cenários via desvio-padrão de "media", não a média dos ic95
        agg = (
            subset.groupby("reinveste_recompensa")["media"]
            .agg(["mean", "std"])
            .reset_index()
        )

        ax.errorbar(
            agg["reinveste_recompensa"],
            agg["mean"],
            yerr=agg["std"],
            marker="o",
            capsize=5,
            label=f"Rodadas={rodada}"
        )

    ax.set_title(f"n_holders={nh}")
    ax.set_xlabel("Reinvestimento da recompensa")
    ax.grid(alpha=0.3)

axes[0].set_ylabel("Número efetivo")
axes[0].legend()
fig.suptitle("Número efetivo vs Reinvestimento das recompensas (por n_holders)")
plt.tight_layout()
plt.show()