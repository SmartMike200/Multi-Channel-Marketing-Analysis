# Multi-Channel-Marketing-Analysis
Multi Channel Marketing Analysis, Using Multiple Linear Regression 


## EXECUTIVE SUMMARY
This project examined the impact of TV advertising, Social Media advertising, and Influencer marketing on Sales using Multiple Linear Regression analysis. The primary objective was to identify the marketing channels that contribute most significantly to sales growth and provide data-driven recommendations for budget allocation.
Prior to model development, exploratory data analysis and multicollinearity testing were performed. Correlation analysis and Variance Inflation Factor (VIF) were used to assess relationships among predictor variables. Radio advertising was excluded from the final model due to multicollinearity concerns, helping to improve model stability and interpretability.

The final regression model achieved an Adjusted R-squared value of 0.427, indicating that approximately 42.7% of the variation in Sales can be explained by TV advertising, Social Media advertising, and Influencer marketing. The overall model was statistically significant (F-statistic = 143.0, p < 0.001), demonstrating that the selected predictors collectively provide meaningful insight into sales performance.

Analysis of individual predictors revealed that TV advertising and Social Media advertising are statistically significant drivers of Sales (p < 0.001). In contrast, Influencer marketing was not statistically significant (p = 0.320), suggesting that its contribution to Sales cannot be reliably distinguished from random variation within this dataset.


## COEFFICIENT INTERPRETATION
Holding all other variables constant:
• A one-unit increase in TV advertising is associated with an average increase of approximately 40.55 units in Sales.
• A one-unit increase in Social Media advertising is associated with an average increase of approximately 18.19 units in Sales.
• Influencer marketing has a coefficient of -2.51; however, because its p-value (0.320) is greater than 0.05, this effect is not statistically significant and should not be interpreted as a reliable negative impact on Sales.


## BUSINESS RECOMMENDATIONS
Prioritize TV Advertising
TV advertising demonstrates a strong positive and statistically significant relationship with Sales. With the largest coefficient (40.55), TV advertising appears to provide the greatest contribution to sales growth and should remain a major component of the marketing budget.
Increase Investment in Social Media Marketing
Social Media advertising is also a significant predictor of Sales and shows a substantial positive effect. Given its measurable contribution and scalability, increasing investment in Social Media campaigns is likely to generate additional sales growth.
Reassess Influencer Marketing Strategy
The analysis found no statistically significant relationship between Influencer marketing and Sales. This does not necessarily mean influencer campaigns are ineffective, but it suggests that current influencer activities may not be generating measurable sales impact. Management should review campaign objectives, influencer selection, audience targeting, and performance metrics before increasing spending in this area.
Focus Budget on Proven Channels
Based on the model results, marketing resources should be concentrated on TV and Social Media advertising, which demonstrate the strongest evidence of driving sales performance.
Continue Monitoring and Model Refinement
Since the model explains 42.7% of sales variation, additional factors beyond advertising channels likely influence Sales. Future analyses should consider variables such as pricing, promotions, seasonality, customer demographics, and market conditions to improve predictive accuracy.


## CONCLUSION
The regression analysis indicates that TV advertising and Social Media advertising are the primary drivers of Sales within this dataset. TV advertising has the strongest observed impact, while Social Media provides an additional significant contribution. Influencer marketing does not show a statistically significant effect on Sales and should be reviewed before receiving additional budget allocation. Therefore, future marketing investments should prioritize TV advertising first, followed by Social Media marketing, while carefully evaluating the effectiveness of Influencer campaigns.
