from arrangement import *
def draw(hand, top_discard, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):
    '''


    >>> draw([1,2,3,5,7,37,26],4,True,[[]],1,1,1)) #This is a case when adding to existing group or sequence
    'discard'
    >>> draw([1,2,3,5,7,37,26],6,True,[[]],1,1,1)) #This is a case when forming a new group or sequence
    'discard'
    '''
    
    #immediately draw card from stock if there's nothing in the discard pile
    if top_discard == None:
        return 'stock'
    #draw card from the discard pile if someone accidentally discarded a wildcard
    elif get_rank(top_discard) == wildcard_rank:
        return 'discard'
    
    #get the current number of groups and sequences in hand
    arrangement = get_arrangement(tuple(hand), wildcard_rank)
    number = len(arrangement)
    
    
    #1. Check if the top_discard card can be added into existing groups or sequences
    #create a shallow copy of cards in hand plus the 
    h = hand[:]
    unarranged_cards = list(h)
    h.append(top_discard)
    unarranged_cards_top = list(h)
    arrangement_top = get_arrangement(tuple(h), wildcard_rank)
    for seq in arrangement:
        for card in seq:
            unarranged_cards.remove(card)
    for seq in arrangement_top:
        for card in seq:
            unarranged_cards_top.remove(card)

    #2. Check if the top discard card can form a new group or sequence
    for i in h:
        #test if by adding the top discard card, a new group or sequence will be formed
        new_arrangement = get_arrangement(tuple(h), wildcard_rank)
        if len(new_arrangement) > number:
            return 'discard'    
    
    
    #3. Check if the top discard card has the potential of forming a group or sequnce with card in hand
    for card in unarranged_cards:
        if card - 1 <= top_discard <= card + 1:
            return 'discard'
        elif top_discard == card - 4 or top_discard == card + 4:
            return 'discard'

    
    return 'stock'
def get_penalty_pts(card):
    points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
    penalty_pts = points[RANKS.index(get_rank(card))]
    return penalty_pts


#largest card last turn
#min seq largest
#discard seq of 4 first
def discard(hand, last_turn, picked_up_discard_cards, player_position, wildcard_rank, num_turns_this_round):
    '''


    >>> discard([1,5,6,7,9,46,47,48], False, [[]], 1, 5, 9)
    9
    >>> discard([1,2,3,46,47,48,5,6,7], False, [[]], 1, 5, 9)
    3
    >>> discard([1,5,9,46,47,48,2,3,4], False, [[]], 1, 5, 9)
    4
    >> discard([2,8,9,46,47,48], False, [[]], 1, 5, 9) #will not discard 9 because 8 and 9 have higher chances of forming seq
    2
    '''
    
    arrangement = get_arrangement(tuple(hand), wildcard_rank)
    unarranged_cards = list(hand)
    for seq in arrangement:
        for card in seq:
            unarranged_cards.remove(card)
    for card in unarranged_cards:
        if (card - 1) in unarranged_cards:
            unarranged_cards.remove(card)
            unarranged_cards.remove(card - 1)
            continue
        elif (card + 1) in unarranged_cards:
            unarranged_cards.remove(card)
            unarranged_cards.remove(card + 1)
            continue
        elif (card - 4) in unarranged_cards:
            unarranged_cards.remove(card)
            unarranged_cards.remove(card - 4)
        elif (card + 4) in unarranged_cards:
            unarranged_cards.remove(card)
            unarranged_cards.remove(card + 4)

    if len(unarranged_cards) > 0:
        max_penalty_pts = get_penalty_pts(unarranged_cards[0])
        discard_card = unarranged_cards[0]
        for card in unarranged_cards:
            penalty_pts = get_penalty_pts(card)
            if penalty_pts <= max_penalty_pts:
                continue
            else:
                max_penalty_pts = penalty_pts
                discard_card = card
        return discard_card
        
    else:
        #discard card in a sequence of 4 or more
        if len(arrangement) > 0:
            l_start = len(arrangement[0])
            for seq in arrangement:
                l_seq = len(seq)
                if l_seq <= l_start:
                    continue
                else:
                    l_start = l_seq
                    longest_seq = seq
                return longest_seq[-1]

        if last_turn:
            #discard card that will result in the least penalty
            pts_min = 0
            min_penalty_seq = arrangement[0]
            for card in arrangement[0]:
                pts_min += get_penalty_pts(card)
            for seq in arrangement:
                pts = 0
                for card in seq:
                    pts += get_penalty_pts(card)
                if pts >= pts_min:
                    continue
                else:
                    pts_min = pts
                    min_penalty_seq = seq
            return min_penalty_seq[-1]
        else:
            hand.sort()
            return hand[-1]





