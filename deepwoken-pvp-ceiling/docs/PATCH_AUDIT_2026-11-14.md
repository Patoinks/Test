> **FONTE PRIMÁRIA DO JOGO:** [Patch Log oficial, 19 outubro–1 novembro de 2026](PRIMARY_PATCH_LOG_OCT19_NOV1_2026.md), transcrito de capturas reais enviadas pelo utilizador. **Alloyblood e Cauterize foram nerfados em 1/11 (dano e scaling)**, portanto não utilizar valores do lançamento. **Flashpoint** está escrito em 31/10 e **Flashfusion** em 1/11 — identidade por confirmar.

> **ATUALIZAÇÃO JUN–OUT VIA WIKI (`Version_History/Uncollapsed`):** ao contrário da vista anual [Version History 2026](https://deepwoken.fandom.com/wiki/Version_History/2026) que pára em 31/05, [Version History/Uncollapsed](https://deepwoken.fandom.com/wiki/Version_History/Uncollapsed) + [Hallowtide 2026](https://deepwoken.fandom.com/wiki/Hallowtide_2026) cobrem cronologicamente **junho a 31 de outubro de 2026** (`pv_JUN_15_12:31a` até `3.2.23a` e Hallowtide). Em **Agosto 22 (`pv_AUG_22_17:49a`)**, a Fandom confirma cancelamento e cooldown dinâmico **16s–24s** em `Sightless Beam`, enquanto fonte secundária reporta **3s→2s, dano máximo -⅓**. Faltam ainda notas oficiais publicadas **após 31/10 (novembro)**. Ver [mapa mês a mês](PATCH_COVERAGE_JUN_NOV_2026.md).

# Deepwoken: auditoria de patches e meta de dano PvP — 14/11/2026

> **Escopo:** ênfase em mantras, dano máximo por cast, burst, buffs, resistências e confiabilidade em PvP. Este relatório NÃO substitui leitura integral das mensagens do Discord oficial para novembro: a vista colapsada `Version History/2026` pára em 31/05, mas **`Version History/Uncollapsed` documenta patches até 31/10/2026 (`3.2.23a` e Hallowtide 2026)**. Persistem lacunas em hotfixes de **02/11, 06/11 e 09/11** e nos valores exatos de dano por cast dos mantras híbridos.

## 1. Estado dos dados e confiabilidade

| Verificação | Fonte | O que podemos afirmar |
|---|---|---|
| Histórico Jun–Out 2026 & Hallowtide | [Fandom Uncollapsed](https://deepwoken.fandom.com/wiki/Version_History/Uncollapsed) / [Hallowtide 2026](https://deepwoken.fandom.com/wiki/Hallowtide_2026) | Build tags `pv_...`, patches `3.2.14a`..`3.2.23a`, Shrine of Ego (19/10), Hallowtide (31/10), Songchant PEN `5%→3%` (31/05), All Oaths `+5% PEN` |
| Histórico colapsado & 2025 | [Fandom 2026](https://deepwoken.fandom.com/wiki/Version_History/2026) / [2025](https://deepwoken.fandom.com/wiki/Version_History/2025) | `2026` pára em 31/05; `2025` confirma Bleed `30%→15%` (15/11/2025) e poções `-50%` |
| Novos híbridos | [Deepwoken Builder: Exotherm](https://deepwoken.co/builder?id=OFOy9VMS) / [Alloyblood](https://deepwoken.co/builder?id=S9m4DEaN) | Seis mantras constam no Builder; Fandom já lista reqs (`40/40` Exotherm, `50/50` Alloyblood) e stats das 3 armas conjuradas, mas dano Lv5 dos casts continua por medir |
| Detalhes comunitários Hallowtide | [Artigo comunitário 12/11](https://deepwokengame.wiki/updates/hallowtide-2026/) | Complemento descritivo das mecânicas Sanguine Blaze / Alloyblood face ao registo primário de 31/10 na Fandom |
| Publicações Roblox novembro | [Bloxstatus](https://bloxstatus.com/games/deepwoken/updates/) | Observou novas versões em 02, 06 e 09/11; **não há changelog nestes timestamps** |
| Dados estruturados | [`patch_candidates_2026_11.json`](../data/patch_candidates_2026_11.json) | Timeline estruturada, candidatos Hallowtide, stats de armas conjuradas e conflitos com o Builder |
| Meta / win rate | Não disponível | **Não há amostra de Chime Elo ou win rates para declarar S-tier confirmado** |

## 2. Novidades mais relevantes para PvP mantras

### Outubro–novembro: novas hipóteses de meta (existência apoiada por Builder)

**Bloodrend + Flamecharm: `Exotherm: Sanguine Blaze`** *(confirmado na Fandom Hallowtide 2026: `40 BLD + 40 FLM`, exclusivo com Azure Flames / Lava Serpent / Twisted Puppets)*
- `Cauterize`: grab, aplica Black Blood ou detona o que já existe
- `Combustion Tide`: puxa inimigos e explode, com ignição de Black Blood
- `Flashfusion` (também referido como `Flashpoint` na wiki): híbrido existente no Builder; comportamento/ticks e base L5 a confirmar
- Fontes secundárias descrevem Black Blood com até três stacks, slow e anti-heal; Flamecharm não-Burn detonaria stacks. **Não inserir valores de detonação sem fonte numérica**.
- **Hipótese de meta:** burst de 2–3 casts com detonação, anti-heal e potencial procs em cadeia. Não é recorde matemático confirmado de um cast.

**Bloodrend + Ironsing: `Composite Path: Alloyblood` / `Iron Veins`** *(confirmado na Fandom Hallowtide 2026: `50 BLD + 50 MTL`)*
- `Infused Slash`: duas adagas de plasma (**arma conjurada `Alloyblood Daggers`: 14,5 base / 15% PEN / 1,2x na Fandom** — stat da arma conjurada, **NÃO** é o teto do cast do mantra!)
- `Spinning Serum`: lança de plasma com rotação (**arma conjurada `Alloyblood Spear`: 18 base / 25% PEN / 10% chip / 35,6 + 5,3 Bleed na Fandom**; **prioridade para auditar todos os hits do mantra por jogador**)
- `Rising Plasma`: greataxe de plasma (**arma conjurada `Alloyblood Axe`: 24 base / 20% PEN / 20% chip / 0,87x na Fandom**; stat de arma conjurada separada do mantra)
- **Nota de nomenclatura:** a Fandom documenta a alteração visual parcial para *Iron Veins* (homónimo do talento passivo de 100 Ironsing `-30%` bleed dmg / `-75%` blood loss); não confundir o talento de 100 Ironsing com o path híbrido.
- **Hipótese de meta:** multi-hit + controle + procs; desconhecido se ultrapassa Ceaseless ou Tornado no máximo de um cast.

### Alterações 2025–Out/2026 confirmadas pelo histórico Fandom (`Uncollapsed` + `2025`)

**Alterações que mudam cálculos ou builds:**
1. `All Oaths` recebem **+5% de PEN em todas as fontes de dano**, substituindo o antigo bónus específico associado a Thresher Claws (que permanece talento genérico Power 13 de Weapon PEN). **Não contar o antigo bónus mais o novo como se fossem aditivos independentes**.
2. **Songchant Mantra PEN (`31/05/2026`, `pv_MAY_31_23:53a`):** `Version_History/Uncollapsed` reduz Mantra PEN por ponto de Songchant de **`5% → 3%`** (máx. hipotético `18%` a 6 pts vs **`2,5%/pt → 15%`** ainda listado em [Traits](https://deepwoken.fandom.com/wiki/Traits)). **Auditar em jogo antes de fechar modelo de PEN.** Enquanto isso, o scaling de dano continua **+7,5% por ponto**.
3. `Bleed weapons` (`15/11/2025`) tiveram DoT reduzido de **30% → 15%** do dano escalado; e em `Version_History/2025` consta literalmente **`Damage potion increase/decrease efficiency nerfed by 50%`**.
4. `Gourmet` aumenta **50% a duração dos buffs de comida**. Não aumenta a potência da comida Enchant; melhora a manutenção do +5% de dano de mantra em Overworld.
5. `Shadow Meteor` teve **redução de dano** (sem novo valor numérico publicado) e é **cancelado por *Death from Above* / weapon Critical**. O valor 105 de base usado no dataset anterior está sinalizado em `mantras.json` como potencialmente desatualizado.
6. `Ceaseless Slashes` recebeu ligeira redução de base/windup com ramp em hits consecutivos + correção de bug de mobilidade (alinhando-se ao base `290` do Builder vs `310,05` legado).
7. `Sightless Beam` (`pv_AUG_22_17:49a`): `Uncollapsed` confirma que é **cancelável a meio do channel** e que **cooldown (`16s–24s`) e custo de sanidade escalam com a duração** (complementando a fonte secundária `3s→2s, -1/3 max dmg`). `Gale Trap` / `Wind Gun` perderam auto-aplicação de *Suffocate* e `Gale Trap` subiu de **10s → 18s CD**.
8. `28/09/2026` (`pv_SEP_28_01:33a`): corrigido bug de trainers que permitia **Lv6 mantras** acima do cap de atributo, mais correção automática pós-*Shrine of Mastery*. `19/10/2026` (`pv_OCT_20_01:11a`): *Shrine of Mastery* + *Conceit* fundidos em **Shrine of Ego**, além de cooldown contra stacking de *Ardour Scream*.
9. `Scarlet Cyclone` tornou-se **2-star**; **Ring stacking corrigido**; **Rending Impact em mantras** corrigido; **Arcwarder** perdeu buff geral mantendo `+50% Arc Beam` / `+25% Arc Wave`; **Equipment sem enchant ocupa slots de enchant** (relevante para Specialist full set).

**Outras notas que podem alterar o PvP real:**
- Há alterações de parry/air counter, mantras mais telegráficos, tempo de animação/endlag e correções de stacking que tornam uma sequência de 20 hits menos plausível contra jogadores competentes.
- Não multiplicar dano por críticos de arma ou buffs de M1 quando o mantra é a fonte de dano.

## 3. Recalcular antes de eleger novo líder

**Confronto Deepwoken Builder (indexado em novembro) vs nosso dataset**:

| Mantra | Base em ficheiro | Base no Builder atual | Exemplo 100 stat / 6 Songchant, sem buff | Com pool comum ×1,5 |
|---|---:|---:|---:|---:|
| Ceaseless Slashes | 310,05 | **290,00** | **359,38** | **539,07** |
| Tornado | 177,60 | **186,48** | **260,84** | **391,26** |
| Shadow Meteor | 105,00 | **desconhecida após nerf** | — | — |

Os valores são `B × [1 + (s/1000) × 100 × (1 + 6 × 0,075)]`, com `s = 1,65` para Ceaseless e `s = 2,75` para Tornado; coluna ×1,5 assume hard cap condicionalmente atingido. São cálculos brutos **antes de PEN/resistências** e **não garantem que 20 hits ou 12 ticks acertem o jogador**. Dano de Ceaseless como base agregada no Builder não significa 1 único hit; sua distribuição/timing continua sem confirmação.

O ranking antigo `Ceaseless 576,34 > Tornado 372,63` NÃO representa mais as bases que o Builder atualmente mostra. Com os novos valores, continua `Ceaseless 539,07 > Tornado 391,26` **entre esses dois candidatos, se todos os hits acertarem**, mas não é prova de ceiling geral.

**Referências:**
- [Ceaseless Lv5 = 290](https://deepwoken.co/builder?id=gOxvxvnY)
- [Tornado Lv5 = 186.48](https://deepwoken.co/wiki/mantra/Tornado)
- [Crimson Rain Lv5 46.5 numa entrada da wiki Builder](https://deepwoken.co/wiki/mantra/Crimson%20Rain) — nosso `93` de initial+recall é **duas instâncias**, não necessariamente 93 no mesmo cast/hit. Confirmar o ciclo de retorno.

## 4. Conceito de meta PvP: três objetivos diferentes

| Objetivo | Melhor candidato para priorizar testes, NÃO líder comprovado | Porquê |
|---|---|---|
| Máximo dano teórico de um cast comum, all-hit | Ceaseless Slashes L5 | Continua grande base agregada, mas vulnerable a parry/escape e depende de sequência completa |
| Maior burst consistente após setup | Sanguine Blaze | Detonação Black Blood + antiheal sob condições verificáveis em duas ações |
| Multi-hit e procs sobre mesmo alvo | Spinning Serum / Infused Slash | Hit-count e rehit mechanics precisam de logs |
| Melhor uptime de dano de mantra | Ring of Casters + Enchant Food (+Gourmet extensão) | Baixa dependência de estado; não confundir com hard cap |
| Dano de longa distância por cast sem preparação | Flame Ballista, Eclipse Kick, outros hits individuais | Base menor, mas all-hit mais fiável do que channel longo; depende da reação/parry |

**Não declarar nova meta vencedora sem damage logs e dados PvP recentes.** Builds populares no Builder não são evidência de win rate ou de ceiling.

## 5. Plano de verificação rápido e prioritário

1. Capturar dados de dano e hits em alvo sem resistência para `Cauterize`, `Combustion Tide`, `Flashfusion`, `Infused Slash`, `Spinning Serum` e `Rising Plasma`, com os buffs **desligados**.
2. Testar stack Black Blood: 0, 1, 2, 3; comparar detonação e procs em alvo idêntico; verificar se o dano de detonação entra no pool de damage modifiers.
3. Testar se Spinning Serum conta hits do mantra, hits de arma substituta ou ambos; efeitos que só aplicam a M1 não devem ser incluídos de forma automática.
4. Revalidar os **níveis 5 de Tornado e Ceaseless** e a distribuição dos hits contra um único jogador.
5. Revalidar `Shadow Meteor` (nerf pós-dataset), `Crimson Rain` (recast/return) e a duração de `Gourmet`.
6. Confirmar estatuto oficial dos patches de **31/10, 06/11, 09/11 e 13–14/11** no Discord do jogo, sobretudo eventuais nerfs de Gale / híbridos, antes de cravar meta.
7. Rodar um solver com requisitos reais de talentos, dual attunement e oath, incluindo hard cap 100 por atributo e total 330, e calcular resistência líquida pós-PEN.

## 6. O que este relatório NÃO confirma

- O conteúdo oficial e eventuais hotfixes dos updates Roblox de **02/11, 06/11 e 09/11/2026** (a Fandom `Uncollapsed` pára em **31/10/2026** com Hallowtide 2026). *(Nota: a data 31/10 para Hallowtide / Sanguine Blaze / Alloyblood e 19/10 para Shrine of Ego **já estão confirmadas na Fandom**, faltando apenas os números de dano por cast dos 6 mantras híbridos.)*
- Qualquer percentagem exata de dano da detonação Black Blood, do buildup de Plasma, ou da diferença de Lv5 de `Flashfusion`/`Flashpoint`.
- Valores numéricos exatos de dano pós-nerf para `Shadow Meteor` ou se `Tornado = 186,48` no Builder inclui `After Cut` (+5%).
- Que o máximo de Ceaseless (`290` ou `310,05`) ou Tornado (`177,6` ou `186,48`) é atingível contra humano ativo.
- Que `Songchant Mantra PEN` em servidor vivo é `3%/pt` (`Uncollapsed` 31/05) ou `2,5%/pt` (`Traits`).

**Estado final:** base de dados antiga requer refresh; forte candidato a mudança de meta de combos é Sanguine Blaze e de multi-hit é Alloyblood; teto matemático e nova build dominante não demonstrados.
