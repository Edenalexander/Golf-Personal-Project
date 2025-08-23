# Golf Performance Analysis
## Overview
This project analyses personal golf performance data over a series of 21 games. Using Python and data visualisation tools, the project explores trends in scores, improvement over time, and the impact of environmental factors such as temperature and wind speed.

## Data 
- Date of each round.
- Hole by hole performance.
- Enviromental factors such as temperature and wind speed.

## Analysis & Visualisations
The project includes 7 key visualisations:
1. **Average "Over Par" on Each Hole**

![Average Over Par on Each Hole](Visuals/Avg_Over_Par_on_each_hole.png)

*Shows which holes had higher or lower scores on average.*

2. **First 10 Games Performance**

![First 10 Games Performance](Visuals/First_10_Games.png)

*Highlights early trends in overall performance.*

3. **Last 11 Games Performance**

![Last 11 Games Performance](Visuals/Last_11_Games.png)  

*Shows recent performance trends.*

4. **Hole Improvements**

![Hole Improvements](Visuals/Hole_Improvements.png)  

*Tracks performance improvement on each hole over time.*
  
5. **Over Par vs Game Number**

![Over Par vs Game Number](Visuals/Over_Par_vs_Game_Number.png) 

*Linear regression and trend analysis over all games.*
 
6. **Temperature vs. Performance**

![Temperature vs Performance](Visuals/Temp_vs_Performance.png) 

*Explores potential environmental effects of temperature.*
 
7. **Wind Speed vs. Performance**

![Wind Speed vs Performance](Visuals/Wind_Speed_vs_Performance.png)  

*Examines the impact of wind on scores.*

## Key Insights
- **Overall Performance Trends:** Across all games, there is a clear improvement in scores, with a significant downward trend in “Over Par” over time (p = 0.001). Rejecting the null hypothesis, this indicates steady performance improvement throughout the dataset.  

- **Hole-Specific Patterns:** Analysis by hole shows some holes consistently scoring higher and others lower. Hole 2 and hole 18 show considerably worse scores on average compared to other holes. This may be due to challenges on these holes that lead to penalties, such as lost balls, which negatively impact overall scores.

- **Environmental Effects:** Environmental factors were tested for their impact on performance. Temperature (p = 0.282) and wind speed (p = 0.082) showed no statistically significant effect on scores, suggesting these variables did not meaningfully influence performance in this dataset.  

- **Early vs. Late Game Comparison:** Comparing the first 10 games with the last 11 games shows visible improvement on several holes, particularly Hole 10 and Hole 16, supporting the overall trend of performance enhancement. On the other hand, performance on Hole 4 declined in recent games. This appears to be related to reduced practice with the 5-iron, which affects accuracy on the second shot.

- **Visualization Insights:** Scatterplots, regression lines, and LOWESS smoothing illustrate trends over time and across variables. The visualizations clearly show which factors influenced performance and which did not, making patterns in the data easy to interpret. 

## Tools & Technologies
- **Python** (pandas, numpy, matplotlib, statsmodels, seaborn)  
- **Visual Studio Code** for analysis  
- **Git & GitHub** for version control and project sharing

## How to Use
1. Clone the repository:  
   ```bash
   git clone https://github.com/Edenalexander/Golf-Personal-Project.git
