# AntSimulation
Simulate colonies of ants in a virtual environment

## Simulation Explanation

https://user-images.githubusercontent.com/49039023/205646454-b2728509-8446-44e8-bcc7-398618fc3f5a.mp4

In the simulation video, the purple points are the colonies, the green are the food and the red are the ants. The pheromones track is shown by the little spots on the path, ants release the pheromones as they return to their colony with food.
When food is already consumed, the ants remain on persuit of it because it still containes pheromones, when the pheromones eventually evaporate, then they all start searching for more food, that is what causes those "explosions" of ants where there was previously food. This phenomenon occurs frequently with ants although with lower level of syncronization, that could be fixed with a random probability associated when switching state from following pheromones and searching for food, for the context of this project that was not necessary.

## Setup Environment

Create virtual environment
```bash
python3 -m venv venv
```

Source virtual environment
```bash
source venv/bin/activate
```

Install requirements
```bash
pip3 install -r requirements.txt
```

## How to run

```bash
python3 src/main.py
```
