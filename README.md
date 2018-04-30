# Winybot
RASA SLACK : Chatbot (WIny) that provides reviews, price, ratings and winery about the wines asked by the user.

## Getting started
These instructions will get you all the necessary libraries to run the code.

```
pip install -r requirements.txt 
```

Then check the spacy version. It should be same for the python version and for the language you want your bot to be.

## Running the tests
Build your domain file and data.json.
First the Rasa NLU model must be trained. 


```
python nlu_model.py
```

After this the dialogue engine must be trained. First by running train_init.py followed by train_online.py 
train_online.py will launch the interactive backend training session.


```
python train_init.py

python train_online.py
```
Now you will need a dialogue management model to put everthing together and test the bit in slack.

## Connecting to slack

Here how to do it:
download ngrok and launch it on terminal and we will use 5004 as our input channel.

```
python run_app.py

```
```
./ngrok http 5004 (for mac) and ngrok http 5004 (for windows)

```
Copy the last forwarding link and put it under Event subscription tab of api.slack.com .
Save the changes.


Go to your chatbot and happy chatting! :)



