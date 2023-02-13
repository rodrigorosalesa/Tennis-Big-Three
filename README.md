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
Tennis is one of the most popular sports globally, acording to the Internationa Tennis Federation is calculated that 87 million of people played the white sport in 2022, which is an increment of 4.5% from 2018, more than 578,000 courts ara available worldwide in over 115,000 facilities. 

As tennis is growing as a sport globally, the professional tennis circuit is growing accordingly, more people are interested to follow it and the accessibility to watch events happening around the world is better than ever. 

There have been many great tennis players throughout the years, but none of them have shaped the sport as the Big Three. Roger Federer, Rafael Nadal, and Novak Djokovic are considered the greatest players that ever hold a tennis racket.

In this project, I aim to analyze their performance and compare their statistics to gain insights into their careers. By examining data on their matches, rankings, and Grand Slam victories, I hope to showcase the careers of these players and what has made them some of the greatest athletes to ever grace the court.

<br>

## GUIDING QUESTIONS
1. How did Federer, Nadal and Djokovic moved in the rankings throughout the years?
2. Best single season of the big three
3. Titles breakdown
4. Who has a better serve?
5. Who performs better under preasure?

<br>

## DATASET
To answer my guiding questions, I am using data of every match played in the profesional tennis circuit from 2020 to 2022. Data was obtained from a Git repository named [Tennis ATP](https://github.com/JeffSackmann/tennis_atp) that was created and is currently maintained by Jeff Sackman. Important statistics of every match can be observed, alongside information about the tournaments, ranking and more.

<br>

## METHODOLOGY
1. Problem Definition
2. Data Cleaning and Wrangling
3. Feature Engineering
4. Deep Analysis
5. Data Visualization
6. Conclusions

<br>

## TOOLS
- Python: used for data cleaning, wrangling, and exploration
    - [Pandas](https://pandas.pydata.org/)
    - [Numpy](https://numpy.org/)
    - [Matplotlib](https://matplotlib.org/)
    - [Seaborn](https://seaborn.pydata.org/)
- Tableau: used to create visualziations to show my findings
- GitHub: used for version control of my work and publish my project using GitHub Pages.

<br>

## Q1: HOW DID FEDERER, NADAL AND DJOKOVIC MOVED IN THE RANKINGS THROUGHOUT THE YEARS?
The ATP (Association of Tennis Professionals) Ranking is the system used by the men's professional tennis circuit to determine the top players in the world based on their performance in tournaments. The rankings are updated on a weekly basis and are an important factor in determining player seeding for tournaments and special exempts. 

On the following visualization we can see how Federer, Nadal and Djokovik moved in the ATP ranking throughout their careers.

<img src="images\q1_ranking.png" alt="Ranking" width="900"/> 

Since 2004 these 3 players have dominated the ATP ranking. Below, I am showing the end year ranking as the goal to every tennis player is finish the year at the top of the rankings, meaning there was no other player better than them in the season. Federer and Nadal have 5 year-end no. 1, the Swiss in 2004, 2005, 2006, 2007, and 2009, and the Spaniard in 2008, 2010, 2013, 2017, and 2019; however, Djokovic has the record with 7 during the years of 2011, 2012, 2014, 2015, 2018, 2020, and 2021. Only 2 years since 2004 other tennis player apart from the big three have finished the year as no. 1, in 2016 Andy Murray and in 2022 Carlos Alcaraz.

Moreover, in the following table we can appreciate the brutal dominance of the Big Three at the top of the rankings; since 2004 until January 30th of 2023, 941 weeks have passed in which the Big Three have combined 802 weeks at the top of the ranking, this means that three players have shared the title of “best player of the world” more than 88% percent of the time. It is important to state that despite Djokovic hold the record for more weeks as no. 1, Federer holds the record for more consecutive weeks at the top with 237 starting February 2nd of 2004 and ended 17 August 2008 after loosing the Wimbledon final with Nadal.

<p align="center">
<img src="images\q1_weeks.png" alt="Weeks as no. 1" width="400"/>
</p>

<br>

## Q2: TITLES BREAKDOWN
Winning an ATP tournament is the greatest accomplishment when entering to professional tennis, winning tournaments means more ATP points and more money, Grand slams give the most money and points; for more information on how the point allocation works for every round won on all tournament levels you can click [here](https://www.atptour.com/en/rankings/rankings-faq). Tournaments in the ATP circuit are divided by level:
- _Grand Slam_: 4 tournaments per year. Winner gets 2000 ATP points. 
- _Master Finals_: 1 tournament per year and only the best 8 players of the year can enter. Winner gets 1500 ATP points. 
- _Master 1000_: 9 tournaments per year. Winner gets 1000 ATP points. 
- _Event 500_: 11 tournaments per year. Winner gets 500 ATP points. 
- _Event 250_: 42 tournaments per year. Winner gets 250 ATP points. 

On average a player outside the top 100 of the world plays around 20 – 30 tournaments in a year, as a player starts earning more points and move up the rankings they can be more selective on which tournaments to play; a player inside the top 20 only plays on average 15 – 20 tournaments to be on a good shape and get the best results in the important tournaments of the year. 

Here below we can see a line graph that represents the breakdown of the titles of the Big Three during their careers. 

<img src="images\q2_titles_count.png" alt="Titles count through the years" width="1200"/>

As we observed, Roger Federer is the one with most titles among the 3, with 103, being the only active player that has surpassed the barrier of 100 titles won. Federer holds the record for a male player with most titles with 12 in a single season (2006). Novak Djokovik is in a close second with 94 titles and Nadal is last with 92. 

To understand better what big tournaments (Grand Slams, M1000 and World Tour Finals) the Big Three has won over the years I created the following Tree Map, subdivided by tournament and player; the size and color are represented with the number of matches won in the event, first number is the number of wins and second is the number is the number of titles won. Nadal has dominated the French Open since his first title in 2005 at the age of 19. Federer has more wins in the rest of the Grand Slams, Wimbledon with 106, Australian Open with 103 and US Open with 91, Djokovik just won his 10th Australina Open last month. 

<img src="images\q2_titles_tree.png" alt="Big titles and matches won distribution" width="1200"/>

As we mentioned Grand Slams tournaments are the most prestigious events in the year, the titles that all tennis players cherish the most. Since July of 2003 there has been 79 Gran Slams held, the Big Three has won 64 of them, in other words they have won 81% of the Grand Slams in the last 20 years. In the graph below we can see Federer has a total of 20, being more dominant in Wimbledon with 8 titles, Nadal and Djokovic are tight with 22, 14 titles for the Spaniard in Roland Garros and 10 titles for the Serbian in the Australian Open.

<img src="images\q2_grand_slams_count.png" alt="GS count through the years" width="1200"/>

<br>

## Q3: BEST SINGLE SEASON OF THE BIG THREE
During their career the has been moments when these athletes played in a godly manner, appearing to be invincible. In this question I want to showcase the best season of their carers and analysing the most important stats. To have a comparison, in the table below is represented the win-lose ratio of their career. 

<p align="center">
<img src="images\q3_WL_ratio_career.png" alt="Career´s Win-Lose Ratio" width="300"/>
</p>

<br>

**Rafael Nadal 2013 Season**

<img src="images\q3_nadal.png" alt="Nadal's 2013 season" width="1200"/>

Considerer one of the greatest comeback seasons of all time, as the previous year Nadal did not played since June due a to an injury, he missed the first Grand Slam of the year, the Australian Open. He finished the year as no. 1 player of the world, 11 titles, including 2 Grand Slams (Roland Garros and US Open) and 4 M1000. 

He had a a win-lose ratio of 92.5% (9.88% over the WL Ratio oh his career), winning 81 matches out of 88. He lost only two matches, won 6 clay titles and accumulated a 22 winning streak during a the clay court season, ending with a lost in first round in Wimbledon against Steve Darcis, being the only lost he had before a semifinals during the year. 

<p align="center">
<img src="images\q3_nadal_matches.png" alt="Nadal´s 2013 matches" width="500"/>
</p>

<br>

**Novak Djokovik 2015 Season**

<img src="images\q3_djokovic.png" alt="Djokovic's 2015 season" width="1200"/>

Djokovic began a dominance in profesional tennis in the season of 2011, but his greatest season came in 2015, considered one of the greatest seasons of all time. He reached the final of all of the Grand Slam and won 3, Australian Open, Wimbledon and US Open. The serbian was the no. 1 player of the world for the whole year, won 6 M1000 tournament and reached the final in 8 of them. At the end of the year he claimed the ATP World Tour Finals, an event that only the 8 best player of the year can enter. 

Djokovic ended his 2015 season with 11 tittles, a Win-Lose Ratio of 93.26% (9.64% over the WL Ratio oh his career), winning 83 matches out of 89. He finished the season with a record of of 4-0 againts Nadal, even beating him at the quarter finals of Roland Garros, and a record of 5-3 versus Federer, including his victory in the Wimbledon Final. He lost to Ivo Karlovik in the quarter finals of the Qatar Open, making this tournament the only in which he didn´t get at least to the final. Novak Djokovic is considered the player of the 2010-2020 decade.

<p align="center">
<img src="images\q3_djokovic_matches.png" alt="Djokovic´s 2015 matches" width="500"/>
</p>

<br>

**Roger Federer 2006 Season**

<img src="images\q3_federer.png" alt="Federer's 2006 season" width="1200"/>

During the end of 2003 until mid 2008 we saw the Swiss dominated professional tennis like no one has done it before and probably no player would ever do it again. Roger´s 2006 season is considered by many tennis experts the best tennis season of the open era. He maintained the no. 1 position in the ATP ranking for the whole year and finished no. 1 for a third year in a row, he won 3 Grand Slams, the Australian Open, Wimbledon for a fourth time in a row and the US Open for a third time in a row; he lost in the Final of Roland Garros to the Nadal. 

In addition to that, Federer reached the finals in 6 M100 finals from the 7 that he entered and won 4 on hard courts and loosing 2 in clay. He won the ATP World Tour Finals. He finished the year with a record of 12 titles, becoming the male player with most titles in a single season. He ended the season with a Win-Lose Ratio of 94.85% (12.07 over the WL Ratio oh his career), winning 92 matches out of 97, he finished the year with a 27 winning streak that continued in the 2007 season, reaching 41 matches won in a row. He reached the finals of every tournament he played but the Cincinnati Masters where he lost to Andy Murray in the second round. Roger Federer is considered the tennis player of the 2000-2010 decade.

<p align="center">
<img src="images\q3_federer_matches.png" alt="Federer´s 2006 matches" width="500"/>
</p>

<br>

## Q4: WHO PERFORMS BETTER UNDER PREASURE?
In tennis, pressure points are moments in a match when the outcome could significantly impact the outcome of the match. These moments often arise in critical situations, such as break points, set points, or match points. 

On the following graph we can observe three important statistics, break points saved ratio at serving, break points conversion ratio at return, and preassure points won ratio, which is an average of the previous two; this last one is the best representation on how good a player when stakes are higher.

Nadal has the highest score for pressure points won ratio with a 54.09%, Djokovic in close second and Federer is last. One of the key aspects to win important points, apart from the tennis skills, is the mental strength of the players and the ability to manage nerves, Rafael Nadal is considered by many the greatest fighter on tour and possesses one of the toughest mentalities on tour.

<p align="center">
<img src="images\q5_preassure_points.png" alt="Preassure points ratio" width="550"/>
</p>

<br>

## Q5: HOW DOES THEIR SERVE STATISTICS VARIES ACCORDING TO THE SURFACE PLAYED?
The serve is considered the most important shot in tennis because it sets the tone for the entire point. A good serve gives a player a significant advantage and allows them to dictate the pace of the rally. If a player can consistently serve well, they can control the game and put constant pressure on their opponents. 

Below the most importat statistics to analyze a good serve:

<p align="center">
<img src="images\q5_formulas.png" alt="Serving Statistics" width="500"/>
</p>

On the graph below we see that Nadal has the higher 1st serve ratio with 67.74% and Federer the best 2nd serve ratio with 93.87%. Having more successful serves do not warranty you more points, you need to assure that is a good enough shot to help you dictate the point. According to Andrea Cazzaro, the best way to understand the influence of the serve in a match is to compute the probability of winning a point when the serve is successful, which is calculated with the probability of winning a point after a successful 1st serve and the probability of winning a point after a successful 2nd serve (formula described above). 

As we can see Federer has a better chance to win a point after having a successful serve with 70.78%, Djokovic is second with 68.53% and Nadal last with 68.35%. Despite Federer not having the fastest serve with an average of 200 km/hr he is probably one of the best ones at varying effect and direction making the return very hard for his opponents.

<p align="center">
<img src="images\q5_serve_all.png" alt="Serve Statistics" width="600"/>
</p>

<br>

To understand how the court surfaces affect their serve, we need to understand first, the difference of each surface. There are three tennis surfaces in which professional tournaments are played, hard, clay, and grass; depending on the surface the ball will bounce at different speeds and altitude, altering completely how the opponent will feel the coming serve.

- _Hard Courts_: most common type of surface composed of asphalt and concrete with a coating of paint or acrylic on top. This type of surface has lower energy assumption than clay courts, making the ball move faster. This benefits aggressive players that like to play from the baseline. 
- _Clay courts_: clay courts are made of a coarse mixture made from brick. Clay courts is the slowest surface, making it easier to return a high speed serve. In the contrary if offers high bounce so players that hit with lots of topspin are highly favourable; moreover, points tend to last longer. 
- _Grass Courts_: consists of short-cut grass on a tightly packed soil, being the less common surface today due to the high cost of maintenance. Grass is the fastest surface and offers the lowest bounce, making rallies short and fast, this type of courts is beneficial to great servers. 

<img src="images\q5_serve_surfaces.png" alt="Serve Statistics by surface played" width="700"/>

As we were expecting, probability of winning a point after a successful serve varies in accordance to the speed of the surface, for clay in decreases between 2-3% and for grass it incremented between 1 and 3%, Roger Federer maintained the status as the best server of the three regardless of the court surface.

As important as the serve is, there are other important factors that can alter the outcome of the match, for example the physical condition of the player, ground strokes, volleys, mentally strength, etc. I included the W-L Ratio of their career by surface to understand how good players are in each surface. Nadal has a 91.05% W-L ratio on Clay and he posses the longest win streak in a single surface with 81 matches won between 2005 and 2007. Djokovic best W-L ratio is on hard courts with 84.71% and Federer on Grass with 87.78%.

<br>

## FINAL THOUGHTS
The Big Three conformed by Roger Federer, Rafael Nadal, and Novak Djokovic, has dominated the tennis professional circuit for over two decades, winning everything that is to win, breaking every record and producing many amazing matches. The debate for who is the Greatest Off All Time will not stop, what these legends have done is beyond measure, numbers can not fully encompass the extent of their legacy nor can describe how they inspired millions of people. 

One thing is certain, they have redefined what it means to be a tennis player and the impact they have had on and off the court will be eternal. 

<br>

## REFERENCES
- ATP Tour. (2020). ATP Rankings FAQ. Obtained from ATP Rankings: https://www.atptour.com/en/rankings/rankings-faq
- Cazzaro, A. (July 5th, 2020). Understanding the Importance of First Serve in Tennis with Data Analysis. Obtained from Medium: https://towardsdatascience.com/understanding-the-importance-of-first-serve-in-tennis-with-data-analysis-4829ab088d36
- Master Class. (7 de June de 2021). Explore the 4 Types of Tennis Courts, From Clay to Synthetic. Obtained from Master Class - Articles: https://www.masterclass.com/articles/types-of-tennis-courts
- Musa, M. (January 18th, 2023). How Many People Play Tennis in the World? Obtained from Tennis Racket Ball: https://tennisracketball.com/guide/how-many-people-play-tennis/?gclid=CjwKCAiAuaKfBhBtEiwAht6H75-ooTLgJnCaocXWVKTXLVdRglm7pzgHph4fibmf1pOlx_T2OXg1hhoCnJMQAvD_BwE



