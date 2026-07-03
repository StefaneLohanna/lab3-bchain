# Análise colaborativa dos algoritmos consenso em Blockchain

Em nossas discussões sobre blockchain, o **Proof of Work (PoW)**, popularizado pelo Bitcoin, é frequentemente o ponto de partida e a referência principal. Ele foi uma das soluções para resolver o problema do gasto duplo de forma descentralizada. No entanto, como vimos, o PoW também apresenta desafios, um deles e o alto consumo de energia e à escalabilidade (o número de transações por segundo).

Para superar essas limitações e atender a diferentes necessidades, a comunidade de pesquisadores e desenvolvedores criou uma gama de algoritmos de consenso alternativos. Alguns dos mecanismos que exploraremos incluem:

*   **Proof of Stake (PoS)**
*   **Practical Byzantine Fault Tolerance (PBFT)**
*   **Delegated Proof of Stake (DPoS)**
*   **Proof of History (PoH)**
*   **Proof of Authority (PoA)**

Sabendo que **não existe o "melhor" algoritmo de consenso em termos absolutos**. Cada um representa uma solução com diferentes **trade-offs**, geralmente buscando equilibrar três pilares fundamentais: **Segurança, Escalabilidade e Descentralização**.

Um algoritmo otimizado para transações ultrarrápidas em uma rede corporativa privada (como o PBFT) fará concessões muito diferentes de um que prioriza a descentralização máxima em uma rede pública global (como o PoS). A escolha do algoritmo define a arquitetura, o propósito e as limitações de uma blockchain.

> 🎯 O objetivo desta atividade é que vocês investiguem alguns desses algoritmos consenso. A tabela abaixo distribui os temas para as apresentação de vocês.


| Algoritmo / Mecanismo                              | Blockchain / Aplicação             | Conjunto de Artigos 01 | 
|----------------------------------------------------|------------------------------------|------------------------|
| **Practical Byzantine Fault Tolerance (PBFT)**     | Hyperledger Fabric, Tendermint     | a. Castro & Liskov, *Practical Byzantine Fault Tolerance* (1999) – [OSDI PDF](http://pmg.csail.mit.edu/papers/osdi99.pdf)</br>b. Chondros et al., *On the Practicality of "Practical" BFT* (2011, arXiv) – [arXiv](https://arxiv.org/abs/1110.4854) </br>c. **Você pode escolher outro** |
| **Proof of Stake (PoS)**                           | Ethereum, Cardano, etc.            | a. "Casper the Friendly Finality Gadget" - [arxiv](https://arxiv.org/abs/1710.09437) </br>b. Abellán Álvarez et al., *Unsealing the secrets of blockchain consensus…* (2024, arXiv) – [arXiv](https://arxiv.org/abs/2401.14527) </br> c. Saleh, *Blockchain without Waste: Proof‑of‑Stake* (2021, RFS) – [Oxford Academic](https://academic.oup.com/rfs/article/34/3/1156/5868423) , [pdf](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3183935)  </br>d. Nguyen et al., *Proof‑of‑Stake Consensus Mechanisms for Future Blockchain Networks* (2019, IEEE Access) – [ResearchGate](https://www.researchgate.net/publication/334061880_Proof-of-Stake_Consensus_Mechanisms_for_Future_Blockchain_Networks_Fundamentals_Applications_and_Opportunities) </br>e. "Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol" - [Cardano](https://eprint.iacr.org/2016/889.pdf)</br>f. ["Proof of Stake Phase 1: Initial Draft Specification"](https://ethereum.github.io/consensus-specs/#ethereum-proof-of-stake-consensus-specifications) |
| **Delegated Proof of Stake (DPoS)**                | EOS, Tron, BitShares, Steemit      | a. MDPI, *Delegated Proof of Stake Consensus Mechanism* (2023) – [MDPI](https://www.mdpi.com/1099-4300/25/9/1320)</br>b. ArXiv, *Delegated Proof of Reputation* (2019) – [arXiv](https://arxiv.org/pdf/1912.04065) </br>c. Technical White Paper v2 (ios.io) – [PDF](https://academy.bit2me.com/wp-content/uploads/2021/05/eos-whitepaper.pdf)
| **Proof of Authority (PoA)**                       | Ethereum private, POA Network      | a. Joshi, *Feasibility of Proof of Authority as a Consensus Protocol Model* (2021, arXiv) – [arXiv](https://arxiv.org/abs/2109.02480)</br>b. Ekparinya et al., *The Attack of the Clones Against Proof‑of‑Authority* (2019, arXiv) – [arXiv](https://arxiv.org/abs/1902.10244) | 
| **Proof of History (PoH)**                         | Solana                             | a. Solana whitepaper – *A new architecture for a high performance blockchain* (2017/18) – [PDF](https://solana.com/solana-whitepaper.pdf)</br>b. Victor Shoup, *Proof of History: what is it good for?* (2021) – [PDF](https://www.shoup.net/papers/poh.pdf)</br>c. ArXiv, *From Bitcoin to Solana – Innovating Blockchain towards Enterprise* (2022) – [arXiv](https://arxiv.org/pdf/2207.05240) | 


**❗Importante**

> Artigos que **todos os times podem utilizar**, que contem informações em alto nivel de todos os protocolos:
> 1. *Consensus Algorithms on Blockchain* (2022) – [PDF](https://www.scirp.org/pdf/jcc_2022090914431653.pdf)
> 1. *A Comparative Study of Blockchain Consensus Algorithms* (2020) – [PDF](https://iopscience.iop.org/article/10.1088/1742-6596/1437/1/012007)


## Dinâmica da Atividade

Diferente de um trabalho em duplas pré-definidas, esta atividade terá uma abordagem **individualizada na escolha, mas colaborativa na execução**. O processo funcionará da seguinte forma:

1.  **Escolha**: Cada aluno deve escolher **UM** artigo da tabela de temas para analisar.
    <!-- - Obrigatoriamente um time tera que escolher um artigo de Proof of Stake (PoS) e Delegated Proof of Stake (DPoS) -->
2.  **Inscrição**: Adicione seu nome na coluna "Aluno(a) Responsável" ao lado do artigo que você escolheu. A escolha é livre, no modelo "primeiro a chegar, primeiro a ser servido".
    - [📋 link](https://docs.google.com/spreadsheets/d/1GN1cGO_4C01WEEAY4b6OQsBJh99vXAeJUsebsiEj3RA/edit?usp=sharing) da planilha
3.  **Formação dos times**: Alunos que escolherem artigos do **mesmo algoritmo** (ex: todos que escolheram artigos sobre PoS) formarão um "time" de apresentação para aquele tema.
4.  **Apresentação colaborativa**: O "time" deverá preparar **uma única apresentação** sobre o algoritmo. O grande desafio será justamente **apontar os pontos em comum e as diferenças** encontradas nos artigos que cada membro do time analisou.
    - Instruções detalhadas das apresentações na [seção abaixo](#apresentações-google-slides)

## Apresentações (Google Slides)

Cada grupo de tema deverá construir sua apresentação no link correspondente abaixo. O tempo de apresentação por tema será de **20 minutos**, podendo variar em +- 5 minutos em razão da quantidade de alunos.

*   **Tema 1**: [Proof of Stake (PoS)](https://docs.google.com/presentation/d/13qjpxhcrbaHTYSRrm9kDUV4U0OORRJwatLZiKw0DMC4/edit?usp=drive_link)
*   **Tema 2**:  [Delegated Proof of Stake (DPoS)](https://docs.google.com/presentation/d/1kJ132PphVQr2Y6lQ-lxHRoealh8VDIdDOF7373pv1jI/edit?usp=drive_link)
*   **Tema 3**: [Proof of Authority (PoA)](https://docs.google.com/presentation/d/1iL9r2HK4P92l4tXuQ5wb2mkhIIP8qR2RxR9YkF3oJto/edit?usp=drive_link)
*   **Tema 4:** [Proof of History (PoH)](https://docs.google.com/presentation/d/16qMDXgapMYT31xjKoYCTd-BC35Mbl3UozAKAnFgG3kw/edit?usp=sharing)

<!-- Practical Byzantine Fault Tolerance (PBFT)
    *   [Link para a apresentação de Practical Byzantine Fault Tolerance](https://docs.google.com/presentation/d/...) -->

<!-- *   **Tema 3**: Delegated Proof of Stake (DPoS)
    *   [Link para a apresentação de Delegated Proof of Stake](https://docs.google.com/presentation/d/...) -->






## Estrutura sugerida para a apresentação

Segue uma sugestão com pontos, não restritos, que espero nas apresentações:

1. **Visão Geral do Algoritmo**
    - Definição central, problema que resolve, e principais blockchains que o utilizam.
    - Nome do algoritmo e blockchain principal
    - Definição em 1-2 frases simples
    - Problema principal que resolve
1. **Como Funciona (Estratégia)**
    - Fluxo básico do processo de consenso
    - Participantes principais (validadores, delegados, etc.)
    - Critério de seleção para validação
1. **Vantagens vs Desvantagens**
    - Pontos fortes identificados nos artigos
    - Limitações e críticas mencionadas
    - Casos de uso ideais
1.   **Síntese: Vantagens, Desvantagens e Trade-offs**
    *   Com base em todas as leituras, quais são os prós, contras e os principais trade-offs (Segurança vs. Velocidade vs. Descentralização) deste algoritmo?
1. **Análise Comparativa dos Artigos**
    - **Convergências**: O que os artigos concordam?
    - **Divergências**: Onde há diferenças de abordagem?
    - **Evolução**: Como o conceito evoluiu entre os artigos?
    *   **Visão do Artigo 1**: Quais as particularidades ou foco do primeiro artigo? (Apresentado pelo aluno responsável).
    *   **Visão do Artigo 2**: Quais as diferenças, evoluções ou críticas apresentadas no segundo artigo? (Apresentado pelo aluno responsável).



### Dicas para a leitura (Perguntas-Guia)

1. **Qual é o problema de consenso que este algoritmo resolve?**
2. **Quais são os requisitos técnicos (hardware, stake, autorização)?**
3. **Como é garantida a segurança e a descentralização?**
4. **Qual é o trade-off entre velocidade, segurança e descentralização?**
5. **Quais são as críticas ou limitações mencionadas?**


## Critérios de avaliação


### Análise dos Artigos (45%)
- Identificação correta das características do algoritmo
- Comparação efetiva entre os artigos
- Compreensão das convergências e divergências

### Apresentação (35%)
- Clareza na explicação da estratégia
- Cumprimento do tempo (5 minutos)
- Linguagem acessível aos colegas
- A estética dos slides não será avaliada!

### Colaboração (20%)
- Contribuição para o slide comparativo final
- Integração com as outras apresentações
- Qualidade das perguntas/comentários