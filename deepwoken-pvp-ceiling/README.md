> **ONE-TAP / ONE-SKILL PvP (14/11/2026):** [comparação matemática de golpes únicos e casts, excluindo Ceaseless](docs/ONESKILL_PVP_2026-11-14.md). [Calculadora independente](src/oneskill_pvp_2026.py) e [testes](tests/test_oneskill_pvp_2026.py). O Eclipse Kick Lv5 foi corrigido de 92 para **115 de base**, conforme Builder; qualquer “recorde” continua condicionado à compatibilidade dos buffs e às resistências reais.

> **FONTE PRIMÁRIA DO JOGO:** [Patch Log oficial, 19 outubro–1 novembro de 2026](docs/PRIMARY_PATCH_LOG_OCT19_NOV1_2026.md), transcrito de capturas reais enviadas pelo utilizador. **Alloyblood e Cauterize foram nerfados em 1/11 (dano e scaling)**, portanto não utilizar valores do lançamento. **Flashpoint** está escrito em 31/10 e **Flashfusion** em 1/11 — identidade por confirmar.

# Deepwoken PvP — teto matemático de dano de Mantras

**Status:** auditoria reprodutível, NÃO uma prova de recorde global. Atualizado em 2026-11-14.

> **ATUALIZAÇÃO DE META / PATCHES 14/11/2026:** [Ler auditoria de patches e nova meta](docs/PATCH_AUDIT_2026-11-14.md). Ao contrário da vista colapsada `Version_History/2026` (que pára em maio), [`Version_History/Uncollapsed`](https://deepwoken.fandom.com/wiki/Version_History/Uncollapsed) + `Hallowtide 2026` cobrem **junho a 31/10/2026** (`3.2.14a`..`3.2.23a`, All Oaths `+5% PEN`, Songchant PEN `5%→3%` a 31/05, Sightless Beam cancel/16–24s CD, Gale Trap `10→18s`). Novos híbridos de `Exotherm: Sanguine Blaze` e `Alloyblood` já aparecem na Fandom e no Builder. O Builder indica **Tornado L5 = 186,48** (vs 177,60), **Ceaseless L5 = 290** (vs 310,05) e **Crimson Rain = 46,5** single-cycle (vs 93 throw+recall); o dataset histórico preserva números antigos para comparação, **não como leaderboard atual**. Faltam ainda notas descritivas dos hotfixes de **novembro (02, 06 e 09/11)**. [Entradas pendentes](data/patch_candidates_2026_11.json).

> **COBERTURA MÊS A MÊS JUN–NOV:** ver [mapa de cobertura Jun–Nov 2026](docs/PATCH_COVERAGE_JUN_NOV_2026.md) para a separação entre entradas primárias Fandom (`Uncollapsed`), métricas secundárias (ex.: Sightless Beam `3s→2s`, dano máximo `-⅓` em fonte secundária), timestamps Roblox de novembro e dados por medir in-game.

## Âmbito
Investigar máximo de dano PvP num único mantra, todos os hits por cast, procs e buffs possíveis legalmente. Distinguir dano bruto (sem resistência), dano efetivo contra jogador, burst de rotação, Chime e Overworld. A wiki consultada pode estar desatualizada.


> **ALERTA DE FONTES:** o Deepwoken Builder apresenta Ceaseless Slashes L5 com **290 de base**, enquanto a decomposição antiga por ticks da Fandom usada aqui dá **310,05**. Logo, **576,34 NÃO está confirmado na versão atual**. Ver [cenários PvP fiáveis](docs/RELIABLE_PVP.md) para valores mais defensáveis e o plano de verificação.

> **AUDITORIA DE 14/11/2026 — [ler antes de usar os números](docs/AUDIT_2026-11-14.md):** a página atual de [`Traits`](https://deepwoken.fandom.com/wiki/Traits) lista **Songchant a +7,5%/pt (máx. +45%)** e **Proficiency a +6,5%/pt (máx. +39%)**, coerente com o buff posterior a fevereiro de 2026 no `Version_History`, enquanto os exemplos antigos na página [`Mantras`](https://deepwoken.fandom.com/wiki/Mantras) (`70,63` e `25,19`) ainda usam **0,065** (`--songchant-rate 0.065` incluído na CLI para reconciliação). Valores da tabela são cenários de *todos os hits* + teoria máxima de itens PvP (`--item-theory`), não dano PvP garantido.
>
> **Poções:** os 27,5% são apenas resultado do modelo de receita da wiki. Um [patch em novembro de 2025](https://deepwoken.fandom.com/wiki/Version_History/2025) reduziu a eficácia de poções de dano em 50%; desconhece-se se a tabela atual já incorpora a redução. Dano real de poção requer teste.
>
> **Damage sources fora do cap:** [Arcwarder Enhance](https://deepwoken.fandom.com/wiki/Oath%3A_Arcwarder) altera o *dano base* de Arc Beam (+50%) e Arc Wave (+25%). [Shock Trooper Specialist](https://deepwoken.fandom.com/wiki/Hybrid_Abilities) dá +15% de base a seis mantras específicos apenas com o **conjunto completo**. [Fan the Flames](https://deepwoken.fandom.com/wiki/Hybrid_Abilities) permite aplicar Inhale a Flamecharm.
>
> Comparação [**sem buffs vs pool comum saturado ×1,50**](docs/AUDIT_2026-11-14.md).

## Resultados documentados
- Hard cap PvP para a categoria dos damage modifiers: **1,50×**; soft cap **1,25×**. Segundo a calculadora Deepwoken Builder, o excesso após +25% conta a metade até +50%. Assim, +75% nominal basta para saturar essa categoria (fontes: Version History 2025; deepwoken.co/builder).
- **Comida Enchant:** Candied Fruit / Fish Omelette, **+5% dano de mantras** (builds com `Carnivore` têm de usar Fish Omelette). Buffs alimentares de tipos diferentes substituem-se, não somar Enchant e Brain.
- **Ring of Casters:** **+5% dano de mantras**, -5% dano de arma.
- **Perfect Flash:** **+25% dano de mantras** acima de 95% de HP (25 INT), reduz com distância (10% a longa distância). Confirmar se entra no pool geral de modifiers em todos os modos.
- **Poção Strengthening:** 3 Plumfruits + 2 Browncaps, ingredientes +2% dano cada: **10% base**, com 100 INT no FABRICANTE + Apothecary soma potência 50%+125%, ou seja **27,5%**. Só pode existir um efeito de poção de cada vez no alvo; Browncap inflige dano instantâneo ao beber e Plumfruit reduz regen.
- **Taunt:** alvo recebe +20% de dano (25 CHA), tratado como modificador e sujeito ao cap. Ele causa +10% de dano ao caster.
- **Tough Love:** a versão para mantras é **+5%** (e não +10%, 25 CHA).
- **Lose Your Mind** (30 STR + 30 FTD): escala abaixo de 70% sanidade até **+15% dano** a 0% sanidade (ativável via *Heretic's Sutra* a 80 WIL).
- **Dark Hours** (35 Shadowcast): **+15% dano** em mantras Shadowcast à noite ou nas Depths.
- **Exclusões confirmadas (não afetam mantras):** **Reinforce**, **Overflowing Dam**, **Shade Devour**, **Nullifying Clarity** (M1s only) e **Charged Return** (M1s/Criticals only).
- **Mantra PEN (não incluído no dano bruto):** **Prophet's Cloak** (+20% Mantra PEN), **6 Songchant** (+15% PEN), **Ironsing** (+30% inato) e **Piercing Will** (+15%); cap base de 50% PEN sem `Ether Overdrive`.
- **Ceaseless Slashes** nível 5: 5 cortes iniciais [20,25,30,35,40] + 15 ticks de 10,67 = 310,05 base no cenário Fandom de 20 hits (`576,34`), vs **290 base** no Deepwoken Builder (`539,07`). Ambos constam agora em `data/mantras.json` com aviso de divergência.

## Cenário de saturação condicional
| Item | +Dano |
|---|---:|
| Perfect Flash (HP >95%, perto) | 25% |
| Poção Strengthening forte, preparada por 100 INT + Apothecary | 27,5% |
| Taunt no alvo | 20% |
| Enchant food | 5% |
| Ring of Casters | 5% |
| Total nominal se acumularem | **82,5%** |
| Resultado da categoria sob cap | **+50% (1,50×)** |

A soma acima é **hipótese de categoria comum e de sobreposição temporal**, não garante que todos os buffs sejam calculados da mesma forma pelo servidor. Em alternativa sustentável a >95% HP (sem *self-damage* de Browncap nem *self-burn* de Flame Within), combinações com `Lose Your Mind` (+15%) e `Dark Hours` (+15% Shadowcast) também atingem **1,50×** em `src/buff_scenarios.py`.

## Executar
```bash
python deepwoken-pvp-ceiling/src/ceiling.py --show-buffs --compare --item-theory
python deepwoken-pvp-ceiling/src/item_theory.py --no-ceaseless --top 6 --proven-only --with-extras --target-armor 35
python deepwoken-pvp-ceiling/src/item_theory.py --no-ceaseless --by-attunement --target-armor 35
python deepwoken-pvp-ceiling/src/ceiling.py --songchant-rate 0.065 --compare
python deepwoken-pvp-ceiling/src/buff_scenarios.py
python -m unittest discover -s deepwoken-pvp-ceiling/tests -v
```
*(Em Linux/macOS pode ser `python3`.)*

## Ficheiros
- `src/ceiling.py`: fórmulas, tabelas (`--songchant-rate` 0.075 atual vs 0.065 legado), PEN/Armor e candidatos (`data/mantras.json` com 70 entradas, Top 6+ por Attunement + Oath mantras).
- `src/item_theory.py` e `data/items.json`: teoria máxima de itens PvP (`Prophet's Cloak`, `Specialist Set +15% base`, `Ring of Casters + Isshin's Ring`, `Deepfire Ring`, `Nocturnal Gem + Brain Food (+15)`, `Sear (+40% Cauterize -> 100% PEN)`, `Grim` debuff, `--top N` / `--proven-only` / `--with-extras` / `--no-oath-mantras`, Bleed `+15%`, After Cut `2.5%/5%`, Storm Strike `+15`, Everchanging Aegis `-20%`, Dawnwalker `Blinding Dawn` híbrido e quarentena de `Vow of Iron` / `Belief` / PvE).
- `src/buff_scenarios.py`: auditoria combinatória de buffs lida diretamente de `data/buffs.json`, com filtros de HP, elemento e orçamento de 330 pontos.
- `tests/test_ceiling.py`: testes regressivos, exemplos resolvidos da Wiki (`70,63` / `25,19` a `0.065` e `0.075`), validação de `buff_scenarios.py` e `item_theory.py`.
- `docs/RESEARCH.md`: evidências, nuances e restrições.
- `docs/RELIABLE_PVP.md`: cenários defensáveis e comparativo de single-hits.
- `docs/TEST_PLAN.md`: ensaios in-game que faltam.
- `docs/PATCH_AUDIT_2026-11-14.md` e `docs/PATCH_COVERAGE_JUN_NOV_2026.md`: auditoria de patches maio–31/out (`Uncollapsed`), lacunas de novembro e impactos na meta.
- `data/patch_candidates_2026_11.json`: timeline estruturada (`2025`–`2026-11`), candidatos Hallowtide (`Exotherm`/`Alloyblood`) e conflitos com o Builder.
- `SOURCES.md`: fontes diretas.

**Limitação:** faltam hotfixes de novembro de 2026 posteriores a 31/10 (Discord) e valores Lv5 medidos em jogo dos mantras híbridos Hallowtide e de `Shadow Meteor` pós-nerf; um valor de calculadora não prova maximum matematicamente alcançável.

Este projeto não tem afiliação oficial com Deepwoken.
