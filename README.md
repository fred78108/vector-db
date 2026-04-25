# Vector Databases

This repository supports a blog post at [chaos by derf](https://chaosbyderf.com) (Upcoming post).

## Project goal
I want to understand the trade-offs between a few different vector databases.


## Status
*This is a work in progress*. Once I'm done with the coding and blog post I'll finalize this page.

## Documents
I used Claude to create 20 documents with a goal of diverse topics:


| File | Topic |
|---|---|
| ancient_rome.md | Rise and fall of the Roman Empire |
| black_holes.md | Astrophysics of black holes |
| chess_history.md | History and culture of chess |
| coffee_origins.md | Origins and global culture of coffee |
| coral_reefs.md | Coral reef ecosystems and bleaching |
| fermentation_science.md | Science and applications of fermentation |
| honey_bees.md | Honey bee biology and ecology |
| japanese_tea_ceremony.md | Chado ritual, history, and philosophy |
| jazz_history.md | History of jazz from New Orleans to fusion |
| machine_learning_basics.md | Intro to ML concepts |
| marathon_running.md | History, physiology, and training |
| ocean_currents.md | Ocean circulation and climate |
| origin_of_languages.md | Linguistic diversity and language origins |
| plate_tectonics.md | Theory of plate tectonics |
| rainforest_ecology.md | Tropical rainforest structure and threats |
| sourdough_bread.md | Sourdough baking process |
| stoic_philosophy.md | Stoicism and its modern revival |
| the_internet.md | History of the internet and Web |
| the_printing_press.md | Gutenberg and its cultural impact |
| the_silk_road.md | Ancient trade routes and cultural exchange |
| volcanoes.md | Volcanic geology and eruption types |


## Organization
I am trying to create simple scripts/notebooks (as needed) to explore the concepts without getting bogged down in code organization. The trade-off is that functions may be replicated across scripts.

- **chroma.py** a simple hello world using the 20 markdown files with chromadb.
- **docs** a set of 20 markdown files (see Documents section).
- **roll.py** doing everything by hand. Use this when looking to understand vector databases and do a bit of your own creation.
 