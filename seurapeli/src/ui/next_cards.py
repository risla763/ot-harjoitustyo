from card_deck import Card

def draw_next(surface, pos,card): #surface on näyttö , jolle kortti vedetään
        card.rect.topleft = pos #tuple
        surface.blit(card.image, card.rect)