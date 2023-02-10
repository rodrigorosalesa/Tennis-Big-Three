# Tennis Insights: Analyzing the career of the BIG THREE
### By [Rodrigo Rosales Alvarez](https://www.linkedin.com/in/rodrigorosalesalvarez/)

<img src="images\big_three.png" alt="Tennis Big 3: Roger Federer, Rafael Nadal, Novak Djokovic" width="650"/>

<br> <br> 

## TABLE OF CONTENTS
- [Introduction](README.md#introduction)
- [Guiding Questions](README.md#guiding-questions)
- [Dataset](README.md#dataset)
- [Methodology](README.md#methodology)
- [Tools](README.md#tools)
- [Q1: How did Federer, Nadal and Djokovic moved in the rankings throughout the years?](README.md#q1-how-did-federer-nadal-and-djokovic-moved-in-the-rankings-throughout-the-years)
- [Q2: Titles breakdown](README.md#q3-titles-breakdown)
- [Q3: Best single season of the big three](README.md#q2-best-single-season-of-the-big-three)
- [Q4: Who has a better serve?](README.md#q4-who-has-better-serve)
- [Q5: Who performs better under preasure?](README.md#q5-who-performs-better-under-preasure)
- [Final Thoughts](README.md#final-thoughts)
- [References](README.md#references)

<br> <br>

## INTRODUCTION
There have been many great tennis players throughout the years, but none of them have shaped the sport as the Big Three. Roger Federer, Rafael Nadal, and Novak Djokovic are considered the greatest players that ever hold a tennis racket.

In this project, I aim to analyze their performance and compare their statistics to gain insights into their careers, their strengths, and weaknesses. By examining data on their matches, rankings, and Grand Slam victories, I hope to shed light on the careers of these tennis legends and what has made them some of the greatest players to ever grace the court.

<br>

## GUIDING QUESTIONS
1. How did Federer, Nadal and Djokovic moved in the rankings throughout the years?
2. Best single season of the big three
3. Titles breakdown
4. Who has a better serve?
5. Who performs better under preasure?

<br>

## DATASET
To answer my guiding questions, I am using data of every match played in the profesional tennis circuit. Data was obtained from a Git repository named [Tennis ATP](https://github.com/JeffSackmann/tennis_atp) that was created and is currently maintained by Jeff Sackman. Important statistics of every match can be observed, alongside information about the tournaments, ranking and more.

<br>

## METHODOLOGY
1. Problem Definition
2. Data Cleaning
    - Null values
    - Type of columns
    - Column names
3. Feature Engineering
4. Deep Analysis
5. Data Visualization
6. Conclusions

<br>

## TOOLS
- Python: used for data cleaning, data wrangling and exploration of data
    - [Pandas](https://pandas.pydata.org/)
    - [Numpy](https://numpy.org/)
    - [Matplotlib](https://matplotlib.org/)
    - [Seaborn](https://seaborn.pydata.org/)
- Tableau: used to create final visualziations to showcase my findings
- GitHub: used to have a version control of my work and publish my project using GitHub Pages.

<br>

## Q1: HOW DID FEDERER, NADAL AND DJOKOVIC MOVED IN THE RANKINGS THROUGHOUT THE YEARS?
The ATP (Association of Tennis Professionals) Ranking is the system used by the men's professional tennis tour to determine the top players in the world based on their performance in tournaments. The rankings are updated on a weekly basis, and are an important factor in determining player seeding for tournaments, as well as in decisions regarding wildcard entries, direct acceptances, and special exempts. 

On the following visualization we are able to see how Roger, Rafael and Novak moved in the ATP ranking throughout their careers.

<img src="images\q1_ranking.png" alt="Ranking" width="900"/> 

As we can see, since 2004 these 3 players have dominated the ATP ranking. On the image above I am showing the end year ranking as the goal to every tennis player is finish the year at the top of the rankings, meaning there was no other player better than them in the season. Federer has finished 5 year-end no. 1 (2004, 2005, 2006, 2007, 2009), Nadal has 5 (2008, 2010, 2013, 2017, 2019) and Djokovic has the record with 7 (2011, 2012, 2014, 2015, 2018, 2020, 2021). Only 2 years since 2004 other tennis player apart from the big three have finished the year as no. 1, in 2016 Andy Murray and in 2022 Carlos Alcaraz.

Moreover, in the following table we can appreciate even more the dominance of the Big Three; since 2004 until January 30th of 2023, 941 have passed in which the Big Three have combined 802 week at the top of the ranking, this means that three players have shared the title of “best player of the world” more than 88% percent of the time. It is important to state that despite Djokovic hold the record for more weeks as no. 1, Federer holds the record for more consecutive weeks at the top with 237 starting February 2nd of 2004 and ended 17 August 2008 after loosing the Wimbledon final with Nadal.

<p align="center">
<img src="images\q1_weeks.png" alt="Weeks as no. 1" width="400"/>
</p>

<br>

## Q2: TITLES BREAKDOWN
Winning an ATP tournament is the greatest accomplishment when entering to the professional level in tennis, winning tournaments mean more points for the ranking system and more money earned. Tournaments in the ATP circuit are divided by level:
- Grand Slam: 4 tournam-ents per year. This type of events gives the most money and the most points, the winner wins 2000 ATP points. 
- Master Finals: 1 tournament per year and only the best 8 players throughout the year can enter. This tournament gives 1500 ATP points to the winner. 
- Master 1000: 9 tournaments per year. The winner gets 1000 ATP points. 
- Event 500: 11 tournaments per year. The winner gets 500 ATP points. 
- Event 250: 42 tournaments per year. The winner gets 250 ATP points. 

On average a player outside the top 100 of the world plays around 20 – 30 tournaments in a year, as a player start earning more points and move up the rankings they can be more selected on which tournaments to play; a player inside the top 20 only plays on average 15 – 20 tournaments to be on a good shape and get the best results in the best tournaments of the year. 

Here below we can see a line graph that represents the breakdown of the titles of the Big Three during their careers. 

<img src="images\q3_titles_count.png" alt="Titles count through the years" width="900"/>

As we observed, Roger Federer is the one with most titles among the 3, with 103, being the only active player that has surpassed the barrier of 100 titles won. In a single season Federer holds the record for a male player with most titles with 12 in the season of 2006. Novak Djokovik is in a close second with 94 titles and Nadal is last with 92. 

As we mentioned Grand Slams tournaments are the most prestigious event in the year, the titles that all tennis players cherish the most. Since July of 2003 there has been 79 Gran Slams held, the Big Three has won 64 of them, in other words they have won 81% of the Grand Slams in the last 20 years. In the graph below we can see Federer has a total of 20, being more dominant in Wimbledon with 8 titles, Nadal and Djokovic are tight with 22, 14 titles for the Spaniard in Roland Garros and 10 titles for the Serbian in the Australian Open, those torunaments are their best performing Slams.

<img src="images\q3_grand_slams_count.png.png" alt="Titles count through the years" width="900"/>

<br>

## Q3: BEST SINGLE SEASON OF THE BIG THREE
Write here

<br>

## Q4: WHO HAS BETTER SERVE?
Write here

<br>

## Q5: WHO PERFORMS BETTER UNDER PREASURE?
Write here

<br>

## FINAL THOUGHTS
Write here

<br>

## REFERENCES
Write here

