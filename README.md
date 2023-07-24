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
