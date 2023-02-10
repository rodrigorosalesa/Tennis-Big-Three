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
- [Q4: Who performs better under preasure?](README.md#q4-who-performs-better-under-preasure)
- [Q5: How does their serve varies according to the surface played?](README.md#q5-how-does-their-serve-varies-according-to-the-surface-played)
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

<img src="images\q2_titles_count.png" alt="Titles count through the years" width="1200"/>

As we observed, Roger Federer is the one with most titles among the 3, with 103, being the only active player that has surpassed the barrier of 100 titles won. In a single season Federer holds the record for a male player with most titles with 12 in the season of 2006. Novak Djokovik is in a close second with 94 titles and Nadal is last with 92. 

As we mentioned Grand Slams tournaments are the most prestigious event in the year, the titles that all tennis players cherish the most. Since July of 2003 there has been 79 Gran Slams held, the Big Three has won 64 of them, in other words they have won 81% of the Grand Slams in the last 20 years. In the graph below we can see Federer has a total of 20, being more dominant in Wimbledon with 8 titles, Nadal and Djokovic are tight with 22, 14 titles for the Spaniard in Roland Garros and 10 titles for the Serbian in the Australian Open, those torunaments are their best performing Slams.

<img src="images\q2_grand_slams_count.png" alt="GS count through the years" width="1200"/>

<br>

## Q3: BEST SINGLE SEASON OF THE BIG THREE
During their career the has been moments when these athletes played in a godly manner, appearing to be invincible, on this question I want to showcase the best season of their carers and analysing the most important stats. To have a comparison, in the table below is represented the win-lose ratio of their career. 

<p align="center">
<img src="images\q3_WL_ratio_career.png" alt="Career´s Win-Lose Ratio" width="300"/>
</p>

<br>

**Rafael Nadal 2013 Season**

<img src="images\q3_nadal.png" alt="Nadal's 2013 season" width="1200"/>

Considerer one of the greatest comeback seasons of all time, as the previous year Nadal was not playing since June due a to an injury, he even missed the first Grand Slam of the year, the Australian Open. He finished the year as no. 1 player of the world, 11 titles, including 2 Grand Slams (Roland Garros and US Open) and 4 M1000. 

He had a a win-lose ratio of 92.5% (9.88% over the WL Ratio oh his career), winning 81 matches out of 88. He lost only two matches during the clay season and won 6 clay titles. He accumulated a 22 winning streak during a the clay court season, ending with a lost in first round in Wimbledon against Steve Darcis, being the only lost he had before a semifinals during the year. 

<p align="center">
<img src="images\q3_nadal_matches.png" alt="Nadal´s 2013 matches" width="500"/>
</p>

<br>

**Novak Djokovik 2015 Season**

<img src="images\q3_djokovic.png" alt="Djokovic's 2015 season" width="1200"/>

Djokovic began a dominance in profesional tennis in the season of 2011, but his greatest season came in 2015, considered one of the greatest seasons of all time. He reached the final of all of the Grand Slam, winning 3 Australian Open, Wimbledon and US Open. The serbian was the no. 1 player of the world for the whole year, won 6 M1000 tournament and reaching the final in 8 of them and even claiming the ATP World Tour Finals, an event that only the 8 best player of the year can enter. 

Djokovik ended his 2015 season with 11 tittles won, a Win-Lose Ratio of 93.26% (9.64% over the WL Ratio oh his career), winning 83 matches out of 89. He finished the season with a record of of 4-0 againts Nadal, even beating him at the quarter finals of Roland Garros, and a record of 5-3 versus Federer, including his victory in the Wimbledon Final. He lost to Ivo Karlovik in the quarter finals of the Qatar Open, making this tournament the only onw in which he did´t got at least to the final. Novak Djokovic is considered the player of the 2010s decade.

<p align="center">
<img src="images\q3_djokovic_matches.png" alt="Djokovic´s 2015 matches" width="500"/>
</p>

<br>

**Roger Federer 2006 Season**

<img src="images\q3_federer.png" alt="Federer's 2006 season" width="1200"/>

During the end of 2003 until 2007 we saw the Swiss dominated professional tennis like no one has done it before and probably no player would ever do it again. Roger´s 2006 season is considered by many tennis experts the best tennis season of the open era. He maintained the no. 1 position in the ATP ranking for the whole year and finished no. 1 for a third year in a row, he won 3 Grand Slams, the Australian Open, Wimbledon for a fourth time in a row and the US Open for a third time in a row; he lost in the Final of Roland Garros to the king of clay. 

In addition to that, Federer reached the finals in 6 M100 finals from the 7 that he entered and won 4 on hard courts and loosing 2 in clay. He won the ATP World Tour Finals. He finished the year with a record of 12 titles, becoming the male player with most titles in a single season. He ended the season with a Win-Lose Ratio of 94.85% (12.07 over the WL Ratio oh his career), winning 92 matches out of 97, he finished the year with a 27 winning streak that continued in the 2007 season to win 41 matches in a row. He reached the finals of every tournament he played but the Cincinnati Masters where he lost to Andy Murray in the second round. Roger Federer is considered the tennis player of the 2000s decade.

<p align="center">
<img src="images\q3_federer_matches.png" alt="Federer´s 2006 matches" width="500"/>
</p>

<br>

## Q4: WHO PERFORMS BETTER UNDER PREASURE?
Write here

<br>

## Q5: HOW DOES THEIR SERVE VARIES ACCORDING TO THE SURFACE PLAYED?
The serve is considered the most important shot in tennis because it sets the tone for the entire point. A good serve gives a player a significant advantage and allows them to dictate the pace of the rally. If a player can consistently serve well, they can control the game, put pressure on their opponent, and create opportunities for easy points. Additionally, serving well can also help a player maintain their confidence and mental edge throughout the match.

In the table below we can observed the career most importat statistics to analyze a good serve for the Big Three.
- Ratio First Serve In: ratio of 1st serves in and 1st serves made.
$% 1st serve ratio = \frac{# of 1st serves in}{# of first serves produced}$

There are four different tennis surfaces in which profesional torunaments are played, Hard, Caly, Grass and Carpet; deppending on the surface the ball will bounce in different speeds and high altering completely how the the opponent on the other side of the court will fell the coming serve. 

- Hard Courts: most common type of surface composed on aspahlt and concrete with a coatin of pait or acrylic on top. This type of surfaces have lower energy assumption than clay courts, making the ball move faster. This benefits aggresive players that like to play from the baseline. 
- Clay courts: clay courts are made of a coarse mixture made from brick. Clay courts is the slowest surface for ball speed, making it easier to return a high speed serve. In the countrary if offers high bounce so players that hit with a lot of top-spin are highly favourable; moreover points tend to last longer. 
- Grass Courts: a grass surface consists of short-cut grass on a tighly packed soil, being the less common surface today due to the high cost of maintenance. Grass is the fastest surface and also offers the lowest bounce, making rallies short and fast, this type of courts 

<br>

## FINAL THOUGHTS
Write here

<br>

## REFERENCES
Write here

