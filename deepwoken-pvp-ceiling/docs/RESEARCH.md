> **Nota de auditoria (14/11/2026):** Songchant é **+7,5% por ponto**, NÃO 6,5% (que pertence a Proficiency). Fórmula confirmada em [Traits](https://deepwoken.fandom.com/wiki/Traits) e [Mantras](https://deepwoken.fandom.com/wiki/Mantras). Tabela «sem buffs / com cap»: [AUDIT_2026-11-14.md](AUDIT_2026-11-14.md). **27,5% de poção é apenas receita teórica: nerf de eficácia de poções de dano em 2025, efeito líquido não comprovado.**

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

**Oath Mantras:** a fórmula geral de oath tem fator Songchant adicional **(1 + 0.02 × Songchant)**. Os mantras específicos podem ter scaling zero. NÃO usar este fator em Ceaseless/Tornado.

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
| Enchant food | +5% | Sim | Candied Fruit / Fish Omelette, por Reinforced Hunger |
| Power food | +5% M1 | **Não** | Outro tipo de comida |
| Brain food | Nocturnal proc 10→15 | Apenas proc da gema | Substitui Enchant, não simultâneo |
| Ring of Casters | +5% mantra / -5% melee | Sim | Não presumir stack de vários anéis iguais |
| Perfect Flash | +25% mantra perto e acima de 95% HP | Sim | Confirmar canal do cap e distância |
| Taunt | Alvo recebe +20% | Sim | Explicitamente sujeito ao cap, alvo revida +10% |
| Strengthening potion | Até +27.5% condicional | Geral, a confirmar prática | 3 Plumfruit + 2 Browncap; 100 INT + Apothecary **no fabricante** |
| Tough Love | +5% mantra em Charmed | Sim | +10% para outras formas de dano; requer Charm |
| Flame Within | +10% geral | Potencialmente | Dá self-burn; testar compatibilidade com Perfect Flash |
| Inhale / Fan the Flames | até +10% no próximo Gale **ou Flamecharm se tiver Fan the Flames** | Gale ou Fire condicional | Requer armazenar mantra Gale (nível 5 para +10%); verificar cap |
| Last Resort | +5% abaixo de 25% HP | Condicional | **Incompatível** com Perfect Flash >95% HP |
| Reinforce | +5% ou +2.5% weapon | **Não** | Wiki declara weapon attacks only |
| Overflowing Dam | até +10% basic | **Não** | Wiki declara basic attacks only |
| Shade Devour | +20 a 25% **weapon** | **Não** | Não atribuir aos mantras seguintes |
| Nocturnal Gem | +10 damage fixo, ou +15 com Brain food | Proc separado | NÃO afetado por damage modifiers normais, tem counterplay |

Possíveis talentos/sinergias que exigem verificação de canal, condições ou patch: Charged Return, Lose Your Mind, Nullifying Clarity, Matador, Rush Hour, Spinning Swordsman, After Cut, Galebreathe Inhale, Charismatic Cast, Inspiration, status elemental, PEN específico, Flame Within. O site Deepwoken Builder lista várias destas fontes, mas **não garante** que todas atuem em mantras. Não adicionamos valores de uma categoria de armas à de mantras.

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
| Ceaseless Slashes | 20 | 310,05 | **576,34** | 5 cortes base documentados; mais cortes não auditados |
| Tornado | 12 | 177,60 | **372,63** | 12 ticks documentados; After Cut não incluído |
| Scarlet Cyclone + Multiplying | 30? | 156,00 | **327,31** | **NÃO CONFIRMADO** 3 projéteis atingirem o MESMO alvo |
| Scarlet Cyclone padrão | 10 | 130,00 | **272,76** | Contagem documentada |
| Tornado Kick | 4 | 112,00 | **234,99** | Abertura tem de acertar |
| Metal Rain | ~23 | 110,40 | **231,63** | Estimativa, Bleed adicional não incluído |
| Shadow Meteor | 3 | 105,00 | **220,30** | Acertar os três |
| Scarlet Cannon | 17 | 51,00 | **107,00** | 17 ticks |
| Shadow Assault Blast | 20 | 62,80 | **131,76** | Somente <=40% HP, NÃO com Perfect Flash |

Para Scarlet Cyclone + Multiplying Spark cada projétil passa a **5,2** de base por tick em vez de 13. Mesmo se TODOS acertarem, 3×10×5,2=156; não são 3× o dano da versão normal (390).

O mantra Ceaseless Slashes pode superar 5 cortes quando se recupera Ether durante a execução/timing, segundo a Wiki, mas não há comprovação de um máximo finito ou de que se repita com um jogador a aguentar sem escapar. Isto impede afirmar um recorde absoluto.

## 4B. Efeitos de dano base que ultrapassam o cap

- **Arcwarder Enhance, com Arc Suit ativo:** **Arc Wave +25% base** e **Arc Beam +50% base**, exclusivamente. Dano base entra ANTES de scaling e modifiers, não se reduz no soft/hard cap comum. [Oath: Arcwarder](https://deepwoken.fandom.com/wiki/Oath%3A_Arcwarder)
- **Shock Trooper Specialist:** com **TODAS as peças equipadas**, +15% base em **Grand Javelin, Thunder Kick, Electro Carve, Astral Wind, Champion's Whirlthrow, Gale Lunge**. O capacete isolado não dá o bónus de base; o set também pode causar Stormcall Strikes quando atinge limiar. [Hybrid Abilities](https://deepwoken.fandom.com/wiki/Hybrid_Abilities)
- **Oath/Monster Songchant** +2% por ponto, *além* da fórmula de scaling apropriada. **Ceaseless Slashes e Tornado NÃO são mantras Oath.** [Mantras](https://deepwoken.fandom.com/wiki/Mantras)
- **Fan the Flames:** Inhale (Mantra Wind armazenado) potencia **Flamecharm** com +(nível×2)% até 10%, além de transferir modificadores do mantra inalado. [Hybrid Abilities](https://deepwoken.fandom.com/wiki/Hybrid_Abilities)

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
1. Confrontar wiki vs changelogs posteriores a julho de 2026, sobretudo Ceaseless e variantes adicionadas.
2. Validar cap do Perfect Flash por testes com e sem Taunt/food/potion.
3. Confirmar compatibilidade de food, poções e pre-buffs em Chime e Overworld.
4. Medir se Ceaseless com Ether regen consegue >5 cortes quantas vezes; limites internos de casts.
5. Testar os três cyclones sobre um jogador; retorno Reversal (hit novo ou ignora mesmo alvo?).
6. Medir procs de After Cut e da gema, incluindo cooldown por mantra e por hit.
7. Integrar subset de builds legais para filtros de oath, element requirements e mantras equipáveis.
8. Definir resistência do alvo e PEN com fórmula real; só depois comparar dano HP de uma rotação e DPS.
