<<<<<<< HEAD
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tttonyalpha/life_analyser">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Life analyser</h3>

  <p align="center">
    This is a telegram bot that parses which parses my telegram channel with daily reports. Based on this data, it generates a summary of past reports, predicts various indicators of well-being for the next day and recommends activity for 
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
<details>
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



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Every day I make a list of tasks in the telegram channel, and at the end of the day I mark with emoji whether I have completed the tasks or not and evaluate my productivity, the interest of the day and stress level. on a 10-point scale.


I decided to create a chatbot, a chatbot that parses my telegram channel, my Google calendar, data from my fitness bracelet and, based on the information from there, makes various predictions, gives advice and checks the correctness of filling out reports

# Feature 1: N-day summary and autoreports  
Model summarize my activities, emotions and etc during week and make report with advices 

Main idea:

1. Detect intents (activity types)
2. NER (detect activity and get it’s normal form)
3. For every activity detect emotion (neutral, happy, angry, etc ..)
4. Get numeric metrics 
5. Anomalies detection and alarms 
6. If the report is filled out incorrectly, make reminders

# Feature 2: Recsys for activity

Based on information from summary:
    
1. Recommend top 3 activity for next day (from my activity pool)
2. Recommend Activity types on which i should focus next n-days 
3. Rest time control 
4. Tumblers for recommendations types: (work/rest/creativity)

# Feature 3: Activity recognition on images 

If I haven't filled out the report, but attached photos, bot automatically analyzes the images and recognizes activities


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

My contacts: [@twitter_handle](https://t.me/my_name_is_nikita_hey) - tttonyalpha@gmail.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/tttonyalpha/life_analyser)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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
[product-screenshot]: images/screenshot.png
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
=======
# life_analyser

- 1. N-day summary and autoreports
    
    
    Model summarize my activities, emotions and etc during week and make report with advices 
    
    Main idea:
    
    1. Detect intents (activity types)
    2. NER (detect activity and get it’s normal form)
    3. For every activity detect emotion (neutral, happy, angry, etc ..) [model](https://huggingface.co/SamLowe/roberta-base-go_emotions?text=Stupid+work)
    4. Get numeric metrics 
    5. Make n-day summary and predict next day metrics, emotions and reccomend activities 
    6. Anomalies detection and alarms 
    7. Make automatic dayily posts with default picture 
    
    **Features to analyse:**
    
    1. Activity types 
    2. Emotions 
    3. Numerical metrics: anomalies detect, etc 
    4. Mi band data
    
    **Activity types:** selfdev, university, work, relax/rest time, sport & health, family, travel_&_adventure, chore, bad habit 
    
    **Summary:**
    
    1. Average numeric metrics
    2. Best/worst day and activity connected with this
    3. Activity types pie chart and metrics increase in comparison with previous days
    4. Next day metrics prediction 
    5. Activity and emotions connected with it matrix  
    6. Generate picture for next day based on summary and make pushes about adding notes and day rates to the day 
    
    **Data to store in DB:**
    
    TABLE Posts:
    
    1. post_id INTEGER PRIMARY KEY
    2. text
    3. parsed_date
    4. upload_date
    5. edit_date
    6. productivity_rate
    7. interest_rate
    8. stress_rate
    
    TABLE Images:
    
    1. image_id PRIMARY KEY
    2. post_id FOREIGN KEY
    3. object_id 
    4. image_path
    5. image_parsed_description
    
    TABLE Activities:
    
    1. post_id FOREIGN KEY
    2. ? activity_id PRIMARY KEY AUTO INCREMENT
    3. activity_name
    4. parsed_activity_name
    5. activity_type (intent)
    6. activity_emotion 
    7. activity_emoji

TABLE Week_reports:

1. Report_ id
2. 

- 2. **Recsys for activity**
    
    Based on information from summary:
    
    1. Recommend top 3 activity for next day (from my activity pool)
    2. Recommend Activity types on which i should focus next n-days 
    3. Rest time control 
    4. Tumblers for recommendations types: (work/rest/creativity)
    
- 3. **Photos\Videos autogeneration based on summary**
    
    

- 4. **Image recognition**
>>>>>>> 53318719849f165fff7512b4edbf64c01eb028ce
