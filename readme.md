# **The West World Project**
## A State Machine Based on an Example From **Programming Game AI by Example*** by Mat Buckland

This is an expansion of a concept for a state machine in Mat Buckland's Book **Programming Game AI by Example*** which
is called **The West World Project**.

In its most basic form, which we have translated from C++, a describes Gold Mining AI named Bob alternates between four states 
based on the amount of gold he has mined, the amount of gold he has saved, how thirsty he is, how tired he is,
what his last task was, and where said task was carried out. 

These states are:

1. Digging for gold.
  1. When he enters this state, if he isn't already in the Gold Mine, his location will be changed to Gold Mine, and he 
will declare that he is walking to the mine.
  2. If he finds gold he will collect it and gain one gold and one fatigue, and then will declare that he is picking up
 a nugget.
  3. If he is thirsty, he will enter the fourth state, which is visiting the Saloon.
  4. If he has not collected the maximum amount of gold, he will continue collecting gold.
  5. Once he has collected the maximum amount of gold he can carry, he will declare that he is leaving the mine with 
his pockets full of gold and enter the second state, "Visting the Bank".

2. Visiting the Bank
  1. When he enters this state, if he isn't already at the Bank, his location will be changed to the Bank, and he will
declare that this is location he is traveling to.
  2. The gold that he is carrying will be transferred to his savings, and the amount of gold he is carrying on his
person will return to zero. He will declare that he is making a deposit, and the total amount of savings he has will be 
declared.
  3. If he has not aquired a satisfactory increase in his savings, he will return to first state and search for more 
gold.
  4. If he has aquired a satisfactory increase in his savings, he will aknowledge his contentment and declare that he 
is heading home, and then enter the third state "Going Home to Rest".

3. Going Home to Rest 
  1. If he is not already at Home, his location will change to Home, and he will declare the he is going home to see
his wife.
  2. The miner rests. His fatigue is reduced by one.
  3. If he is still tired when he wakes up he will say he wants to sleep some more and keep resting until he is no 
longer tired.
  4. If he is thirsty when he wakes up, he will change his state to Going to the Saloon to Drink.
  5. If he is no longer tired and not thirsty he will change his state to Digging For Gold.
  6. As he exits this state he will greet you with a cheerful good morning.

4. Going to the Saloon to Drink
  1. When he enters this state, if he isn't already at the Saloon, his location will be changed to the Saloon, and he 
will declare that this is where he is heading.
  2. At the Saloon, his fatigue will increase by one. His thirst will decrease by three in order to compensate for the 
fact that his thirst is increased by one everytime his status is updated, giving him aq net decrease of two thirst 
everytime he drinks. When he does this he declares he's having a drink.
  3. If he is still thirsty after drinking he will have another drink.
  4. If his thirst is quenched and his pockets are full, he will change his state to Visiting the Bank.
  5. If his thirst is quenched and his pockets are not full, but he is tired, he will go home and rest.
  6. If his thirst is quenched and his pockets are not full and he is not tired, he will change his state to digging 
for gold.

The goal of this project is to make improvements and implement new features to this program to make it more complex.
Some of these include, but are not limited to:
* Improve basic functionality of the state machine.
* Implementing other miners besides Bob to operate alongside one another, likely each one having different starting
stats that cause them to behave differently from one another.
* Implement other types of characters such as the miners' wives or the characters that run the facilities that miners and 
these other characters visit. 
* Create dynamic interactions between characters.
* Creating an economy.
* Adding new states.
* Implementing a death and health system.
* Implementing a GUI.
* Creating charts to visualize interactions within the state machine.
* Implementing zombies???