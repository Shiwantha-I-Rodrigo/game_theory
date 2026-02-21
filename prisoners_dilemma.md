# STRATEGIES THAT WERE TESTED

1. Always Defect (ALLD)
    * **Rule:**
        1. Always betray.

2. Always Cooperate (ALLC)
    * **Rule:**
        1. Always stay silent (cooperate).

3. Tit for Tat (TFT)
    **Rule:**
        1. Start by cooperating.
        2. Then copy your opponent’s previous move.

4. Grim Trigger
    * **Rule:**
        1. Cooperate until opponent defects once.
        2. then defect forever.

5. Pavlov (Win-Stay, Lose-Shift)
    * **Rule:**
        1 If last move gave good payoff → repeat it
        2 If bad payoff → switch action

6. Generous Tit for Tat
    * **Rule:**
        1. Like Tit for Tat, but occasionally forgives defection.

7. Suspicious Tit for Tat
    * **Rule:**
        1. Start by defecting.
        2. then copy opponent.

8. Random Strategy
    * **Rule:**
        1. Cooperate or defect randomly.

9. Adaptive / Learning / AI Strategies
    * **Rule:**
        1. Adjust behavior based on opponent patterns over time.

10. Zero-Determinant (Extortion) Strategies
    * **Rule:**
        1. forces opponent into lower payoff ratio.

```
Zero-Determinant (Extortion) Strategies Explanation

--> Establish a payoff structure

|                       | Firm B Cooperates | Firm B Defects |
| --------------------- | ----------------- | -------------- |
| **Firm A Cooperates** | 3 , 3             | 0 , 5          |
| **Firm A Defects**    | 5 , 0             | 1 , 1          |

* 3 = mutual cooperation (stable profits)
* 5 = temptation payoff (defect while other is cooperating)
* 1 = punishment (both defect)
* 0 = sucker payoff
 
--> Firm A adopts a Zero-Determinant extortion strategy.

Firm A cooperates in a way that enforces a specific payoff relationship:

    Sa - 1 = 2(Sb - 1)

This means Firm A corporate only after a certain threashold of profit gained.

* If Firm B constantly defects, both firms remain near the punishment payoff, and both gains equally.
* If Firm B chooses to cooperate more often, it earns more than it would by defecting. However, Firm A earns even more than Firm B and maintains a consistent advantage.
* This creates pressure on Firm B to cooperate, SINCE cooperation yields better returns than constant defection - a 1 versus occasional higher payoffs like 3.
* Firm A carefully adjusts its cooperation probabilities to preserve this enforced ratio, cooperating just enough to keep cooperation attractive for Firm B, but not enough to allow Firm B to surpass it.

! THIS STRATEGY ONLY WORKS IF THE OPPONENT IS RATIONAL
```

---
Versus Predictions

| Algo \ Opponent   | ALLC  | ALLD  | TFT   | Grim  | Pav   | ZD-Ext        | ZD-Gen    |
| -                 | -     | -     | -     | -     | -     | -             | -         |
| **ALLC**          | High= | B     | High= | High= | High= | B             | High=     |
| **ALLD**          | A     | Low=  | Low=  | Low=  | Low=  | Low=          | Low=      |
| **TFT**           | High= | Low=  | High= | High= | High= | B (slightly)  | High=     |
| **Grim**          | High= | Low=  | High= | High= | High= | B (slightly)  | High=     |
| **Pav**           | High= | Low=  | High= | High= | High= | B (slightly)  | High=     |
| **ZD-Ext**        | A     | Low=  | A     | A     | A     | Low=          | A (slight)|
| **ZD-Gen**        | High= | Low=  | High= | High= | High= | B (slight)    | High=     |

Legend:

+ **A** --> row strategy tends to earn more
+ **B** --> column strategy tends to earn more
+ **Low=** --> both get low (near punishment)
+ **High=** --> both get high (near mutual cooperation)

Strategies included:

+ ALLC = Always Cooperate
+ ALLD = Always Defect
+ TFT = Tit for Tat
+ Grim = Grim Trigger
+ Pav = Pavlov (Win-Stay Lose-Shift)
+ ZD-Ext = Zero-Detinant Extortion (χ > 1)
+ D-Gen = Generous Zero-Determinant
