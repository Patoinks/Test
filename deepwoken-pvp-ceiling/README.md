# Deepwoken PvP — teto matemático de dano de Mantras

**Status:** auditoria reprodutível, NÃO uma prova de recorde global. Atualizado em 2026-11-14.

## Âmbito
Investigar máximo de dano PvP num único mantra, todos os hits por cast, procs e buffs possíveis legalmente. Distinguir dano bruto (sem resistência), dano efetivo contra jogador, burst de rotação, Chime e Overworld. A wiki consultada pode estar desatualizada.


> **ALERTA DE FONTES:** o Deepwoken Builder apresenta Ceaseless Slashes L5 com **290 de base**, enquanto a decomposição antiga por ticks da Fandom usada aqui dá **310,05**. Logo, **576,34 NÃO está confirmado na versão atual**. Ver [cenários PvP fiáveis](docs/RELIABLE_PVP.md) para valores mais defensáveis e o plano de verificação.

> **AUDITORIA DE 14/11/2026 — [ler antes de usar os números](docs/AUDIT_2026-11-14.md):** o valor **0,075 por Songchant é correto** (+7,5% por ponto). O valor **0,065 (+6,5%)** aplica-se a **Proficiency** das armas. A [wiki de Mantras](https://deepwoken.fandom.com/wiki/Mantras) confirma a fórmula. Valores da tabela são cenários de *todos os hits*, não dano PvP garantido.
>
> **Poções:** os 27,5% são apenas resultado do modelo de receita da wiki. Um [patch em novembro de 2025](https://deepwoken.fandom.com/wiki/Version_History/2025) reduziu a eficácia de poções de dano em 50%; desconhece-se se a tabela atual já incorpora a redução. Dano real de poção requer teste.
>
> **Damage sources fora do cap:** [Arcwarder Enhance](https://deepwoken.fandom.com/wiki/Oath%3A_Arcwarder) altera o *dano base* de Arc Beam (+50%) e Arc Wave (+25%). [Shock Trooper Specialist](https://deepwoken.fandom.com/wiki/Hybrid_Abilities) dá +15% de base a seis mantras específicos apenas com o **conjunto completo**. [Fan the Flames](https://deepwoken.fandom.com/wiki/Hybrid_Abilities) permite aplicar Inhale a Flamecharm.
>
> Comparação [**sem buffs vs pool comum saturado ×1,50**](docs/AUDIT_2026-11-14.md).

## Resultados documentados
- Hard cap PvP para a categoria dos damage modifiers: **1,50×**; soft cap **1,25×**. Segundo a calculadora Deepwoken Builder, o excesso após +25% conta a metade até +50%. Assim, +75% nominal basta para saturar essa categoria (fontes: Version History 2025; deepwoken.co/builder).
- **Comida Enchant:** Candied Fruit/Fish Omelette, **+5% dano de mantras**. Buffs alimentares de tipos diferentes substituem-se, não somar Enchant e Brain.
- **Ring of Casters:** **+5% dano de mantras**, -5% dano de arma.
- **Perfect Flash:** **+25% dano de mantras** acima de 95% de HP, reduz com distância (10% a longa distância). Confirmar se entra no pool geral de modifiers em todos os modos.
- **Poção Strengthening:** 3 Plumfruits + 2 Browncaps, ingredientes +2% dano cada: **10% base**, com 100 INT no FABRICANTE + Apothecary soma potência 50%+125%, ou seja **27,5%**. Só pode existir um efeito de poção de cada vez no alvo; há efeitos secundários, incluindo dano ao beber e perda de regen.
- **Taunt:** alvo recebe +20% de dano, mas é tratado como modificador e está sujeito ao cap. Ele causa +10% de dano ao caster.
- **Tough Love:** a versão para mantras é **+5%** (e não +10%).
- **Reinforce** e **Overflowing Dam:** aumentam **ataques de arma**, NÃO mantras. Não incluí-los erradamente.
- **Ceaseless Slashes** nível 5: 5 cortes iniciais [20,25,30,35,40] + 15 ticks de 10,67 = 310,05 base no cenário de 20 hits. Com 100 Light e 6 Songchant: 310,05×1,23925×1,5 ≈ **576,34** dano bruto. Maior número de cortes pode acontecer com recuperação de Ether; sem limite certificado, não declarar ceiling absoluto.

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

A soma acima é **hipótese de categoria comum e de sobreposição temporal**, não garante que todos os buffs sejam calculados da mesma forma pelo servidor. Se Perfect Flash for aplicado num canal separado, o resultado muda. Exigir teste no jogo.

## Executar
```bash
python3 deepwoken-pvp-ceiling/src/ceiling.py
python3 -m unittest discover -s deepwoken-pvp-ceiling/tests -v
```

## Ficheiros
- `src/ceiling.py`: fórmulas, tabelas e candidatos.
- `tests/test_ceiling.py`: testes regressivos.
- `docs/RESEARCH.md`: evidências, nuances e restrições.
- `docs/TEST_PLAN.md`: ensaios que faltam.
- `SOURCES.md`: fontes diretas.

**Limitação:** não foi feita auditoria exaustiva dos mantras e patches de novembro de 2026; um valor de calculadora não prova maximum matematicamente alcançável.

Este projeto não tem afiliação oficial com Deepwoken.
