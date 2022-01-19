from card import*
from arrangement import*
from game import*
def draw(hand, top_discard, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):
    if top_discard == None:
        return 'stock'
    
    if get_rank(top_discard) == wildcard_rank:
        return 'discard'
    

    new_hand = hand[:]
    new_hand.append(top_discard)
    arrangement = get_arrangement(tuple(new_hand), wildcard_rank)
    if is_valid_arrangement(arrangement, tuple(new_hand), wildcard_rank):
        return 'discard'
    
    discard_weight = 3
    
    discard_weight -= calculate_round_points([top_discard])
    
    for card in hand:
        if same_rank(card, top_discard):
            discard_weight += 6
        
    for card in hand:    
        if same_suit(card, top_discard):
            if get_rank(card) == get_rank(top_discard) + 1:
                discard_weight += 4
            if get_rank(card) == get_rank(top_discard) - 1:
                discard_weight += 4
            if get_rank(card) == get_rank(top_discard) + 2:
                discard_weight += 2
            if get_rank(card) == get_rank(top_discard) - 2:
                discard_weight += 2
            
    if discard_weight > 0:
        return 'discard'
    else:
        return 'stock'

    
def discard(hand, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):

    hand_copy = hand[:]
    # we basically just remove the highest rank card that isn't a wildcard and doesn't form a combination
    if last_turn:
        
        for card in hand:
            if get_rank(card) == wildcard_rank: # we don't want to remove wildcards if we have any
                wildcard_index = hand_copy.index(card)
                hand_copy.pop(wildcard_index)
        
        combinations = get_arrangement(tuple(hand), wildcard_rank) 
        for i in range(len(combinations)):
            hand_copy.pop(i) # we don't want to remove cards that for combinations
            
        hand_copy.sort() # sort the remaining cards
        index_highest_card = hand_copy.index(max(hand_copy)) # assigning the index of the highest card
        return hand_copy[index_highest_card] # remove the highest card
    
    
    
    # we are only going to consider discarding cards that don't form a combination and aren't wildcards
    
    # get_arrangement puts the cards in nested lists or tuples which complicated things here
    combinations = get_arrangement(tuple(hand), wildcard_rank)
    non_nested_list = []
    for i in combinations:
        for j in i:
            non_nested_list.append(j) # non_nested_list will contain the cards we don't want to discard
    
    
    # the cards that don't form a combination are placed in possible_card_to_discard
    possible_card_to_discard = []
    for card in hand:
        if card not in non_nested_list:
            possible_card_to_discard.append(card)
        
    #uses helper discard function to find index of card we want to discard    
    card_to_discard_index = helper_discard(possible_card_to_discard, num_turns_this_round)
    
    #returns card to be discarded
    if len(possible_card_to_discard) != 0:
        return possible_card_to_discard[card_to_discard_index]
    
    #IDK WHY THIS HAPPENS BUT SOMETIMES THE LENGTH OF THE LIST POSSIBLE_CARD_TO_DISCARD IS 0 SO WE GET INDEXERROR
    #EVEN THOUGH AT THAT POINT THE ROUND SHOULD BE OVER AND IF WE DONT RETURN A CARD THERES ANOTHER ERROR SO JUST
    #RETURN SOME RANDOM CARD:
    else:
        return hand[0]
        
    
        
        
#helper function to prioritize which cards to keep/discard by assigning weightings based on their penalty
#and the likeliness that they can form a group/sequence. Higher weight means we want to discard the card.
def helper_discard(possible_card_to_discard, num_turns_this_round):

    #store value of highest weight card as we iterate through possible cards to discard
    highest_weight = 0
    #stores index of highest weight card in possible cards to discard
    card_to_discard_index = 0
    
    #iterate through every card index in list of possible cards to discard
    for i in range(len(possible_card_to_discard)):
        #initializing weight of card
        weight = 0
        
        #multiplier based on number of turns this round used to assign the weight due to card penalty (later in
        #round we want to prioritize discarding high penalty cards more), caps out after 20 turns
        if num_turns_this_round <= 20:
            turn_multiplier = 0.05 + num_turns_this_round*0.05
        else:
            #after 20 rounds turn multiplier is capped out at 1, increasing weight of high penalty cards
            turn_multiplier = 1
        
        #increase weight by product of penalty score of card and turn multiplier (weight gets increased more by
        #a high penalty score in later turns as we'll have less chances to discard the high score card later)
        weight += turn_multiplier*calculate_round_points([possible_card_to_discard[i]])
        
        #iterate through every other card in list of possible cards to discard
        for j in range(len(possible_card_to_discard)):
        
            #check that our second card isn't our first card
            if j==i:
                continue

            #if there is another card which we are considering discarding with same rank as current card we are weighing,
            #reduce weight as the card has potential to become part of a group (2/3 of group already exists in hand)
            elif get_rank(possible_card_to_discard[i]) == get_rank(possible_card_to_discard[j]):
                weight -= 6
            
            #next 2 conditional statements check if other card has adjacent rank and same suit as current card. If yes,
            #reduce weight as the card has potential to become part of a sequence (2/3 of sequence already exist in hand)
            elif get_rank(possible_card_to_discard[i]) == get_rank(possible_card_to_discard[j]) + 1:
                if get_suit(possible_card_to_discard[i]) == get_suit(possible_card_to_discard[j]):
                    weight -= 4
                
            elif get_rank(possible_card_to_discard[i]) == get_rank(possible_card_to_discard[j]) - 1:
                if get_suit(possible_card_to_discard[i]) == get_suit(possible_card_to_discard[j]):
                    weight -= 4

            #next 2 conditional statements check if other card has rank 2 greater and same suit as current card. If yes,
            #reduce weight as the card has potential to become part of a sequence (2/3 of sequence already exist in hand)
            elif get_rank(possible_card_to_discard[i]) == get_rank(possible_card_to_discard[j]) + 2:
                if get_suit(possible_card_to_discard[i]) == get_suit(possible_card_to_discard[j]):
                    weight -= 2
        
            elif get_rank(possible_card_to_discard[i]) == get_rank(possible_card_to_discard[j]) - 2:
                 if get_suit(possible_card_to_discard[i]) == get_suit(possible_card_to_discard[j]):
                        weight -= 2
            
        #compare final weight of card to previous highest weight. If current card has a weight higher than previous highest weight,
        #we replace the previous highest weight with the current card's weight and store the current card's index
        
        if weight > highest_weight:
            highest_weight = weight
            card_to_discard_index = i
    
    return card_to_discard_index