#Geoffrey Meric ID: 260950354
#Yilin Lyu ID: 260952140
#Luca Balan ID: 260950824
#Ziming Dong ID: 260951177
#Alexandre Manguian ID: 260950146

from card import*
from game import*
from arrangement import*

def draw(hand, top_discard, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):
    '''(list,int,bool,nest_list,int,int,int) -> str
    choose where to draw a card
    >>>draw([5,19,13],9,False,[[]],1,1,1)
    'discard'
    >>>draw([2,21,13,51],30,False,[[]],1,2,1)
    'stock'
    >>>draw([1,2,51],6,False,[[]],1,1,1)
    'discard' #Because 6 is wildcard
    '''
    #if top_discard is None,then return stock
    if top_discard == None:
        return 'stock'
    #draw card from the discard pile if top_discard is wildcard
    elif get_rank(top_discard) == wildcard_rank:
        return 'discard'
    
    #get the groups and sequences in hand
    arrangement = get_arrangement(tuple(hand), wildcard_rank)
    number = len(arrangement)
    
    #Check if the top_discard card can be added into groups or sequences for now
    #create a copy 
    new_hand = hand[:]
    unarranged_cards = list(new_hand)
    new_hand.append(top_discard)
    unarranged_cards_top = list(new_hand)
    arrangement_top = get_arrangement(tuple(new_hand), wildcard_rank)
    for seq in arrangement:
        for card in seq:
            unarranged_cards.remove(card)
    for seq in arrangement_top:
        for card in seq:
            unarranged_cards_top.remove(card)
    
    #Check if the top discard card can form a new group or sequence
    for i in new_hand:
        #test if by adding the top discard card, a new group or sequence will be formed
        new_arrangement = get_arrangement(tuple(new_hand), wildcard_rank)
        if len(new_arrangement) > number:
            return 'discard'    
    
    #Check if the top discard card has same rank or sequnce with card
    for card in unarranged_cards:
        if card - 1 <= top_discard <= card + 1:
            return 'discard'
        elif top_discard == card - 4 or top_discard == card + 4:
            return 'discard'

    # if no special case then return stock
    return 'stock'



def discard(hand, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):
    '''(list,bool,nest_list,int,int,int) -> int
    choose which card to discard
    >>>discard([5,19,13,9],False,[[]],1,1,1)
    19
    >>>discard([2,21,13,51,30],False,[[]],1,2,1)
    51
    >>>discard([1,2,51,6],False,[[]],1,1,1)
    51 #Because 6 is wildcard
    '''
    #if this is last turn then we should choose discard card wisely
    if last_turn:
        #make a hand copy
        hand_copy = hand[:]
        #get combination of arrangement
        combinations = get_arrangement(tuple(hand), wildcard_rank) 
        for a_list in combinations:
            for i in a_list:
                hand_copy.remove(i) # we don't want to remove cards that for combinations
            
        hand_copy.sort() # sort the remaining cards
        #if we meet special case,then we discard the highest rank card
        if len(hand_copy) == 0:
            hand.sort()
            if get_rank(hand[-1] == 12):
                return hand[-2]
            else:
                return hand[-1]
        #if not we return highest rank card which is useless
        index_highest_card = max(hand_copy) # assigning the index of the highest card
        return index_highest_card
    #test if there exist a card,without it it could be a valid arrangement,and discard it
    for i in range(len(hand)):
        new_hand = hand[:]
        new_hand.remove(new_hand[i])
        arrangement = get_arrangement(tuple(new_hand), wildcard_rank)
        if is_valid_arrangement(tuple(arrangement), tuple(new_hand), wildcard_rank):
            return hand[i]
    #get combination of useful arrangement in hand    
    combinations = get_arrangement(tuple(hand), wildcard_rank)
    valid_card = []
    for i in combinations:
        for card in i:
            valid_card.append(card)#append valid card
    discard_card = []
    for card in hand:
        if card not in valid_card:
            discard_card.append(card)
    discard_card.sort()
    #check if there exist a very special case,and return highest rank card
    if len(discard_card) == 0:
        hand.sort()
        if get_rank(hand[-1] == 12):
                return hand[-2]
        else:
            return hand[-1]
    
    for card in discard_card:#just don't discard wildcard
        if get_rank(card) == wildcard_rank:
            discard_card.remove(card)
        if len(discard_card) == 1:
            return discard_card[-1]
            
    if len(discard_card) == 2 or len(discard_card) == 1:#beacuse if len(discard_card) is less than 2,then error would exist during follow for loop
        return discard_card[-1]
    #remove same rank cards if they are not in the valid
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
    #if there still have cards useless,then discard highest rank one
    return discard_card[-1]
