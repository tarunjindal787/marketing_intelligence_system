# Part 1: Business Problem Discovery

Heres the three major problems that we face in a digital marketing agency and how we can use technology (AI and non-AI) to solve them. Like the PDF said, we shouldn't use AI for everything, so I've highlighted where simple automation works better.

---

### Problem 1: Predicting Content Performance (Requires AI/ML)

1. **What is the current problem?**
   Digital marketing managers spend hours creating posts and ads, but many fail to get engagement, wasting client budget. They don't know what works before publishing.
2. **Who experiences the problem?**
   Social media managers, content creators, and the clients who pay for the campaigns.
3. **What data would be required?**
   Historical post metrics like impressions, reach, likes, comments, shares, saves, platform, industry, posting day/time, and content format.
4. **Why is AI/ML appropriate for solving it?**
   Because engagement patterns are non-linear, multi-dimensional (depends on platform, time, topic, content format combined), which is too complex for simple rules. ML can learn these patterns from data.
5. **What would happen if the problem is not solved?**
   Money wasted on bad ads, clients get unhappy and churn.
6. **How would you measure the business impact?**
   Reduction in wasted ad spend by 15-20%, increase in client ROI.
7. **What would a human currently have to do manually?**
   A human has to look at old posts in Excel, try to spot trends by eye, and guess what might work next.

---

### Problem 2: Client Monthly Report Generation (Does NOT require AI - Automation is better)

1. **What is the current problem?**
   Every month, account managers spend 3-4 days collecting data from Facebook, Google Analytics, Instagram, etc., putting it in powerpoint slides. It's boring and slow.
2. **Who experiences the problem?**
   Account managers, digital marketers.
3. **What data would be required?**
   API data from Facebook Ads, Google Ads, GA4.
4. **Why is AI/ML appropriate for solving it?**
   Actually, it is **NOT** appropriate. There is no prediction or pattern recognition needed. It is a straight data extraction and formatting task. A simple rule-based automation script or ETL tool (like Zapier or Python with APIs) is 100% accurate, cheaper, and faster. Using AI here would be overkill and might introduce hallucinations.
5. **What would happen if the problem is not solved?**
   High staff burnout, late reporting, human typos in data.
6. **How would you measure the business impact?**
   Hours saved per month per employee (e.g., saving 20 hours per manager).
7. **What would a human currently have to do manually?**
   Logging into 5 dashboards, copy-pasting numbers to Excel, making charts, pasting to PPT.

---

### Problem 3: Basic Lead Qualification & Scoring (Does NOT require AI - SQL/Analytics rules are better)

1. **What is the current problem?**
   Marketing campaigns generate hundreds of cheap leads, but sales teams waste time calling people with invalid phone numbers or who don't fit the client profile.
2. **Who experiences the problem?**
   Sales team, marketing team.
3. **What data would be required?**
   Lead form data (age, job title, email, phone format).
4. **Why is AI/ML appropriate for solving it?**
   It is **NOT** required for the first phase. We can filter out 60% of bad leads using simple SQL filters or regular expressions (e.g., checking if email is @gmail vs @company, if phone has 10 digits, if job title contains "student" or "unemployed" for B2B). Traditional rule-based software is much faster and cheaper to start with than training a complex lead prediction model.
5. **What would happen if the problem is not solved?**
   Sales team gets annoyed, conversion rates look terrible.
6. **How would you measure the business impact?**
   Leads rejected automatically, percentage increase in sales conversion from qualified leads.
7. **What would a human currently have to do manually?**
   Checking emails manually, dialing fake numbers.
