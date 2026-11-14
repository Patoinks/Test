> **Nota de auditoria (14/11/2026):** Songchant é **+7,5% por ponto (`0,075`, máx. +45%)** segundo [Traits](https://deepwoken.fandom.com/wiki/Traits) e `Version_History` 2026 (Proficiency = 6,5% / +39%); **exemplos resolvidos antigos em `Mantras` (`70,63`, `25,19`) usam o coeficiente pré-patch `0,065`**, suportado em `ceiling.py` via `--songchant-rate 0.065` (`576,34` vs `571,74` em Ceaseless). Ver [AUDIT_2026-11-14.md](AUDIT_2026-11-14.md) e [item_theory.py](../src/item_theory.py). **27,5% de poção é apenas receita teórica: nerf de 50% na eficácia das poções em 15/11/2025.**

# Investigação — metodologia e todas as fontes de dano relevantes

Versão documental: **2026-11-14**. O jogo não expõe nesta investigação uma fórmula de servidor verificável por código-fonte; há números da Wiki e uma calculadora comunitária, sujeitos a patches.

## 1. Definições do problema

### A. Potencial bruto de um cast
Somar TODO o dano das instâncias elegíveis (incluindo ticks separados) antes de resistência do alvo, supondo todos os hits. Isto não é uma garantia de combo ou hit confirmado.

### B. Dano real por jogador
Aplicar resistência física/elemental, talentos defensivos, PEN efetiva, parry/roll/block, estado do alvo, distâncias e janelas de invulnerabilidade. O valor pode ser muito inferior ao teto bruto.

### C. Rotação / burst
Uma sequência de vários casts exige tempo, animação, cooldown, Ether, tempo de controlo, duração de buffs e procs por evento. Não comparar total de um cast com DPS. Um alvo pode recuperar, ventar, bloquear, escapar ou morrer antes de todos os hits.

## 2. Fórmulas

**Mantra comum:**

`D_base = sum(hit_base_i) × (1 + scaling/1000 × attribute × (1 + 0.075 × songchant))`

Coeficiente típico: **1,65** para mantras sem elemento / Weapon e **2,75** para elementais, com exceções por mantra. Necessário verificar as exceções caso a caso. Nivelamento muda a base individual e alguns efeitos, não apenas um multiplicador universal.

**Oath Mantras:** segundo [Mantras](https://deepwoken.fandom.com/wiki/Mantras) e [AUDIT_2026-11-14.md](AUDIT_2026-11-14.md), a fórmula geral de Oath/Monster mantras inclui fator Songchant adicional **`(1 + 0.02 × Songchant)`** (`+12%` a 6 Songchant), já implementado em `ceiling.py` via `"oath_or_monster": true`. Mantras específicos podem ter exceções (ex.: `Sightless Beam` ~150 base sem songchant), e mantras comuns como `Ceaseless Slashes` e `Tornado` **não** usam este fator (`"oath_or_monster": false`).

**Cap PvP da categoria de dano:** valor compatível com o Deepwoken Builder:
- Até +25% bruto: contribuição integral.
- Acima de +25%: contribuição excedente a 50%.
- Hard cap: +50% efetivo.
- Em fórmula, para bônus bruto não negativo B: `1 + min(0.5, min(B,0.25) + 0.5×max(0,B-0.25))`.
- B=0.75 chega a ×1.5; B=0.825 continua ×1.5.
- Existe risco de efeitos que não entram neste mesmo canal (procs, vulnerabilidades, damage type, scaling do próprio mantra). NÃO aplicar teto a tudo indistintamente.

**Dano efetivo simplificado:** bruto × (1 – resistência líquida após PEN). É somente uma aproximação: no jogo, outfit general, type-specific, gear e resistências de talentos combinam de formas diferentes; consultar Character Stats wiki para a fórmula de resistência completa.

## 3. Buffs ofensivos: auditados

| Mecanismo | Efeito de interesse | Aplica mantras? | Nota |
|---|---|---|---|
| Enchant food | +5% | Sim | Candied Fruit / Fish Omelette (`Carnivore` obriga a usar Fish Omelette) |
| Power food | +5% M1 | **Não** | Outro tipo de comida |
| Brain food | Nocturnal proc 10→15 | Apenas proc da gema | Substitui Enchant, não simultâneo |
| Ring of Casters | +5% mantra / -5% melee | Sim | Não presumir stack de vários anéis iguais |
| Isshin's Ring | +15% geral / +20% dano sofrido | Sim | Acumula com `Ring of Casters` (`+20%` bruto só em anéis); sujeito ao cap PvP |
| Grim (Weapon Enchant) | +25% dano sofrido no alvo (~6s) | Condicional (debuff M1) | Canal vs cap comum por confirmar; modela-se em `item_theory.py` |
| Divine Cast Ring | 3× dano (zera Ether) | **ILEGAL em PvP padrão** | Exclusivo de **Vow of Iron** Relic (quarentenado fora do teto Overworld/Chime) |
| Perfect Flash | +25% mantra perto e acima de 95% HP | Sim | 25 INT; confirmar canal do cap e distância |
| Taunt | Alvo recebe +20% | Sim | 25 CHA; explicitamente sujeito ao cap, alvo revida +10% |
| Strengthening potion | Até +27.5% modelo receita (**não confirmado pós-nerf 2025**) | Geral, a confirmar prática | 3 Plumfruit + 2 Browncap; 100 INT + Apothecary **no fabricante**; Browncap dá dano ao beber |
| Tough Love | +5% mantra em Charmed | Sim | 25 CHA; +10% para outras formas de dano; requer Charm |
| Flame Within | +10% geral | Sim (self-burn) | 25 Flamecharm; self-burn contínuo ameaça Perfect Flash >95% HP |
| Inhale / Fan the Flames | até +10% no próximo Gale **ou Flamecharm se tiver Fan the Flames** | Gale ou Fire condicional | 80 Galebreathe (Lv5) + 40 Flamecharm p/ Fan the Flames; janela de 5s |
| Last Resort | +5% abaixo de 25% HP | Condicional | 35 Willpower; **incompatível** com Perfect Flash >95% HP |
| Lose Your Mind | até +15% a 0% sanidade | Sim (assume pool comum) | 30 STR + 30 FTD; escala abaixo de 70% sanity (ativável com Heretic's Sutra a 80 WIL) |
| Dark Hours | +15% Shadowcast noite/Depths | Só Shadowcast | 35 Shadowcast; ativo XX:50–XX:10 IRL ou nas Depths |
| Reinforce | +5% ou +2.5% weapon | **Não** | Wiki declara weapon attacks only |
| Overflowing Dam | até +10% basic | **Não** | Wiki declara basic attacks only |
| Shade Devour | +20 a 25% **weapon** | **Não** | Não atribuir aos mantras seguintes |
| Nullifying Clarity | +10% basic attacks | **Não** | Wiki restringe a basic attacks (M1s) |
| Charged Return | +10% M1/Critical | **Não** | Wiki restringe a basic attacks e criticals |
| Nocturnal Gem | +10 damage fixo, ou +15 com Brain food | Proc separado | NÃO afetado por damage modifiers normais, tem counterplay |

**Mantra PEN e mecânicas ainda fora da fórmula de dano bruto:**
- **Fontes de PEN:** `All Oaths` (**+5% PEN** em todas as fontes de dano, substituindo Thresher Claws PEN em Oaths), `6 Songchant` (**+15% PEN** em `Traits` a `2,5%/pt` vs **`3%/pt → +18%`** segundo `Version_History/Uncollapsed` de 31/05/2026 — divergência por validar), `Prophet's Cloak` (+20% Mantra PEN), `Ironsing` (+30% PEN inata), `Piercing Will` (+15% PEN, via Heretic's Sutra). A PEN base tem cap de **50%**, só removível por talentos como `Ether Overdrive` (90 INT) / `Million Ton Piercer`.
- **Drowned / Yun'Shul Wind-Up Resonance (Bell):** a versão base só aplica em ataques físicos, mas a versão upgraded via Yun'Shul sobe até nível 10 e **passa a ativar em mantras** (percentagem exata sem número fixo documentado na Wiki).

Talentos/sinergias adicionais que ainda exigem verificação de canal ou patch: `After Cut` (**2,5%** em mantras segundo `Talents` / **5%** em M1s — menção legada `5%` em Galebreathe — atuando como **hit secundário fora do cap**), `Matador`, `Rush Hour`, `Spinning Swordsman`, `Blast Furnace`, `Crystallization`, `Emperor Flame`, `Bleed` (`30%→15%` DoT em armas no patch de 15/11/2025) / `Blood Loss` PvP vs PvE. O site Deepwoken Builder lista várias destas fontes, mas **não garante** que todas atuem em mantras. Não adicionamos valores de uma categoria de armas à de mantras.

### Poções (método completo; **modelo de receita, eficácia após o patch NÃO CONFIRMADA**)
- Uma única poção ativa por jogador; outra substitui. Buff dura 15s por defeito.
- Limite habitual: até 5 ingredientes totais, até 3 do mesmo.
- Browncap +2% damage; Plumfruit +2% damage.
- 3 Plumfruit + 2 Browncap ⇒ 5×2% = 10% inicial.
- Brewer 100 Intelligence ⇒ +50% potency; nota: o [patch de 2025](https://deepwoken.fandom.com/wiki/Version_History/2025) reduziu a eficiência das poções de aumento/redução de dano em 50%. Sem testar não sabemos se a tabela dos ingredientes já está atualizada.
- Apothecary ⇒ +125% potency extra (soma à base, NÃO multiplica o resultado anterior): `10% × (1 + 0.5 + 1.25) = 27.5%`.
- **Browncap também dá dano instantâneo ao utilizador**, e Plumfruit reduz regeneração. Se baixarem o HP do caster abaixo do threshold do Perfect Flash, não valem os dois simultaneamente sem cura/mitigação; avaliar Biotic Salts e calendário de aplicação.
- Ingredientes podem ser preparados por um personagem diferente; validar se tipo específico de poção preparável por outra personagem pode ser recebido e usado no modo PvP escolhido.

### Comida
- Enchant +5% mantra, via Candied Fruit ou Fish Omelette.
- O Buff Brain (Grilled Parasol Brain) aumenta Nocturnal de 10 para 15, mas substitui Enchant. O seu benefício para uma build multi-hit de alto dano pode ser menor do que +5% mantra.
- Só a duração da mesma categoria de comida soma, não a potência.
- Para Ceaseless Slashes, uma gema ativada por mantra não é automaticamente 20 procs; verificar limite de proc/cooldown.

## 4. Mantras e hits: não multiplicar projeções impossíveis

| Nível 5 | Hits | Base total | Dano bruto a 100 atributo, 6 Songchant, ×1.5 | Grau de confiança |
|---|---:|---:|---:|---|
| Ceaseless Slashes (Fandom) | 20 | 310,05 | **576,34** | **DISPUTADO** vs 290 no Builder; 5+ cortes não auditados |
| Ceaseless Slashes (Builder) | ? | 290,00 | **539,07** | Base agregada no Deepwoken Builder pós-nerf 2025 |
| Tornado | 12 | 177,60 | **372,63** | **DIVERGENTE** vs **186,48** (`391,26`) no Builder (`×1,05`); After Cut omitido |
| Scarlet Cyclone + Multiplying | 30? | 156,00 | **327,31** | **NÃO CONFIRMADO** 3 projéteis atingirem o MESMO alvo |
| Scarlet Cyclone padrão | 10 | 130,00 | **272,76** | Contagem documentada (2-star no patch 2026) |
| Tornado Kick | 4 | 112,00 | **234,99** | Abertura tem de acertar |
| Metal Rain | ~23 | 110,40 | **231,63** | Estimativa, Bleed adicional não incluído |
| Ice Flock | 8 | 105,60 | **221,56** | Documentado; Everchanging Aegis corta hits seguintes |
| Shadow Meteor | 3 | 105,00 | **220,30** | **POTENCIALMENTE DESATUALIZADO:** nerf de dano em maio 2026 + cancel por Death from Above / Crit |
| Flame Ballista (Full Charge) | 1 | 96,00 | **201,42** | Requer carga máxima; single hit (Burn omitido) |
| Crimson Rain (Initial + Recall) | 12 | 93,00 | **195,13** | 6 ida + 6 recall (**46,5** single-cycle no Builder) |
| Eclipse Kick | 1 | 92,00 | **193,03** | Single hit (50 SHD + 30 STR; elegível a Dark Hours) |
| Shadow Assault Blast | 20 | 62,80 | **131,76** | Somente <=40% HP, NÃO com Perfect Flash |
| Table Flip | 1 | 60,00 | **111,53** | Exemplo Strength de referência |
| Scarlet Cannon | 17 | 51,00 | **107,00** | 17 ticks |
| Rocket Lance | 1 | 47,00 | **98,61** | Single hit Ironsing (+30% PEN inato não incluído) |
| Grand Javelin | 1 | 44,20 | **92,74** | Single hit Thundercall |
| Fire Forge | 3 | 36,99 | **77,61** | 3 adagas Flamecharm (Burn omitido) |

Para Scarlet Cyclone + Multiplying Spark cada projétil passa a **5,2** de base por tick em vez de 13. Mesmo se TODOS acertarem, 3×10×5,2=156; não são 3× o dano da versão normal (390).

O mantra Ceaseless Slashes pode superar 5 cortes quando se recupera Ether durante a execução/timing, segundo a Wiki, mas não há comprovação de um máximo finito ou de que se repita com um jogador a aguentar sem escapar. Isto impede afirmar um recorde absoluto.

## 4B. Efeitos de dano base que ultrapassam o cap

- **Arcwarder Enhance, com Arc Suit ativo:** **Arc Wave +25% base** e **Arc Beam +50% base**, exclusivamente. Dano base entra ANTES de scaling e modifiers, não se reduz no soft/hard cap comum. [Oath: Arcwarder](https://deepwoken.fandom.com/wiki/Oath%3A_Arcwarder)
- **Shock Trooper Specialist:** com **TODAS as peças equipadas**, +15% base em **Grand Javelin, Thunder Kick, Electro Carve, Astral Wind, Champion's Whirlthrow, Gale Lunge**. O capacete isolado não dá o bónus de base; o set também pode causar Stormcall Strikes quando atinge limiar. [Hybrid Abilities](https://deepwoken.fandom.com/wiki/Hybrid_Abilities)
- **Oath/Monster Songchant** +2% por ponto, *além* da fórmula de scaling apropriada. **Ceaseless Slashes e Tornado NÃO são mantras Oath.** [Mantras](https://deepwoken.fandom.com/wiki/Mantras)
- **Fan the Flames:** Inhale (Mantra Wind armazenado) potencia **Flamecharm** com +(nível×2)% até 10%, além de transferir modificadores do mantra inalado. [Hybrid Abilities](https://deepwoken.fandom.com/wiki/Hybrid_Abilities)

## 4C. Teoria máxima de itens para PvP (`data/items.json` / `src/item_theory.py`)

No PvP padrão (Overworld / Chime), a combinação teórica máxima de equipamento que afeta mantras é:
- **Outfit (`Prophet's Cloak`):** `+20% Mantra PEN` via *Crippling Darkness*. Não conflita com Head/Arms/Legs.
- **Set de armadura (quando aplicável):** `Shock Trooper Specialist Full Set` (**+15% dano base fora do cap** nos 6 mantras Thundercall/Galebreathe elegíveis — ex.: `Electro Carve` `70 → 80,5` base, `Champion's Whirlthrow` `61 → 70,15`, `Grand Javelin` `44,2 → 50,83`). Peças são unenchantable e consomem slots de enchant; **Pips e Enchants de armadura comuns (`Ferocity`, `Viscosity`, `Entanglement`, `Multiplicity`, `Drowned`) dão `0%` de dano PvP de mantra** (`Drowned` é PvE-only).
- **Anéis:** `Ring of Casters` (`+5%`) + `Isshin's Ring` (`+15%`) = **`+20%` passivo**; somado a `Enchant Food` (`+5%`) atinge **`+25%` → `1,250×` sem perda por soft cap nem condição de HP/Taunt/Poção**. (`Scaling Rings` só afetam scaling de arma.)
- **Deep Gem:** `Nocturnal Gem` (`+10` slash fixo fora do cap por trigger, ou `+15` com `Brain Food` trocando `+5%` Enchant). `Insignia Gem` reduz windup `-15%`.
- **PEN máximo contra oponente equipado:** `Prophet's Cloak (20%) + All Oaths (5%) + 6 Songchant (15% Traits / 18% Uncollapsed) + Piercing Will (15%) + Ether Overdrive (5% + remove cap 50%) = 60%–63% PEN` (e **`90%–93%` em Ironsing** com `+30%` inato). Contra alvo com `35%` armadura, isto vale mais dano líquido do que exceder o soft cap comum.
- **Canais separados/incertos:** weapon enchant `Grim` (`+25%` incoming dmg por 6s via M1s — mostrado como teto hipotético à parte em `item_theory.py`), Bell `Yun'Shul Wind-Up Lv10` (sem % fixa na Wiki). **`Divine Cast Ring` (`3×`) é exclusivo de *Vow of Iron* Relic e ilegal em PvP padrão.**

## 5. Estados/exclusões e incompatibilidades
- **Perfect Flash >95% HP** e **Last Resort <25% HP** não coexistem no mesmo instante.
- **Perfect Flash >95% HP** e **Shadow Assault Blast <=40% HP** são incompatíveis no mesmo instante.
- Comida **Enchant** e comida **Brain** são buffs exclusivos entre si.
- Apenas uma poção ativa; não empilhar 5 poções Strengthening.
- Oath ou Sparks podem substituir o comportamento/hit base do mantra; não multiplicar o número de projéteis sem reavaliar dano por projétil.
- Algumas habilidades são buffs de M1, de critical ou de weapon e não aplicam a mantras.
- Soft cap/hard cap PvP limitam boosts em determinada categoria, não dano absoluto de todas as fontes.
- A build só dispõe de 330 pontos normais, talent requirements, slots de mantras e oath exclusiva; precisa de solver para provar exequibilidade.
- O alvo pode ter Everchanging Aegis (multi-hit elemental sofre uma redução enorme nos hits posteriores), armaduras, PEN reduction, immunities, dano por parry; baseline usa **0 resistência**.

## 6. Pendências prioritárias
1. Recolher hotfixes de **novembro de 2026** (pós-31/10 — `Version_History/Uncollapsed` já cobre junho–31/10, ver [PATCH_COVERAGE_JUN_NOV_2026.md](PATCH_COVERAGE_JUN_NOV_2026.md) e [PATCH_AUDIT_2026-11-14.md](PATCH_AUDIT_2026-11-14.md)) e medir Lv5 de Exotherm / Alloyblood & Shadow Meteor pós-nerf.
2. Validar cap do Perfect Flash por testes com e sem Taunt/food/potion.
3. Confirmar compatibilidade de food, poções e pre-buffs em Chime e Overworld.
4. Medir se Ceaseless com Ether regen consegue >5 cortes quantas vezes; limites internos de casts.
5. Testar os três cyclones sobre um jogador; retorno Reversal (hit novo ou ignora mesmo alvo?).
6. Medir procs de After Cut e da gema, incluindo cooldown por mantra e por hit.
7. Expandir a validação de builds legais em `buff_scenarios.py` (já lê `buffs.json` e verifica soma <= 330 em fase única) para incluir Oath, slots de mantras e rotas com *Shrine of Order*.
8. Definir resistência do alvo e PEN com fórmula real; só depois comparar dano HP de uma rotação e DPS.
