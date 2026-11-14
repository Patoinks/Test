# Deepwoken: auditoria de patches e meta de dano PvP — 14/11/2026

> **Escopo:** ênfase em mantras, dano máximo por cast, burst, buffs, resistências e confiabilidade em PvP. Este relatório NÃO é uma leitura completa das mensagens do Discord oficial: o arquivo de `Version History/2026` publicamente indexado só chega a **31/05/2026**. Não foi possível autenticar, linha por linha, todos os hotfixes de junho–novembro. O Builder mais atual (consultado em 14/11) confirma novas skills; fontes secundárias relatam release de 31/10 mas não substituem patch oficial.

## 1. Estado dos dados e confiabilidade

| Verificação | Fonte | O que podemos afirmar |
|---|---|---|
| Histórico até 31/05/2026 | [Fandom 2026](https://deepwoken.fandom.com/wiki/Version_History/2026) | Alterações explícitas, mas atualização do site está atrasada face a novembro |
| Novos híbridos | [Deepwoken Builder: Exotherm](https://deepwoken.co/builder?id=OFOy9VMS) / [Alloyblood](https://deepwoken.co/builder?id=S9m4DEaN) | Seis mantras constam de builds públicas recentes; números de dano completos não estão confirmados |
| Patch de Hallowtide 31/10 | [Artigo comunitário 12/11](https://deepwokengame.wiki/updates/hallowtide-2026/) | Datas e mecânicas reportadas; ainda não confrontadas com patch oficial |
| Publicações Roblox novembro | [Bloxstatus](https://bloxstatus.com/games/deepwoken/updates/) | Observou novas versões em 02, 06 e 09/11; **não há changelog nestes timestamps** |
| Meta / win rate | Não disponível | **Não há amostra de Chime Elo ou win rates para declarar S-tier confirmado** |

## 2. Novidades mais relevantes para PvP mantras

### Outubro–novembro: novas hipóteses de meta (existência apoiada por Builder)

**Bloodrend + Flamecharm: Sanguine Blaze / Exotherm**
- `Cauterize`: grab, aplica Black Blood ou detona o que já existe
- `Combustion Tide`: puxa inimigos e explode, com ignição de Black Blood
- `Flashfusion`: híbrido existente no Builder; comportamento/ticks e base L5 a confirmar
- Fontes secundárias descrevem Black Blood com até três stacks, slow e anti-heal; Flamecharm não-Burn detonaria stacks. **Não inserir valores de detonação sem fonte numérica**.
- **Hipótese de meta:** burst de 2–3 casts com detonação, anti-heal e potencial procs em cadeia. Não é recorde matemático confirmado de um cast.

**Bloodrend + Ironsing: Composite Path Alloyblood**
- `Infused Slash`: duas adagas de plasma
- `Spinning Serum`: lança de plasma com rotação; **prioridade para auditar todos os hits por jogador**
- `Rising Plasma`: greataxe de plasma
- Fonte secundária indica path com `50 Bloodrend + 50 Ironsing` e plasma buildup. Builder confirma que Rising Plasma requer estes atributos e talento Composite Path.
- **Hipótese de meta:** multi-hit + controle + procs; desconhecido se ultrapassa Ceaseless ou Tornado no máximo de um cast.

### Alterações 2026 confirmadas pelo histórico (até maio)

**Alterações que mudam cálculos ou builds:**
1. `All Oaths` recebem **+5% de PEN em todas as fontes de dano**, substituindo o antigo bónus específico associado a Thresher Claws. **Não contar o antigo bónus mais o novo como se fossem aditivos independentes**.
2. `Gourmet` aumenta **50% a duração dos buffs de comida**. Não aumenta a potência da comida Enchant; melhora a manutenção do +5% de dano de mantra em Overworld.
3. `Shadow Meteor` teve **redução de dano**. O valor 105 de base usado no dataset anterior está sob suspeita e deve ser reconsultado.
4. `Scarlet Cyclone` tornou-se **2-star**. Isso, por si só, não permite inferir novos ticks ou multiplicadores.
5. **Ring stacking corrigido**. Não modelar mais de um Ring of Casters equivalente sem verificação.
6. **Rending Impact aplicado a mantras** foi corrigido como bug. Não o utilizar como +dano de mantras.
7. **Arcwarder** perdeu o bónus geral de dano quando usa o suit, embora o efeito específico em mantras Arcwarder permaneça. Não generalizar `Enhance` a mantras não-Arcwarder.
8. **Equipment sem enchant ocupa slots de enchant**: pode limitar efeitos de equipamento adicionais numa build com Specialist full set.
9. `Ceaseless Slashes` recebeu correção de bug de mobilidade. Não confirma aumento de dano.
10. O histórico menciona aumento de scaling de Songchant, mas a fórmula consultável em [Traits](https://deepwoken.fandom.com/wiki/Traits) continua a indicar **+7,5% de scaling por ponto** (não +6,5%, que é Proficiency).

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

- Que os seis híbridos foram exatamente lançados a 31/10 (data apenas corroborada por publicação secundária).
- Qualquer percentagem exata de dano da detonação Black Blood ou de Plasma.
- Se o último patch Roblox contém nerf de Gale.
- Que o máximo de Ceaseless ou Tornado é atingível contra humano ativo.
- Que já foram analisadas *todas* as notas oficiais semanais até 14/11/2026.

**Estado final:** base de dados antiga requer refresh; forte candidato a mudança de meta de combos é Sanguine Blaze e de multi-hit é Alloyblood; teto matemático e nova build dominante não demonstrados.
