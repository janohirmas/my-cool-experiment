from otree.api import *
import random 

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iNumber1 = models.IntegerField()
    iNumber2 = models.IntegerField()
    iDec = models.IntegerField()
    dRT = models.FloatField()
    bCorrect = models.BooleanField()
    sInstructions = models.StringField()
    sLongText = models.LongStringField()
# FUNCTIONS 

def creating_session(subsession):
    for player in subsession.get_players():
        # Between-subject info
        if player.round_number == 1:
            p = player.participant
            p.iTreat = random.randint(0,1)
            p.iSelectedTrial = random.randint(1,C.NUM_ROUNDS)
            print( p.iSelectedTrial)
        # within-subject (every round)
        player.iNumber1 = random.randint(1,10)
        player.iNumber2 = random.randint(1,10)



# PAGES
class between(Page):
    pass

class Decision(Page):
    
    # All the things recorded in the page
    form_model = 'player'
    form_fields = ['iDec','dRT']

    @staticmethod 
    def vars_for_template(player: Player):

        return dict(
            iNumber1 = player.iNumber1,
            iNumber2 = player.iNumber2,
            list = ['a','n']
        )
    
    @staticmethod
    def js_vars(player: Player):
        return dict(
          
        )
    
    # @staticmethod 
    # def is_displayed(player: Player):
    #     return True

    @staticmethod 
    def before_next_page(player: Player, timeout_happened):
        p = player.participant 
        player.bCorrect = (player.iNumber1 + player.iNumber2 == player.iDec)
        if p.iSelectedTrial==player.round_number:
            p.iDec = player.iDec 
            p.bOutcome = player.bCorrect
            print(player.bCorrect)



page_sequence = [between,Decision]
