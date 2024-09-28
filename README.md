
# YouTube Trending Data Analysis

This repository contains code and resources for analyzing YouTube trending videos data. The objective of this project is to explore the YouTube trending dataset and extract insights such as video popularity patterns, trends, and factors that contribute to a video going viral.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

YouTube is one of the most popular platforms for sharing video content. Videos that trend on YouTube can have a significant impact on content creation and influence viewer preferences. This project aims to analyze the dataset of trending videos from YouTube and provide insights based on various factors such as views, likes, comments, category, and publication time.

The primary goals of this analysis include:

- Understanding which factors contribute most to a video trending on YouTube.
- Exploring patterns related to video categories, views, likes, and other metrics.
- Visualizing trends and relationships in the dataset.

## Dataset

The YouTube Trending Data is sourced from [Kaggle's YouTube Trending Video Dataset](https://www.kaggle.com/datasnaek/youtube-new). The dataset includes metadata for daily trending videos in different regions and contains the following key fields:

- `video_id`: Unique identifier for the video.
- `title`: The title of the video.
- `channel_title`: The channel that published the video.
- `category_id`: The category in which the video was published.
- `publish_time`: The date and time when the video was published.
- `views`, `likes`, `dislikes`, `comment_count`: Engagement metrics for the video.
- And more.

## Installation

To set up the project on your local machine, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/SummerVo/youtube-trending-data-analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd youtube-trending-data-analysis
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After the installation, you can start analyzing the dataset by running the main analysis script.

1. To run the data analysis:

   ```bash
   python analyze_trending_videos.py
   ```

2. The analysis results, including visualizations and data insights, will be generated in the `output/` folder.

## Features

- **Data Cleaning:** Handles missing values and inconsistencies in the YouTube trending data.
- **Data Exploration:** Provides various statistics, such as the distribution of views, likes, and other metrics across video categories.
- **Visualization:** Uses libraries like `matplotlib` and `seaborn` to create charts for trends and relationships between variables.
- **Insights:** Identifies factors that contribute to video virality, such as the role of category, publish time, and engagement metrics.

## Contributing

Contributions to this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`.
5. Push to the branch: `git push origin my-feature-branch`.
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
