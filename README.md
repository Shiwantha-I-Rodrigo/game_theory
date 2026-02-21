# 🧠 Game Theory Experiments

This project implements and simulates classic **game theory and behavioral economics experiments** using Python.

The goal is to compare strategic behavior, equilibrium predictions and emergent outcomes across multiple well-known games.

## 📌 Implemented Games

* **Prisoner’s Dilemma (Iterated)** – Repeated cooperation or betrayal between two players where mutual cooperation benefits both, but temptation to defect is constant.
* **Ultimatum Game** – One player proposes a split of money, and the other can accept or reject it, risking both getting nothing.
* **Dictator Game** – One player unilaterally decides how to split a sum, with the other having no say.
* **Trust / Investment Game** – Player A sends money to Player B, which can grow; B can return some, testing trust and reciprocity.
* **Public Goods Game** – Multiple players contribute to a shared pot that benefits all, even free-riders who contribute nothing.
* **Stag Hunt** – Cooperation yields high reward if mutual, but hunting alone risks a smaller guaranteed payoff.
* **Chicken (Hawk–Dove)** – Two players drive toward conflict; the first to yield avoids disaster, but both lose if neither swerves.
* **Matching Pennies** – Players choose heads or tails; one wins if choices match, the other if they differ, creating pure conflict.
* **Battle of the Sexes** – Two players prefer different outcomes but gain from coordinating, forcing compromise.
* **Centipede Game** – Players alternate choices to continue or take the growing pot, testing trust versus short-term gain.
* **Traveler’s Dilemma** – Two players independently claim a value; the lower claim wins, incentivizing undercutting despite mutual benefit from higher claims.

## 🎯 Project Goals

* Compare rational equilibrium vs observed behavior
* Test classical strategies
* Simulate evolutionary dynamics
* Analyze cooperation, fairness and competition
* Run tournaments between strategies
* Visualize payoff distributions

## ⚙️ Installation

```
git clone `repo`
cd game_theory
pip install -r requirements.txt
```

## 📈 Metrics Tracked

* Average payoff
* Cooperation rate
* Nash equilibrium detection
* Evolutionary stability
* Payoff variance
* Convergence speed

## 🧪 Research Questions

* When does cooperation emerge?
* Are extortion strategies evolutionarily stable?
* How does noise affect equilibrium?
* Does fairness outperform rational greed?
* How do populations evolve under replicator dynamics?

## 📚 References

Classic foundations from:

* Axelrod tournaments
* Evolutionary game theory
* Behavioral economics experiments

## 🧩 Why This Project?

Game theory explains:

* Market competition
* Political negotiations
* Social cooperation
* Conflict and war
* Fairness and punishment

This repository serves as a sandbox for experimenting with strategic interaction.

## 📜 License

Copyright 2026 Shiwantha-I-Rodrigo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---