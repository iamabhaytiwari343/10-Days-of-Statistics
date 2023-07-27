# Statistic important concepts
*** 
### Mean
In statistics, the term "mean" refers to the average value of a set of numbers. It is one of the most commonly used measures of central tendency. The mean is calculated by summing up all the values in the dataset and then dividing that sum by the total number of data points.

For a given dataset of n elements, the mean (often denoted by μ) is computed as follows:

Mean (μ) = (Sum of all values) / (Number of values)

Mathematically, it can be represented as:

μ = (x₁ + x₂ + x₃ + ... + xₙ) / n

where x₁, x₂, x₃, ..., xₙ are the individual values in the dataset, and n is the total number of values.

The mean provides a useful summary of the dataset as it represents a typical value around which the data tends to cluster. It is sensitive to extreme values, often called outliers, as they can significantly affect the overall average.

### Median 
In statistics, the median is another measure of central tendency, like the mean. While the mean represents the average of a dataset, the median is the middle value of a sorted list of numbers. To calculate the median, you first need to arrange the data in ascending or descending order.

If the dataset has an odd number of elements, the median is the middle value. If the dataset has an even number of elements, the median is the average of the two middle values.

Here's how to find the median for a given dataset:

* Sort the data in ascending or descending order.
* If the number of elements is odd, the median is the middle value.
* If the number of elements is even, the median is the average of the two middle values.

The median is often preferred over the mean when dealing with datasets that contain outliers, as it is less influenced by extreme values. It gives us the value that separates the lower half and the upper half of the data, making it a robust measure of central tendency in such situations.
### Mode

In statistics, the mode is another measure of central tendency, distinct from the mean and median. The mode represents the value that appears most frequently in a dataset. In other words, it is the data point with the highest frequency or count.

A dataset can have one mode (unimodal) if there is a single value that occurs most frequently, or it can have multiple modes (multimodal) if there are two or more values with the same highest frequency.

Finding the mode is relatively straightforward. You can do it by counting the occurrences of each unique value in the dataset and identifying the one(s) with the highest frequency.

It's worth noting that a dataset can have no mode if all the values occur with the same frequency, or it can be bimodal, trimodal, etc., if it has two, three, or more values with the same highest frequency.

The mode is particularly useful when dealing with categorical or discrete data, such as colors or categories, where calculating a mean or median might not be meaningful. It helps identify the most frequently occurring value, which can provide insights into the central tendency of the dataset.

### Weighted Mean

In statistics, the weighted mean is a variation of the regular arithmetic mean that takes into account the importance or weight of each data point in the dataset. It is used when some values in the dataset are more relevant or have a greater impact on the overall average than others.

To calculate the weighted mean, you multiply each data point by its corresponding weight, sum up these products, and then divide the total by the sum of the weights. Mathematically, it can be represented as:

Weighted Mean (μ) = (Σ (wᵢ * xᵢ)) / (Σ wᵢ)

Where:

* μ is the weighted mean.
* wᵢ is the weight of the i-th data point.
* xᵢ is the i-th data point.
