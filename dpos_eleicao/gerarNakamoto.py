"""
gerarNakamoto.py
----------------
Gera os dados do Coeficiente de Nakamoto (G10 – Concentracao de recompensas).

Usa exatamente os mesmos parametros da grade do G10 ja estabelecida e salva
os resultados em nakamoto_resultados.csv (sem sobrescrever arquivos existentes).

Uso:
    python gerarNakamoto.py
"""

import io
import contextlib
import os
import numpy as np

# O bloco de nivel de modulo do simulador executa rodar_csv ao ser importado.
# Suprimimos o stdout para evitar mensagens duplicadas; os arquivos existentes
# (cenarios.csv / resultados.csv) nao sao alterados porque o bloco ja rodou e
# o Python faz cache do modulo apos o primeiro import.
with contextlib.redirect_stdout(io.StringIO()):
    import simulador_dpos as sim

# ------------------------------------------------------------------
# Autoteste da implementacao
# ------------------------------------------------------------------
_ctx = sim.Contexto(
    cfg=sim.Config(), camada="stake",
    shares=np.array([0.5, 0.3, 0.2]),
    stakes=np.array([0.5, 0.3, 0.2]),
    scores=np.zeros(3), eleitos=np.array([0]),
    pool=np.array([0, 1, 2]), peso_corte=0.0,
    vota=np.ones(3, dtype=bool),
    aprovacoes=np.zeros((3, 3), dtype=bool),
    idx_diretos=np.array([0, 1, 2]),
    blocos=np.array([1.0, 0.0, 0.0]),
    historico=[]
)
_nc = sim.coef_nakamoto(_ctx)
# 0.5 > 1/3 na primeira posicao → Nc = 1
assert _nc == 1.0, f"Autoteste falhou: esperado 1.0, obtido {_nc}"
print(f"Autoteste coef_nakamoto: OK  (Nc={_nc:.0f} para shares=[0.5,0.3,0.2], limiar=1/3)")

# ------------------------------------------------------------------
# Grade identica a usada pelo G10 no simulador_dpos.py
# ------------------------------------------------------------------
grade = {
    "n_holders":            [200, 500, 1000],
    "parametro_dist":       [1.1, 1.5, 2.0],
    "n_rodadas":            [5, 10, 20],
    "reinveste_recompensa": [0.0, 0.25, 0.5],
}

cenarios = sim.gerar_cenarios(
    grade,
    metricas=["coef_nakamoto"],
    camadas_alvo=["stake", "eleito", "produzido"],
    grupo="G10",
    patologia="concentracao_de_recompensas",
    n_runs=30,
    seed_base=0,
)

sim.salvar_cenarios(cenarios, "nakamoto_cenarios.csv")
print(f"{len(cenarios)} cenários salvos em nakamoto_cenarios.csv")

resultados = sim.rodar_csv("nakamoto_cenarios.csv", "nakamoto_resultados.csv")
print(f"{len(resultados)} resultados salvos em nakamoto_resultados.csv")
