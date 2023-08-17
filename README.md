<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tttonyalpha/life_analyser">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Life analyser</h3>

  <p align="center">
    This is a telegram bot which parses my telegram channel with daily reports. Based on this data, it generates a summary of past reports, predicts various indicators of well-being for the next day and recommends activity for 
    <br />
    <a href="https://github.com/tttonyalpha/life_analyser"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/tttonyalpha/life_analyser">View Demo</a>
    ·
    <a href="https://github.com/tttonyalpha/life_analyser/issues">Report Bug</a>
    ·
    <a href="https://github.com/tttonyalpha/life_analyser/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<!-- <details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
 -->


<!-- ABOUT THE PROJECT -->
## About The Project

![My channel screen shot][product-screenshot]
<!-- (https://drive.google.com/file/d/12k2PHKTiuc_fPejNALLAS7gnQKYj06X2/view?usp=sharing) -->

Every day I make a list of tasks in the telegram channel, and at the end of the day I mark with emoji whether I have completed the tasks or not and evaluate my productivity, the interest of the day and stress level. on a 10-point scale.


I decided to create a chatbot, a chatbot that parses my telegram channel, my Google calendar, data from my fitness bracelet and, based on the information from there, makes various predictions, gives advice and checks the correctness of filling out reports

## Feature 1: N-day summary and autoreports  
Model summarize my activities, emotions and etc during week and make report 

#### Activiti type recognition

For this task i have tried different models: fasttext+gb, fasttext+BiLSTM, roberta-base. Best score gives roberta, finetuned on small dataset with layer freezing and other specific hacks mentioned in articles: [[1]](#1), [[2]](#2), [[3]](#3)

| Model           | Accuracy(%) | F1   |  
|----------------|---------------|---------------|
| fasttext+gb | 82  |  | 
| fasttext+BiLSTM   | 88  |  | 
| roberta-base   | 92  |  | 
| roberta-base with additional train data  | 95  |  | 

<!-- 2. NER (detect activity and get it’s normal form) -->
#### For every activity detect emotion (neutral, happy, angry, etc ..)

For this task i used zero-shot classification model from huggingface - [bertweet-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)


## Feature 2: Activities recommendation system 

My recommendation system consists of two parts: 1 - activity type reccomendations 2 - activities generation. First model predict top 3 activity types for next day, then second model generate some activities for each actitity type. 

#### Activity type reccomendations:

For this task I used pretrained fasttext embeddings and LSTM. For each day I aggregate activitiy embeddings using average pooling, then concatenate additional numeric features and pooled embeding - thus I get day representtion embedding and put them in LSTM sequentially according to the date. 

#### Activities generation:

Now when I get activities types recommendation I train adapters for flan-T5 model to generate activities.
For each activity type a generate 2 activitiy: one based on user pisitive experience, another something new, that user never experienced before.   

**To generate activities according to the user's positive experience** I get 5 activities from past with highest day score and 5 random activities. Then I use promt: 

```
For last 10 days user experienced activities connected with #activities_type and gives them scores:
#activity_1 - #rate_1, ..., #activity_10 - #rate_10 Reccomend new activity for this user: 

```

and train flan T5 model on GPT-3's responces.

**To generate new activities, that user never experienced before** I use the same promt on T5 inference but add blacklist activities for GPT-3 on train. 


<!-- 
#### Based on information from summary:
    
1. Recommend top 3 activity for next day (from my activity pool)
2. Recommend Activity types on which i should focus next n-days 
3. Rest time control 
4. Tumblers for recommendations types: (work/rest/creativity) -->

#### Architecture: 

![lstm recsys][lstm_recsys]


#### My model results: 

![lstm predictions][lstm_predictions]


## Feature 3: Activity recognition on images 
  
If I haven't filled out the report, but attached photos, bot automatically analyzes the images and recognizes activities


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- 

### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p>
 -->


<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->




<!-- ROADMAP -->
## Roadmap

- [x] Telegram channel data fetcher and parser
- [x] Database mechanics and data markup
- [x] Activity classifier 
- [x] Sentiment detector 
- [x] Day score predictor
- [x] Activity recommender
- [x] LLM-based activity generator 


- [ ] LLM-based chat bot with intent recognition
- [ ] LLM-based daily/weekly summaries generator 
- [ ] Activities detection from images
- [ ] Anomalies detection


<!-- CONTACT -->
## Contacts

Telegram: [@my_name_is_nikita_hey](https://t.me/my_name_is_nikita_hey) <br>
Mail: tttonyalpha@gmail.com 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## References
<a id="1">[1]</a> 
Revisiting Few-sample BERT Fine-tuning.
Tianyi Zhang, Felix Wu, Arzoo Katiyar, Kilian Q. Weinberger, Yoav Artzi.<br>
[arXiv:2006.05987](https://arxiv.org/abs/2006.05987)

<a id="2">[2]</a> 
Investigating Transferability in Pretrained Language Models.
Alex Tamkin, Trisha Singh, Davide Giovanardi, Noah Goodman.<br>
[arXiv:2004.14975](https://arxiv.org/abs/2004.14975)

<a id="3">[3]</a> 
Universal Language Model Fine-tuning for Text Classification.
Jeremy Howard, Sebastian Ruder.<br>
[arXiv:1801.06146](https://arxiv.org/abs/1801.06146)


<a id="4">[4]</a> 
Scaling Instruction-Finetuned Language Models.
Google.<br>
[arXiv:2210.11416](https://arxiv.org/abs/2210.11416)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/channel_screen.png
[lstm_predictions]: images/lstm_predictions.png
[lstm_recsys]: images/lstm_recsys.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
