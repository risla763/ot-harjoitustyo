from services.card_deck import Card
def draw_next(surface, pos,card): #surface on näyttö , jolle kortti vedetään
        """This method draws the next card from the deck.
        Args:
             surface: displays the pygame screen
             pos: a tuple where the card is drawn on the screen
             card: a new card drawn from the list of cards     
                """
        card.rect.topleft = pos #tuple
        surface.blit(card.image, card.rect)