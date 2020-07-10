# Cognito: The future of Parkinsons Detection

## Note 1

The AI model has 80% Accuracy which makes it more accurate than clinical diagnosis by someone who is not an expert. The model is often times more accurate than a real person!

## Note 2

We had the individual AI and Keylogger working, we were unfortunatley unable to combine them and thus there was no demo. To watch the individual demos for the AI and Keylogger you can go down to demo videos.

## Inspiration
Every year thousands of people are diagnosed with Parkinson's. Many times its too late and their relatives are forced to watch as they become shells of the humans that they once were. The worst part is that Parkinson's is often difficult to detect and can be tricky to diagnose.

We wanted to create something that could help detect Parkinsons in a quick and efficent way, without being obtrusive or expensive.

Thus we present Cognito
## What it does
Cognito is very simple

Cognito has a key logger which tracks specific typing metrics. Cognito stores these metrics which are then analyzed by an advanced AI algorithim which detects for signs of Parkinson's. If Cognito detects signs of the disease it will send an email alerting the user about the issue.

Cognito is a simple background script that doesn't need an internet connection and is simple and hassle free. 

Cognito has plenty of potential as typing can not only be used for Parkinsons, but for many other dieases as well such as Huntington's and Alzheimer's Disease. 

## How we built it

We used the neuroQWERTY dataset and keras to develop an algorithm which detects whether or not a user has Parkinson's.

We then used python to develop a simple keylogger that tracks the metrics which the Algorithm will need to analyze.

## Challenges we ran into

Developing the Algorithm was incredibly difficult. It took a lot of time and was difficult to debug. It was the group's first time working with numerical classification in AI. 


## Accomplishments that we're proud of

We are proud that we got the AI algorithm to work. It took a lot of time and effort, but it payed off!

We were also proud that we could detect such a deadly disease with such a simple metric... typing!

## What we learned

We learned how AI works and how to use it and learned how to do key detection with python. For two thirds of the group it was their first time working with any sort of AI at all so this was a new and fun journey for all!

## What's next for Cognito

We would like to develop our algorithm even further. Unfortunatley, Cognito has a 50% accuracy, however with the discovery of some new datasets and with the ability to spend more time with the Algorithim we feel confident that we could get the prediction to over 70%.

We then plan to release this so that we can start helping people all around the world!

## Demo Videos:

Keylogger: https://www.youtube.com/watch?v=iiWSOhdJlaA
AI: https://www.youtube.com/watch?v=YuE35_pRSeE

## Discords

CantTouchThis#8155
theaditya24#8701
anishfish#5103

## Citation
Arroyo-Gallego, Teresa et al. “Detecting Motor Impairment in Early Parkinson's Disease via Natural Typing Interaction With Keyboards: Validation of the neuroQWERTY Approach in an Uncontrolled At-Home Setting.” Journal of medical Internet research vol. 20,3 e89. 26 Mar. 2018, doi:10.2196/jmir.9462

Adams, Warwick R. “High-accuracy detection of early Parkinson's Disease using multiple characteristics of finger movement while typing.” PloS one vol. 12,11 e0188226. 30 Nov. 2017, doi:10.1371/journal.pone.0188226

We used a few studies for inspiration and we used the tappy kaggle dataset. The keylogger and the algorithm were our own however.

