# Deepwoken — auditoria de **ONE-SKILL PvP** (14/11/2026)

**Objetivo do utilizador:** maximizar dano num único cast, idealmente **um impacto de one-tap**, sem Ceaseless, combinações de várias skills ou preparação agressiva no alvo. Não confundir 20 ticks/10s de canal com golpe instantâneo. Isto é um **modelo numérico**, não uma sessão real de PvP no Roblox.

## Conclusão com os candidatos quantitativamente verificados

| Mantra L5 (100 atributo, 6 Songchant) | Dano base Builder | Hits exigidos | Pré-buff (0%) | Buff comum +25% | Buff cap +50% |
|---|---:|---:|---:|---:|---:|
| **Eclipse Kick** | **115** | **1** | **160,86** | **201,07** | **241,28** |
| Skyshatter Kick | 120 | 2 | 148,71 | 185,89 | 223,06 |
| Flame Ballista | 96 | 1 | 134,28 | 167,85 | 201,42 |
| Ice Flock | 105,6 | 8 | 147,71 | 184,63 | 221,56 |
| Ice Carve (Round Spark) | 100 | 20 | 139,88 | 174,84 | 209,81 |
| Scarlet Cyclone normal | 130 | 10 | 181,84 | 227,30 | 272,76 |
| Scarlet Cyclone Multiplying | 156 | até 30 **NÃO CONFIRMADOS por jogador** | 218,21 | 272,76 | 327,31 |
| Tornado | 186,48 | ~12 | 260,84 | 326,05 | 391,26 |

**Categorias diferentes.** O maior número entre os candidatos é Tornado **em todos os 12 ticks**, mas requer canal/acerto de todas as instâncias — não é one-hit. O mais forte **single-impact comum entre os candidatos verificados** é Eclipse Kick. Não se prova que este seja o máximo de *todos os mantras* introduzidos até novembro; novos híbridos não têm valores quantitativos fiáveis após nerfs de 1 de novembro.

**Fórmula:**
```python
scaled = B * (1 + (scaling/1000)*100*(1 + 6*0.075))
pool_mult = 1 + min(0.50, min(raw_bonus,0.25) + max(0,raw_bonus-0.25)/2)
gross_pvp = scaled * pool_mult
```

## Build e cenário sem ofensiva prévia no alvo — Eclipse Kick

**Atributos exemplificativos viáveis dentro de 330 pontos:** Shadowcast 100 + Willpower 80 + Strength 30 + Fortitude 30 + Intelligence 25 = **265**. Restam **65** para outros atributos. Satisfaz a regra documentada de Shadowcast (Eclipse), Perfect Flash 25 INT e Lose Your Mind 30 STR / 30 FTD + Heretic's Sutra 80 WIL. É um orçamento de atributos, **não** confirmação de roll de todos os talentos/timing/compatibilidade de Oath; testar no Builder.

| Estado | Modificadores brutos do pool | Multiplicador efetivo | Eclipse Kick HP damage bruto |
|---|---:|---:|---:|
| Nenhum | 0 | 1,00 | 160,86 |
| Ring of Casters + Isshin's (perto) + Enchant food | +25% | 1,25 | 201,07 |
| Anteriores + Perfect Flash (>95% HP, perto) + Dark Hours (à noite/Depths) | +65% | 1,45 | 233,24 |
| Ring of Casters (+5) + Isshin (+15) + Perfect Flash (+25) + Dark Hours (+15) + Lose Your Mind (0 sanity, +15) | **+75%** | **1,50** | **241,28** |

**Importante**: Isshin's Ring aplica o seu +15% **em combate próximo** e aumenta o dano recebido pelo portador em +20%; Perfect Flash precisa de HP >95% e proximidade. Dark Hours só é elegível para Shadowcast à noite/Depths. Lose Your Mind a 0 sanity é muito frágil e NÃO uma condição de PvP consistente. Sem ela, usar `1.45×` como **cenário condicionado de opener noturno**, não como dano permanente.

**Nocturnal Gem (opcional):** +10 *flat* após **1 segundo**, ou +15 com *Brain Food*. Como a composição para ×1.5 acima já tem +75% **sem** Enchant Food, pode trocar a comida para Brain e adicionar potencialmente **15** de dano noutra instância = **256,28 bruto em dois eventos**. O proc é **parryable / blockable / dodgeable**, tem cooldown 25s e dano slash independente; **não é literalmente one-hit e não é garantido**. Nunca somar +15 por tick.

**Eclipse Kick tem desvantagem**: recebeu nerf que reduz substancialmente o dano contra adversários já stunned; evitamos qualquer stun setup para não acionar essa redução. O Multiplying Spark exige reativação para efetuar o ataque regular, portanto não é um único acionamento equivalente ao normal.

### Exemplo contra armor, sem afirmar que é a fórmula completa do jogo

Se o alvo tiver **35% resistência de armadura anterior à PEN**, e a PEN efetiva for **50%**, no modelo simplificado:
`241.284375 × (1 − 0.35×(1−0.50)) ≈ 199.06 HP` num hit não defendido. Uma personagem com 400HP não morre com isso — 1 cast de Eclipse Kick não demonstra um **100→0**. O jogo aplica resistências e talentos específicos de forma mais complexa que esta aproximação, e outros efeitos podem reduzir ainda mais o dano.

### O que não foi permitido no teto estrito

- **Ceaseless Slashes**: explicitamente excluído.
- **Taunt, Charm ou Grim/Sear em stacks no inimigo**: exige outra skill/5 M1s/4 heavy M1s, portanto **não é 1 cast sem preparação ofensiva**. Grim também pertence ao pool cap comum; não multiplica ×1.25 fora do cap. [Grim](https://deepwoken.fandom.com/wiki/Grim).
- **Potions**: não usadas porque o patch de 2025 reduziu eficácia de poções de dano em 50% e o valor live atual não foi confirmado. Podem ser cenário separado após teste.
- **Inhale/Fan the Flames**: exige outro cast preparatório, excluído.
- **Ebb and Flow níveis 6–10**: existem no Builder para mantras de Medium/Heavy, mas requerem stack de mantras alternados antes do cast; excluído por ser combo/set-up ofensivo. [Ebb and Flow](https://deepwoken.co/wiki/talent/Ebb%20and%20Flow).
- **Soul Beam**: cerca de 250 de dano total **após resistências médias** segundo Wiki, mas precisa de vários wisps ativos, 2s de windup, 5min cooldown e o beam completo. A wiki não oferece base detalhada atual; não o comparar numericamente com Eclipse como dano bruto. [Soul Beam](https://deepwoken.fandom.com/wiki/Oath%3A_Oathless).
- **Flame Repulsion refletida**: depende de receber outro ataque numa janela estreita; não é dano sob controlo exclusivo do caster, por isso fica fora do teto consistente. [Flamecharm](https://deepwoken.fandom.com/wiki/Flamecharm).
- **Specialist set**: +15% a seis mantras específicos, fora do cap comum; esses mantras devem ser comparados mais tarde com a versão atual pós 31/10. [Specialist Plate](https://deepwoken.fandom.com/wiki/Specialist_Plate).
- **Arcwarder Enhance**: +50% base no Arc Beam, +25% no Arc Wave com suit ativo; habilidades de oath com requisitos diferentes e contagem de hits separada. [Enhance](https://deepwoken.co/wiki/talent/Arc%20Module%3A%20Enhance).
- **Sanguine Blaze e Alloyblood**: novos 31/10, ambos nerfados 1/11; sem coeficientes pós-nerf, **não ordenar inventando valores**. [Notas oficiais transcritas](PRIMARY_PATCH_LOG_OCT19_NOV1_2026.md).

## Fontes de números atuais

- [Eclipse Kick base L5 115, requisito 50 Shadowcast/15 Strength](https://deepwoken.co/wiki/mantra/Eclipse%20Kick)
- [Skyshatter Kick base L5 120 por 2 kicks](https://deepwoken.co/wiki/mantra/Skyshatter%20Kick)
- [Flame Ballista base L5 96](https://deepwoken.co/wiki/mantra/Flame%20Ballista)
- [Ice Flock base L5 105.6](https://deepwoken.co/wiki/mantra/Ice%20Flock)
- [Ice Carve Round L5 base 100](https://deepwoken.co/wiki/mantra/Ice%20Carve)
- [Tornado L5 aggregate 186.48](https://deepwoken.co/wiki/mantra/Tornado) — diverge do antigo 177.6 e **pode já incluir After Cut**.
- [Scarlet Cyclone L5 130; Multiplying L5 aggregate 156](https://deepwoken.co/wiki/mantra/Scarlet%20Cyclone); same-target 30 ticks não verificado.
- [Formulas + Songchant +0.075](https://deepwoken.fandom.com/wiki/Mantras)
- [Nocturnal Gem, 25s CD, 1s delay, +10/+15 apenas um proc](https://deepwoken.fandom.com/wiki/Nocturnal_Gem)
- [Isshin's Ring close-quarters, +15% damage / +20% damage received, cap](https://deepwoken.fandom.com/wiki/Isshin%27s_Ring)
- [Talents: Perfect Flash / Lose Your Mind / Dark Hours](https://deepwoken.fandom.com/wiki/Attribute_Trees)
- [Modifier caps (PvP)](https://deepwoken.fandom.com/wiki/Version_History/2025)

## Testes efetuados e pendentes

**Efetuados:** 9 verificações aritméticas (scaling, caps, dano com +65% e +75%, Ice Carve, Tornado, Flame Ballista, Skyshatter, gem +15 e alvo de armor hipotético). `tests/test_oneskill_pvp_2026.py` testa a calculadora Python.

**Não efetuados:** Roblox in-game damage logs, impacto real do alvo após PEN/armor, legalidade de Brain Food com outros efeitos, verificações completas de todos os novos mantras, se 100% dos ticks acertam o mesmo jogador e bugfixes posteriores a 1/11.

**Conclusão válida:** Eclipse Kick **241,28 bruto como golpe único num cenário condicional x1.5**, 256,28 com uma gema de dano atrasada, **não é prova de um one-tap 100→0** contra Power 20.
