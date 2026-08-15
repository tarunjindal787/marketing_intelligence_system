# Part 2: Marketing Dataset Analysis

I ran the analysis on our synthetic dataset of 600 records. Here is what we found from the data. I've also saved the charts as PNGs in this folder so you can look at them.

### 1. Which content performs best and worst?
- **Best Performing Content Types**: Reels and Videos got the highest average performance scores (around 31.2). This is probably because people watch video content longer, which boosts the score.
- **Worst Performing Content Types**: Text posts and Images performed the worst (around 28.3). They don't engage users as much.
- **Best Performing Platforms**: LinkedIn and TikTok are the top-performing platforms on average in our dataset. YouTube also did well.
- **Worst Performing Platforms**: Facebook and Instagram actually got lower average scores.

### 2. Which variables are correlated with performance?
This was a really interesting finding.
- **Leads and Revenue** have a positive correlation with the Performance Score (around 0.11 and 0.10). This makes sense because our score formula values conversions and business results.
- **Reach and Impressions** actually had a *negative* correlation (around -0.18 and -0.16) with the Performance Score. 
- **Ad Spend** has almost zero correlation (-0.001) with performance.
*What this means for the agency:* This is a classic digital marketing trap! Chasing "vanity metrics" like reach or impressions doesn't mean you are getting good results. A post can go viral and reach 50,000 people but get 0 leads and 0 clicks, giving it a low performance score. High ad spend also doesn't guarantee success if the content is bad.

### 3. Are there differences between Industries?
Yes, some industries do much better on average:
- **Tech and Fashion** had the highest performance scores. They are very visual and have trending topics, which makes them easier to promote.
- **Finance and Healthcare** had lower average scores. These are "drier" industries, so it's harder to get high engagement rates or cheap leads.

### 4. What anomalies or unusual patterns exist?
- We found 21 posts where the client spent **over $150 in Ad Spend** but the Performance Score was **less than 20**. E.g. Client_B on YouTube spent a lot of money but got terrible results.
*What this means:* This represents "budget bleeding." The agency is wasting client money on ads that are either targetted at the wrong audience or have bad creatives. We should have automated alerts for these!

### 5. What data would you want but don't have?
If we want to build a better system, we are missing some key data:
- **Creative elements**: Is it a photo of a person? What are the main colors? Text overlay?
- **Audience demographics**: Age, gender, location of the people who saw the post.
- **Historical competitor data**: How are competitor brands performing with similar topics?
- **Click-through rates (CTR) by placement**: Was the ad in Instagram Stories or Main Feed?

---

### Visualisations generated:
- [platform_performance.png](file:///E:/BLEND/marketing_intelligence_system/part2_dataset_analysis/platform_performance.png)
- [industry_performance.png](file:///E:/BLEND/marketing_intelligence_system/part2_dataset_analysis/industry_performance.png)
- [correlation_matrix.png](file:///E:/BLEND/marketing_intelligence_system/part2_dataset_analysis/correlation_matrix.png)
