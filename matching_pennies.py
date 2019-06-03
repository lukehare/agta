#Note: Tie-breaking rule used is if strategy is equal, choose heads ('H')
import matplotlib.pyplot as plt

p1_model = [0, 0] #This is the model kept by P1 - i.e. a model of P2
p2_model = [0, 0] #Model kept by P2 - i.e. a model of P1

#Initial guesses. WLOG assume P1 guesses 'H'. I will run this code twice, once
#for P2 also guessing 'H', and once for P2 guessing 'T'
p1_init = 'H' 
p2_init = 'T'

p1_guess = ''
p2_guess = ''

#A function to update the models (statistical mixed strategies) kept by each 
#player, depending on the guesses in the prior round
def update_models(guess1, guess2, mod1, mod2):
#If P1 guesses 'H', P2 adds 1 to entry 0 of its model, otherwise (if tails)
#add 1 to entry 1
    if guess1 == 'H':
        mod2[0] += 1
    else:
        mod2[1] += 1

#Likewise, if P2 guesses 'H', P1 adds 1 to entry 0, otherwise to entry 1    
    if guess2 == 'H':
        mod1[0] += 1
    else:
        mod1[1] += 1
        
    return mod1, mod2

#A function to play one round of the game
def play_round(mod1, mod2):
#If P1 thinks P2 will choose heads (number of heads greater than number of tails),
#also choose heads. Otherwise choose tails.
    if mod1[0] >= mod1[1]:
        guess1 = 'H'
    else:
        guess1 = 'T'
        
#If P2 thinks heads is less likely for P1, choose heads
#If number for each is equal up until now, also choose heads.
#Otherwise choose tails
    if mod2[0] <= mod2[1]:
        guess2 = 'H'
    else:
        guess2 = 'T'
        
    return guess1, guess2
     
#Update the models with the initial guesses
p1_model, p2_model = update_models(p1_init, p2_init, p1_model, p2_model)

#Setup lists that will hold probability of heads at every tenth round
p1_heads = []
p2_heads = []

#Play 100000 rounds. Make new guess each round, then update models.
#Add probability of heads for each player to list every 10 rounds, so that
#this can be plotted to show convergence to 0.5
for i in range(100000):
    p1_guess, p2_guess = play_round(p1_model, p2_model)
    p1_model, p2_model = update_models(p1_guess, p2_guess, p1_model, p2_model)
    
    if i%10 == 0:
#Probability of Player 1 choosing heads equal to statistical model chance of
#P2 choosing heads
        p1_heads.append(p2_model[0]/sum(p2_model))
        
#Probability of Player 1 choosing heads equal to statistical model chance of
#P2 choosing tails
        p2_heads.append(p1_model[1]/sum(p1_model))
    
#Probability of Player 1 choosing heads equal to statistical model chance of
#P2 choosing heads
print("Player 1 strategy: (", p2_model[0]/sum(p2_model),",", p2_model[1]/sum(p2_model), ")")

#Probability of Player 1 choosing heads equal to statistical model chance of
#P2 choosing tails
print("Player 2 strategy: (", p1_model[1]/sum(p1_model),",", p1_model[0]/sum(p1_model), ")")

#Plot probabilities to show convergence to 0.5
plt.figure(0)
plt.ylim(0,1)
plt.title("Probability of P1 choosing heads")
fig1 = plt.plot(p1_heads)

plt.figure(2)
plt.ylim(0,1)
plt.title("Probability of P2 choosing heads")
fig2 = plt.plot(p2_heads)

