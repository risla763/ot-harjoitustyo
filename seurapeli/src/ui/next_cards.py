from card_deck import Card
"""This method draws the next card that is drawn from the deck."""
def draw_next(surface, pos,card): #surface on näyttö , jolle kortti vedetään
        card.rect.topleft = pos #tuple
        surface.blit(card.image, card.rect)