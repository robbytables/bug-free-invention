<!--
title: Intro to Visualization
type: lesson
duration: "00:40"
creator: Emma Freeman [originating from David Yerrington's python-data-viz-principles lesson]
-->

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Visualization

<!--


## Overview
This lesson introduces students to the concept of data visualization - what it is, why it's important, the components of a great data visualization. Near the end, there's a section to help students understand when they would use a bar chart, pie chart, scatter plot, or histogram.

## Important Notes or Prerequisites

The next lesson is on Pandas and actually building these graphs. This lesson is all about understanding the different types of graphs and their use cases.


## Learning Objectives
*After this lesson, students will be able to...*

- Describe why data visualization is important.
- Identify the characteristics of a great data visualization.
- Identify when you would use a bar chart, pie chart, scatter plot, and histogram.

## Duration
45 minutes.

---

## Suggested Agenda

| Time | Activity | Purpose |
| --- | --- | --- |
| 0:00 - 0:03 | Welcome |
| 0:03 - 0:08  | Data Visualization |
| 0:08 - 0:30  | Types of Plots |
| 0:30 - 0:42  | Visualization Tips |
| 0:42 - 0:45  | Summary |

## Materials and Preparation
- Send out the link to the presentation slides to students.
- No out of the ordinary prep needed

## Differentiation and Extensions
- There is a lot to say about best practices for data visualization! Feel free to add slides of your own.

## In Class: Materials
- Projector
- Internet connection
- Jupyter Notebooks
- Python3
-->


---

## Lesson Objectives
*After this lesson, you will be able to...*

* Describe why data visualization is important.
* Identify the characteristics of a great data visualization.
* Identify when you would use a bar chart, pie chart, scatter plot, and histogram.

<aside class="notes">
Teaching Tips:

- Introduce topic and learning objectives
</aside>

---


## Check Out This Graph - Made with Python!

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/flight-chart.jpg)

*Source: u/dx034 on Reddit*

<aside class="notes">
Teaching tips:

- Note that it seems intricate but was created with code.
</aside>

---

## Check Out the Data Set

This is only 1/3 of it!

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/flight-data-set.png)


<aside class="notes">
Teaching tips:

- Note how much more difficult it is to read and make sense out of

**Teaching Tips**:

- Raw data contains a lot of information but isn't digestible or understandable until it is presented in a synthesized way.
- The first chart allowed us to compare, draw inferences, and have a clear take-away
</aside>


---

## So What Is Data Visualization?

- A quick, easy way to convey concepts.
- We can use charts or graphs to visualize large amounts of complex data.


<aside class="notes">
Teaching Tips:

- Encourage discussion here.
- "Data Visualization" can be a confusing term, so to get them comfortable with the idea that it can be simplified to mean "Charts and Graphs"

**Teaching Tips**:

- "Because of the way the human brain processes information, charts or graphs that visualize large amounts of complex data are easier to understand than spreadsheets or reports.  Data visualization is a quick, easy way to convey concepts in a universal  manner — and you can experiment with different scenarios by making slight adjustments."
</aside>

---

## Discussion: Why Use Data Visualization?

Where have you seen helpful charts, graphs, or other visualizations?

Where could this be useful?


<aside class="notes">
**Teaching Tips**:

- With your table, discuss some of the ways you have used or enjoyed data visualization. Why do you think data visualization is useful? Why is it important?
</aside>


---

## Chart Types

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/chart_types.png)


<aside class="notes">
Teaching tips:

- Explain that we'll go over many of these in detail throughout the slides
- Do frequent checks for understanding by asking students for examples of cases where they would use each type of plot, and example of good or bad things they've seen with the plots.
- As you introduce new chart types, contrast it with the previous ones - give examples of when you'd use one vs the other.
- Bring up good (or bad!) practices as you see them in the examples.
</aside>


---

## The Bar Chart

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/zombie-chart.png)

<aside class="notes">
**Teaching Tips**:

- Before moving to the next slide ask, when would you use a bar chart?
</aside>

---


## The Bar Chart

- Effective for numerical data in categories.
- Easy to compare information.
- Most common type of graph.
- Quickly reveal highs and lows.

![](https://www2.le.ac.uk/offices/ld/images/study-guide-images/numeracy/bar1.gif)


<aside class="notes">
**Teaching Tips**:

- Bar charts are one of the most common ways of visualizing data. Why? Because they make it easy to compare information, revealing highs and lows quickly. Bar charts are most effective when you have numerical data that splits neatly into different categories.
</aside>


---


## The Pie Chart

![](http://static.twentytwowords.com/wp-content/uploads/Pie-Chart-39.png)

<aside class="notes">
**Teaching Tips**:

- Before moving to the next slide ask, when would you use a pie chart?
</aside>

---


## The Pie Chart


Effective for proportions or percentages.

![](https://www.csisun.com/wp-content/uploads/2012/07/solarhotwaterpiechart.jpg)


<aside class="notes">
**Teaching Tips**:

- Pie charts are the most commonly misused chart type.
- Pie charts show the relationship of parts out of whole.
- If you want to compare data, leave it to bars or stacked bars. If your viewer has to work to translate pie wedges into relevant data or compare pie charts to one another, the key points you're trying to convey might go unnoticed.
- Why do they work well with proportions or percentages? Because those two types of information show the relationship of parts to a whole.
</aside>

---

## Pie Chart vs. Bar Chart


![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/stephen-few-pie-vs-bar.png)


<aside class="notes">
**Teaching Tips**:

- Before moving to the next slide ask, when would you use a pie chart instead of a bar chart?
</aside>

---


## The Scatter Plot


- Effective for trends, concentrations, and outliers.
- Useful to see what you want to investigate further.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/scatter%20plot.png)


<aside class="notes">
**Teaching Tips**:

- Scatter plots are a great way to give you a sense of trends, concentrations, and outliers, and are great to use while exploring your data. This will provide a clear idea of what you may want to investigate further.
</aside>
---

## The Histogram


- Effective for distribution across groups.

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/histogram.png)


<aside class="notes">
**Teaching Tips**:

- Histograms are useful when you want to see how your data are distributed across groups. Important: histograms are not the same thing as a bar chart! Histograms look similar to bar charts, but with bar charts, each column represents a group defined by a categorical variable; and with histograms, each column represents a group defined by a continuous, quantitative variable.
- One implication of this distinction: with a histogram, it can be appropriate to talk about the the tendency of the observations to fall more on the low end or the high end of the X axis.
- With bar charts, however, the X axis does not have a low end or a high end; because the labels on the X axis are categorical - not quantitative.
</aside>

---

## Bar Chart vs Histogram

![](https://qph.fs.quoracdn.net/main-qimg-237e649130e7ae0245e003a6a1949b91.webp)

<aside class="notes">
**Teaching Tips**:

- When would you use a histogram? What about a bar chart?
</aside>

---

## Choosing the Right Chart


Check out [this series of charts](https://i.redd.it/e7alp8yrnb711.png): `https://i.redd.it/e7alp8yrnb711.png`

- Which is easiest to view the data?


<aside class="notes">
**Teaching Tips**:

- The choice of visualization should depend what you are trying to show. Here is a helpful flowchart that you can use to determine the best type of visualizations.
</aside>

---

## Knowledge Check: Choosing a Chart


Annual sales in each state for a grocery store chain?

- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.

<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(bar)
</aside>

---

## Knowledge Check: Which type of chart?

Change in average income since 1960 for American adults?

- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.


<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(line or scatter)
</aside>


---

## Which type of chart?

Relationship of average income to education level?


- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.


<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(scatter)
</aside>


---

## Which type of chart?


Distribution of average income across age ranges?

- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.

<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(histogram)
</aside>

---

## Which type of chart?


Percentage of people who own a car vs. don't own a car?

- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.

<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(pie, or bar)
</aside>
---

## Which type of chart?


Percentages of people who like 5 different genres of music?

- Bar chart.
- Pie chart.
- Scatterplot.
- Histogram.


<aside class="notes">
**Teaching Tips**:

- Which type of chart do you think we should use in the following cases?
(bar)
</aside>

---

## Changing Gears: Best Practices

Are all charts created equal?

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/bad_lines.png)

<aside class="notes">
**Teaching Tips**:

- What can you understand from this chart? Not much!
- How do visual cues help us understand the data?
- What key piece of information is missing from this chart? (A title)
</aside>

---

## Group Activity: Exploring Good Visualizations

Get in small groups of 2-3.

[Go to [https://www.reddit.com/r/dataisbeautiful/top/](https://www.reddit.com/r/dataisbeautiful/top/). These are all data visualizations created by people like you!

Pick one that you think is particularly good and one that is particular bad. Why? What are the characteristics?


<aside class="notes">
Teaching tips:

- Give them time to think about this, then have them announce to the class.
</aside>


---

## Attributes of Good Visualization



Some attributes affect our brain more strongly.

In order of focus:
- Position
- Color
- Size


<aside class="notes">
**Teaching Tips**:

- What are some attributes you think are important for data visualizations to have? Some have more of an effect on our brains than others. The ones we tend to focus on most are position, then color, then size.
- Let's take a look at what Jeffrey Shaffer, who teaches data visualization at the University of Cincinnati, thinks:
</aside>

---

## Visualization Tips: General


Avoid all 3D options!

![](https://s3.amazonaws.com/ga-instruction/assets/python-fundamentals/3dchart.png)

<aside class="notes">
Teaching Tips:

- If you have extra time at the end, head to the Data is Beautiful reddit page and pull up various visualizations; discuss what makes each one good or bad.
</aside>

---

## Summary

- What is the purpose of data visualization?

- What are some examples of what makes for good or bad visualization?

- When would you use the following types of charts or graphs?
    - Bar chart
    - Pie chart
    - Scatter plot
    - Histogram

<aside class="notes">
Teaching Tips:

- Wrap up the learning and share additional resources and next steps.
- If you have extra time at the end, head to the Data is Beautiful reddit page and pull up various visualizations; discuss what makes each one good or bad.
</aside>

---

## Additional Resources

- A great short article on [when pie charts are better?](http://annkemery.com/pie-chart-guidelines/)
- [A gallery of charts](https://github.com/mbostock/d3/wiki/Gallery)
- [A Stats Video](https://www.youtube.com/watch?v=hVimVzgtD6w)
- [SAS: Data Viz](http://www.sas.com/en_us/insights/big-data/data-visualization.html)
- [A guide to when to use each chart](https://drive.google.com/file/d/0Bx2SHQGVqWasT1l4NWtLclJJcWM/view)
- [44 Types of Graphs](http://blog.visme.co/types-of-graphs/)
- [Advice on making good visualizations](https://www.gooddata.com/blog/8-ways-turn-good-data-great-visualizations)
- [Reddit's Data Visualization forum](http://reddit.com/r/dataisbeautiful)
