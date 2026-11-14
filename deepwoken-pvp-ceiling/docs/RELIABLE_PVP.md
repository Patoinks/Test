> **Auditoria adicional:** ver [AUDIT_2026-11-14.md](AUDIT_2026-11-14.md). Songchant **7,5%** por ponto (Proficiency é 6,5%). O soft cap/hard cap PvP está no patch de 2025; a redução acima do soft cap foi documentada em 2023. As estimativas de resistência deste documento são ilustrativas, não médias confirmadas.

# Dano PvP **fiável**: hard cap vs aplicação real

> **Atualização: 2026-11-14.** Estes são cenários demonstrativos segundo o modelo de caps comum, **não recordes máximos de HP damage**. Um cast pode ser parried, blocked, dodged ou parcialmente evitado.

## A distinção essencial
- **Cap legal do pool de damage modifiers em PvP**: ×1.50 (+50% efetivo).
- **Buffs estáveis de baixo custo**: Ring of Casters (+5%) + Enchant food (+5%) = +10% nominal, **×1.10** enquanto a comida está ativa.
- **Opener dependente de estado**: acrescentar Perfect Flash perto do alvo com mais de 95% HP (+25%): +35% bruto ⇒ depois da soft cap +25% ⇒ +30% efetivo, **×1.30**.
- **Opener com Taunt aplicado**: soma +20% bruto (alvo afetado): +55% nominal ⇒ +40% efetivo, **×1.40**.
- **Hard cap** exige pelo menos **+75% de modifiers brutos da categoria** para chegar a ×1.50: depende de mais buffs de estado (poção, Taunt, talentos, etc.), nem sempre disponíveis numa luta comum.
- **Não confundir**: +35% bruto NÃO dá ×1.35 neste modelo, porque o excedente acima de +25% é contado a metade.

| Cenário | Bruto nominal da categoria | Multiplicador efetivo |
|---|---:|---:|
| Ring apenas (sem buffs alimentares) | +5% | ×1.05 |
| Ring + Enchant food | +10% | ×1.10 |
| Ring + food + Perfect Flash | +35% | ×1.30 |
| Ring + food + Perfect Flash + Taunt | +55% | ×1.40 |
| Hard cap saturado | +75% ou mais | ×1.50 |

Ring permanece equipado até trocado; o Enchant food tem duração e pode acabar. Perfect Flash >95% HP (diminui com distância) não é **permanente**; Taunt exige acertar uma mantra de suporte e não passa parry, block e dodge.

## Exemplo com um único hit: Table Flip nível 5

Wiki: 60 base damage, 1.65 Strength scaling. Admitir 100 Strength, 6 Songchant, e **25% resistência líquida pós-PEN no adversário** (hipótese para calcular, não média comprovada da comunidade).

`D_pre-buff = 60 × [1 + (1.65/1000) × 100 × (1 + 6 × 0.075)] = 74.355`

| Buffs | Pré-resistência | Após 25% resistência líquida (hipótese) |
|---|---:|---:|
| Ring+food (×1.10) | 81.79 | **61.34** |
| Ring+food+Perfect Flash (×1.30) | 96.66 | **72.50** |
| +Taunt no alvo (×1.40) | 104.10 | **78.07** |
| Saturar hard cap (×1.50) | 111.53 | **83.65** |

Este valor pressupõe que o golpe **acerta sem defesa**. Dano em barra de vida é imprevisível sem resistência, armadura e mecânicas do alvo.

## Correcção de confiança do projeto

Há **divergência de fontes** no dano base de Ceaseless Slashes L5:
- No dataset local estimámos **310.05** por 5 cortes [20,25,30,35,40] e 15 ticks ×10.67, fonte Fandom.
- O [Deepwoken Builder](https://deepwoken.co/builder?id=j6Ot2RWw) apresenta **290** de base no nível 5, atualizado recentemente.
- **Até reconciliação do patch e dos ticks**, o valor de **576.34** de Ceaseless Slashes em simulações anteriores **NÃO é uma base de máxima confiança** e muito menos dano fiável num PvP.
- Dados históricos de [Version History 2025](https://deepwoken.fandom.com/wiki/Version_History/2025) indicam nerf de Ceaseless Slashes; a tabela antiga pode estar desfasada.

## O próximo passo correto
1. Verificar patch e valor de cada tick de Ceaseless no jogo.
2. Testar Table Flip (1 hit) e um combo de 2–3 hits sob as mesmas condições.
3. Medir buff cap e resistência efetiva em alvo com HP conhecido.
4. Só então afirmar limite real de dano total de cast consistentemente aplicável.

### Fontes
- [2025 PvP damage modifier caps](https://deepwoken.fandom.com/wiki/Version_History/2025)
- [Scaling/mantra formula](https://deepwoken.fandom.com/wiki/Mantras)
- [Food buffs](https://deepwoken.fandom.com/wiki/Food)
- [Ring of Casters](https://deepwoken.fandom.com/wiki/Ring_of_Casters)
- [Perfect Flash](https://deepwoken.fandom.com/wiki/Attribute_Trees)
- [Taunt e Table Flip](https://deepwoken.fandom.com/wiki/Attunement-less)
- [Ceaseless L5 em Deepwoken Builder](https://deepwoken.co/builder?id=j6Ot2RWw)
