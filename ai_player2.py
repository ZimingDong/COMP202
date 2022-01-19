from card import*
from game import*
from arrangement import*

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
            return 'discard'
        
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
    if last_turn:
        hand_copy = hand[:]   
                
        combinations = get_arrangement(tuple(hand), wildcard_rank) 
        for a_list in combinations:
            for i in a_list:
                hand_copy.remove(i) # we don't want to remove cards that for combinations
            
        hand_copy.sort() # sort the remaining cards
        if len(hand_copy) == 0:
            hand.sort()
            return hand[-1]
        index_highest_card = max(hand_copy) # assigning the index of the highest card
        return index_highest_card
    #test if there exist a card,without it it could be a valid arrangement,and discard it
    for i in range(len(hand)):
        new_hand = hand[:]
        new_hand.remove(new_hand[i])
        arrangement = get_arrangement(tuple(new_hand), wildcard_rank)
        if is_valid_arrangement(tuple(arrangement), tuple(new_hand), wildcard_rank):
            return hand[i]
        
    combinations = get_arrangement(tuple(hand), wildcard_rank)
    valid_card = []
    for i in combinations:
        for card in i:
            valid_card.append(card)
    discard_card = []
    for card in hand:
        if card not in valid_card:
            discard_card.append(card)
    discard_card.sort()
    if len(discard_card) == 0:#it's wried because idk why it could be zero,so maybe you could improve it.
        hand.sort()
        return hand[-1]
    
    for card in discard_card:#just don't discard wildcard
        if get_rank(card) == wildcard_rank:
            discard_card.remove(card)
        if len(discard_card) == 1:
            return discard_card[-1]
            
    if len(discard_card) == 2 or len(discard_card) == 1:#beacuse if len(discard_card) is less than 2,then error would exist during follow for loop
        return discard_card[-1]
    #remove same rank card if they are not in the valid
    discard_remove = []
    for i in range(len(discard_card)-1):
        if same_rank(discard_card[i],discard_card[i+1]):
            discard_remove.append(discard_card[i])
            discard_remove.append(discard_card[i+1])
    for card in discard_remove:
        discard_card.remove(card)
        if len(discard_card) == 1:
            return discard_card[-1]
        
    discard_remove = []
    if len(discard_card) == 2 or len(discard_card) == 1:
        return discard_card[-1]
    #remove same suit and consecutive cards and if they are not in the valid
    for i in range(len(discard_card)-1):
        if same_suit(discard_card[i],discard_card[i+1]):
            if get_suit(discard_card[i]) + 1 == get_suit(discard_card[i+1]):
                discard_remove.append(discard_card[i])
                discard_remove.append(discard_card[i+1])
    for card in discard_remove:
        discard_card.remove(card)
        if len(discard_card) == 1:
            return discard_card[-1]    
    discard_remove = []
    if len(discard_card) == 2 or len(discard_card) == 1:
        return discard_card[-1]
    #remove same suit and nearby rank cards and if they are not in the valid
    for i in range(len(discard_card)-1):
        if same_suit(discard_card[i],discard_card[i+1]):
            if get_suit(discard_card[i]) + 2 == get_suit(discard_card[i+1]):
                discard_remove.append(discard_card[i])
                discard_remove.append(discard_card[i+1])
    for card in discard_remove:
        discard_card.remove(card)
        if len(discard_card) == 1:
            return discard_card[-1]
    return discard_card[-1]

