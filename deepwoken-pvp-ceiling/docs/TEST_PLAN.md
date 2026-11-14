# Plano de ensaios in-game — necessário para provar o teto real

**Não executado**: esta investigação é documental e tem cálculos reprodutíveis, mas sem acesso ao servidor do jogo.

## A. Regras do ensaio
- Fazer numa sessão **PvP privada** e em ambiente legal, sem exploits.
- Usar dois jogadores com números de HP documentados e armaduras/atributos conhecidos.
- Fixar Power 20, Songchant 6, atributo (por ex. Light 100), nível 5, sem equipamento com procs ao início.
- Gravar **vídeo 60 FPS**, log do HP inicial e final e cada tick separadamente, se possível.
- Repetir cada ensaio várias vezes para descartar latência, distância, redutores e bugs.
- Testar separadamente **Chime vs Overworld**: certas regras de consumíveis ou invulnerabilidades podem variar; não assumir.

## B. Cap e posição dos multiplicadores
1. Baseline: mantra sem buffs, alvo a 0% de resistência.
2. Só Ring of Casters (+5%), medir razão.
3. Só Enchant food (+5%), medir razão.
4. Só Perfect Flash (+25%) com **HP >95%** e curta distância; repetir a longa distância.
5. Só Strengthening (+27.5%) preparad[a] com 3 Plumfruit + 2 Browncap, 100 INT e Apothecary; medir efeito em M1 e mantra.
6. Só Taunt (+20% recebido), documentar duração/side effect.
7. Combinar os anteriores e medir danos com +25%, +50%, +75%, +82.5% brutos; testar exatamente a redução de metade após soft cap e teto +50%.
8. Variar Perfect Flash **quando o cap já está saturado**. Se a potência aumentar, parte de Perfect Flash pode não pertencer à mesma categoria.
9. Verificar se o dano instantâneo ao beber poção deixa HP <95%, e se cura/mitigação reativa Perfect Flash.
10. Testar Talents adicionais com cap saturado: Tough Love, Flame Within, Lose Your Mind, After Cut, outros.
11. Não testar Reinforce/Overflowing Dam como fontes de mantra em builds máximas: wiki já os restringe a arma; podem ser usados como controlo negativo.

## C. Hits, Sparks, gemas e ambiente
1. Ceaseless Slashes: contar hits principais e ticks secundários, e se todos atingem mesmo jogador.
2. Repetir com Ether regen (Sticky Bun, regen gear, efeitos pertinentes) / timing / Lenses, contabilizando duração e quando termina por Ether.
3. Scarlet Cyclone Multiplying Spark: anotar quantos dos 30 ticks potenciais atingem o mesmo jogador; repetir com Reversal Spark, incluindo no retorno.
4. Metal Rain com e sem Logstones: contar ticks exatos; não assumir que 23 aumenta linearmente com duração.
5. Tornado + After Cut: distinguir +5% por proc de +5% no dano direto, capturar impacto de target resistance.
6. Nocturnal Gem: +10 ou +15 com Brain food, procs por cast vs por hit, intervalo entre procs; testar se buff de dano normal altera proc (deveria não alterar).
7. Testar impactos de Everchanging Aegis e tipos distintos de resistência em sequência de ticks.

## D. Registar prova
Guardar nesta matriz:
```
Patch | Modo | Mantra | Lv | Songchant | Atributo | HP caster | HP alvo antes/depois
Food | Potion receita e brewer INT | Ring | Talents ativos | Taunt/Charm | Resistências
Spark/Gem/Mantra mods | Hits observados | Hits bloqueados | Dano por tick | Total | Vídeo
```

Critério de sucesso: só chamar de **ceiling máximo possível** se houver (i) auditoria de todos os candidatos relevantes, (ii) combinação legal de stats/talents/oath/slots, (iii) confirmação no jogo de **todos** os hits e buffs, (iv) comparação ao melhor concorrente e (v) verificação de patches recentes.
