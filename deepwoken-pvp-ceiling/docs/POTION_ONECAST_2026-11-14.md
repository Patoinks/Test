# Poções Strengthening — ONE-SKILL PvP (14/11/2026)

> **Fonte:** [Alchemy Wiki](https://deepwoken.fandom.com/wiki/Alchemy) (ingredientes, fórmula, efeitos negativos, timing) + [Version History/2025](https://deepwoken.fandom.com/wiki/Version_History/2025) (nerf de 15/11/2025). **A eficácia atual no servidor não foi testada**. Os dois cenários são hipóteses alternativas de interpretação do patch, NÃO dois buffs acumuláveis.

## Receita de buff de dano (autoconsumida)
- 3 × Plumfruit (+2% dano cada, mas redução de health regen / efeito secundário).
- 2 × Browncap (+2% dano cada, mas -4 de dano instantâneo ao utilizador por ingrediente).
- Fabricante com 100 INT (+50% potency) e talent Apothecary (+125% potency; pode vir de Alchemist's Hat).
- Máximo 3 cópias por ingrediente / 5 ingredientes total.

**Fórmula da wiki**: `(3×2%+2×2%)×(1+0.5+1.25) = +27.5%` de bónus NOMINAL.

**Patch 15/11/2025**: «Damage potion increase/decrease efficiency nerfed by 50%». Como a wiki em 2026 continua a apresentar +2% por ingrediente, mas não confirma se o nerf já está refletido na tabela, distinguir:
- Cenário **A:** +27,5% nominal é a leitura final **se** a tabela já incorporar o patch.
- Cenário **B:** +13,75% nominal **se** o nerf ainda deve ser aplicado sobre a receita.
- **Não afirmar** que o live buff é definitivamente 27.5% nem 13.75%; validação in-game pendente.

O fabricante e o lutador **não têm obrigatoriamente de ser o mesmo jogador**, mas a obtenção/transferência e restrições de modo devem ser confirmadas. Para cozinhar a 100 INT é suficiente 100 INT na pessoa que fabrica, não obrigatoriamente na build ofensiva, caso consigas utilizar a poção produzida.

## Uma poção ativa, não stacking
- Efeito base **15 segundos**.
- Só **um efeito de poção ativo** no alvo; aplicar outro limpa o anterior.
- Beber: **2.35 segundos**, sem sprint/roll; tomar dano interrompe e gasta a poção.
- **Potion Sickness**: 20 segundos; beber novamente durante esse cooldown não dá efeito.
- Não aplicar Chain Reaction (×1.4) a poção bebida: esse talent só ativa numa **poção atirada** sobre alguém já com efeito, e ainda reduz efeitos positivos atirados em 80%.

## Muito importante: autodano vs Perfect Flash
Browncap tem **-4 dano instantâneo** por ingrediente; dois produzem `-8×2.75=−22 HP` após o multiplier de potency (sem mitigação especial). **Não confundir** esta componente com o nerf do buff de dano: são efeitos diferentes.

Partindo de 400 HP em cheio: `(400−22)/400=94.5%`; **Perfect Flash (>95%) fica desligado** até curar. Acima de 440 HP máximo e com 22 HP autodano, HP restante é >95% (ou com cura/mitigação).

## Comparação — sem debuff prévio no alvo

**Modelagem:** Eclipse Kick L5 `B=115` e scaling 2.75, Ether Barrage L5 `B=48` e scaling 1.65; 100 atributo, 6 Songchant, fórmula atual rate=0.075. Dano bruto antes de resistência/PEN. `Ring of Casters (5%) + Isshin's Ring (15% em curta distância) + Enchant Food (5%) = +25%` de pool nominal; `Perfect Flash +25%` exige HP >95%, distância curta.

| Cenário | Pool nominal | Multiplicador cap | Eclipse Kick | Ether Barrage (6 instâncias) |
|---|---:|---:|---:|---:|
| Sem buff | 0% | ×1.00000 | 160,86 | 59,48 |
| Apenas 3 equipamentos/comida | +25% | ×1.25000 | 201,07 | 74,35 |
| Anteriores + Potion B (+13,75%) | +38,75% | ×1.31875 | 212,13 | 78,44 |
| Anteriores + Potion A (+27,5%) | +52,5% | ×1.38750 | 223,19 | 82,53 |
| Anteriores + Perfect Flash, sem poção | +50% | ×1.37500 | 221,18 | 81,79 |
| Anteriores + Perfect Flash + Potion B | +63,75% | ×1.44375 | 232,24 | 85,88 |
| Anteriores + Perfect Flash + Potion A | +77,5% | ×1.50000 | **241,28** | **89,23** |
| Anteriores + Perfect Flash + Dark Hours + Potion B | +78,75% | ×1.50000 | **241,28** | **89,23** |

**Avisos:** (a) combiná-los exige simultaneidade e legalidade dos buffs; (b) aplicação de cada modificador ao pool comum é hipótese modelada; (c) se a poção te deixar a <=95% HP, o cenário de Perfect Flash não é aplicável; (d) Dark Hours requer noite/Depths e Shadowcast — **não funciona no Ether Barrage**, logo a última linha é exclusiva de Eclipse Kick; (e) Ether Barrage tem 6 ticks, não é single-impact.

## Alternativa de desempenho
Para one-tap num único impacto, a poção **não cria um multiplicador extra fora do hard cap**. Com o pool saturado, Eclipse Kick continua em **241,28 bruto** antes de resistências. Se já tens a combinação para atingir ×1.5, a poção não dá dano adicional.

### Como verificar o valor realmente ativo no patch
Testar Eclipse Kick L5 em um alvo 0 armor/sem talentos de resistência: (1) sem potion, (2) com Strengthening 100 INT+Apothecary sem outros buffs; com base `160.85625`, os modelos predizem ~182,97 para 13,75% ou ~203,08 para 27,5%. Repetir para rejeitar variação, parry e resistência. O resultado só identifica o multiplicador se o jogo o aplicar integralmente fora de outra limitação.

Não efetuei o ensaio no servidor; os números são simulação.
