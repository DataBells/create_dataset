
# Used Car Sales Dataset Generation
### Overview

This guide will help you create a dataset tailored to your specific needs. Before you begin, decide on the dataset's attributes and data types. Once you have a clear idea, you can use ChatGPT to generate a simple Python script that matches your requirements. You can then tweak this script as needed to suit your analysis requirements.

### Example

Suppose you want to create a dataset for used car sales from 2015 to 2024 with 10,000 records and 25 columns containing different data types. Here's the prompt you can use to ask ChatGPT for help:

## Generate a Python script to create a realistic dataset of 10,000 records for used car sales by different distributors from 2015 to 2024.
**The dataset should include the following attributes:**

**ID:** _A unique identifier (String)<br>_

**Distributor Name:** _Randomly assigned from a predefined list of names with at least 23% probability for each name (String)<br>_

**Location:** _Randomly assigned from a list with at least 14% probability for each location (Geo Location)<br>_

**Car Name:** _Randomly assigned from a list with at least 17% probability for each name (String)<br>_

**Manufacturer Name:** _Randomly assigned from a list with at least 27% probability for each name (String)<br>_

**Car Type:** _Randomly assigned from a list with at least 6% probability for each type (String)<br>_

**Color:** _Randomly assigned from a list with at least 23% probability for each color (String)<br>_

**Gearbox:** _Randomly assigned from a list with at least 17% probability for each type (String)<br>_

**Number of Seats:** _Randomly assigned from a list with at least 6% probability for each number (Int)<br>_

**Number of Doors:** _Randomly assigned from a list with at least 16% probability for each number (Int)<br>_

**Energy:** _Randomly assigned from a list with at least 6% probability for each type (String)<br>_

**Manufactured Year:** _Randomly generated with custom probabilities for each year from 2015 to 2024 (Date)<br>_

**Price:** _Generated based on Manufacturer Name, Car Name, Car Type, Manufactured Year, and Energy (Int). Consider how these affect the price and its range.<br>_

**Mileage:** _Values between 1,000 to 1,000,000 kilometers with a probability of 15% above 75,000 (Int)<br>_

**Engine Power:** _Values between 90 to 350 horsepower with a probability of 15% above 110 hp (Int)<br>_

**Purchased Date:** Randomly generated with custom probabilities for each year from 2015 to 2024 (Date)<br>

**Car Sale Status:** _"Sold" if there is a Sold Date, otherwise "Unsold" (String)<br>_

**Sold Date:** _Assigned to 22% of the cars with specific probabilities for each year, ensuring it's at least 2 months after the purchased date (Date)<br>_

**Purchased Price:** _Generated based on Manufacturer Name, Car Name, Car Type, Manufactured Year, and Energy (Int)<br>_

**Sold Price:** _At least $10 to $15 higher or lower than the Purchased Price (Int)<br>_

**Margin:** _Profit or loss percentage based on the Purchased Price and Sold Price (Int)<br>_

**Sales Agent Name:** _Randomly generated (String)<br>_

**Sales Rating:** _Randomly generated from 1 to 5, with more sales leading to a higher rating (Int)<br>_

**Sales Commission to Agent:** _Based on the margin, with 0.2% of the profit given if the agent makes more sales and profit (Int)<br>_

**Feedback:** _Randomly assigned from a list with at least 37% probability for each feedback type (String)<br>_

ChatGPT will provide a basic script that you can customize further. <br>

### Check my GitHub for the code and additional tweaks not included in the prompt.

### Conclusion

This approach allows beginners to create realistic datasets for analysis without the hassle of finding data. 
Having a basic understanding of programming and data analysis will be helpful.

### Thank you!
