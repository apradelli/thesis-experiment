from otree.api import *
import random
import csv
import json
from otree.api import safe_json
import time
import math
from datetime import datetime  
from datetime import timedelta 

author = 'MP'

doc = """
DAY 2
"""


class C(BaseConstants):
    NAME_IN_URL = 'pradelli_matrix'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    MATRIX_WIDTH = 7
    MATRIX_HEIGHT = 7
    DELAY_DAY2=4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    matrix_created = models.LongStringField()
    matrix_correct = models.LongStringField()
    num_errors = models.IntegerField(initial=0)
    payoff_puzzle=models.IntegerField(initial=0)
 

    QT3=models.StringField(choices=("0","180","100","-100"),widget=widgets.RadioSelect)


    treatment=models.StringField()
    role_t = models.StringField(choices=['player 1', 'player 2'], blank=True)
    group_M=models.IntegerField()
  
    

    q1=models.IntegerField(choices=range(1,6,1),widget=widgets.RadioSelectHorizontal)
    q2=models.IntegerField(choices=range(1,6,1),widget=widgets.RadioSelectHorizontal)
    q3=models.IntegerField(choices=range(1,6,1),widget=widgets.RadioSelectHorizontal)
    q4=models.IntegerField(choices=range(1,6,1),widget=widgets.RadioSelectHorizontal)
    q5=models.IntegerField(choices=range(1,6,1),widget=widgets.RadioSelectHorizontal)
    q6=models.IntegerField(choices=range(1,6,1),widget=widgets.RadioSelectHorizontal)

    choose=models.StringField(choices=("Task 3", "Task 4"),widget=widgets.RadioSelectHorizontal)

    #ChoiceQ1= models.StringField(choices= ("Now","At the end of the experiment"),widget=widgets.RadioSelect)
    ChoiceQ1= models.StringField(choices=("The payoff of Task 4","The payoff of Task 4 plus 40", "The payoff of Task 4 minus 40","The payoff of Task 4 minus 100"),widget=widgets.RadioSelect)                             

    
    QT4_1=models.IntegerField(choices=range(1,11,1),widget=widgets.RadioSelectHorizontal)
    QT4_2=models.StringField(choices=("proper nouns", "specialized vocabulary", "common nouns","verbs"), widget=widgets.RadioSelect)
    QT4_3=models.StringField(choices=("240","200", "180","100"),widget=widgets.RadioSelect )
    QT4_4=models.StringField(choices=("80","200", "180","100"),widget=widgets.RadioSelect) 
    

    word1=models.CharField()
    word2=models.CharField()
    word3=models.CharField()
    word4=models.CharField()
    word5=models.CharField()
    word6=models.CharField()
    word7=models.CharField()
    word8=models.CharField()
    word9=models.CharField()
    word10=models.CharField()  

    QO_1=models.StringField(choices=("Task 3", "Task 4"),widget=widgets.RadioSelect)
    QO_2=models.StringField(choices=("Yes", "No"),widget=widgets.RadioSelect)

           
    age = models.IntegerField(choices=range(15,99,1))
    gender=models.StringField(choices=("Male","Female","Non-binary","Prefer not to declare"))
    nationality= models.StringField(choices=('Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 
    'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 
    'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian',
     'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 
     'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 
     'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 
    'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 
    'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian',
     'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 
     'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian',
      'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 
      'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 
      'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 
      'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 
      'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian',
       'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese',
        'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 
        'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer',
         'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan',
          'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani',
           'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean'))
    education=models.StringField(choices=("Less than Secondary School Diploma", "Secondary School Diploma","Bachelor's Degree", "Master of Science", "PhD"))

def set_payoff_puzzle(player):
    player.participant.vars['round_to_pay'] = player.round_number
    if player.num_errors == 0:
        player.payoff_puzzle = 180
    else:
        player.payoff_puzzle = 100



def creating_session(subsession: Subsession):
    subsession.group_randomly()

    if subsession.round_number == 1:
        subsession.session.vars['correct'] = []
        fn = 'pradelli_Day2/static/picture/img.txt'
        with open(fn, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                subsession.session.vars['correct'].append(row)
            print(subsession.session.vars['correct'])
    
       
         
        matching_players = []

        for g in subsession.get_groups():
            for p in g.get_players():
                if subsession.round_number == 1:                    
                    if p.id_in_group % 2 == 0:
                        p.treatment = "individual"
                          
                    else:
                        p.treatment = "matching"
                        matching_players.append(p) # Add matching players to the list
                    p.participant.vars['treatment'] = p.treatment
                    if p.treatment == "matching":
                    # Assign group variable to players in the "matching" treatment
                        p.group_M = matching_players.index(p) // 2 + 1
                        p.participant.vars['group'] = p.group_M

                else:
                    p.treatment = p.participant.vars['treatment']
        
        matching_groups = [matching_players[i:i+2] for i in range(0, len(matching_players), 2)]

        for group in matching_groups:
            if len(group) == 2:
                group[0].role_t = 'player 1'
                group[1].role_t = 'player 2'




        #grouping variable
        # counter=0 
        # for i,p in enumerate (players_matching):
        #     if i % 2== 0:
        #         counter+=1 
        #     p.group_id=counter





        
    




# PAGES
#-----------------------------------------------------------------------------------------

# pages
#-----------------------------------------------------------------------------------------
class Task(Page):
    form_model = 'player'
    form_fields = ['matrix_created','num_errors']

        
    def is_displayed(player: Player):
        if player.round_number > 1:
            prev_round = player.in_round(player.round_number - 1)
        else:
            prev_round = player.in_round(player.round_number)
        return player.round_number<=2 or (player.round_number == 3 and prev_round.field_maybe_none('choose') == 'Task 3')
    
    
    @staticmethod
    def before_next_page(player,timeout_happened):
        set_payoff_puzzle(player)
                       
    @staticmethod
    def get_timeout_seconds(player: Player):
        return 60
    
    @staticmethod
    def vars_for_template(player: Player):
        player.matrix_correct = ''.join(player.subsession.session.vars['correct'][player.round_number-1])

        k = 0
        table = "<table clas=\"table-bordered\">"
        for i in range(C.MATRIX_HEIGHT):
            table += "<tr style=\"height:40px\">"
            for j in range(C.MATRIX_WIDTH):
                table += "<td id=\""+ str(k) +"\" class=\"mytd\" style=\"width:40px\"></td>"                
                k+=1
            table += "</tr>"
        table += "</table>"

        img_name = "/static/picture/p" + str(player.round_number) + ".png"

        return dict(
            matrix_width=C.MATRIX_WIDTH,
            matrix_height=C.MATRIX_HEIGHT,
            table=table,   
            img_name=img_name,
            payoff_puzzle=player.payoff_puzzle,        
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            matrix_width=C.MATRIX_WIDTH,
            matrix_height=C.MATRIX_HEIGHT,
            matrix_correct=player.matrix_correct,
            
        )

   

# -------------------------------------------------------------------------------------
class Final_Result(Page):
    @staticmethod
    def vars_for_template(player: Player):
        table = "<table class=\"table stripped\">"
        table += "<tr><th>Round</th><th>Number of errors</th></tr>"
        for p in player.in_all_rounds():
            table += "<tr><td>" + str(p.round_number) + "</td><td>" + str(p.num_errors) + "</td></tr>"
        table += "</table>"
        return dict(
            table=table,
        )
    
      

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    
class Welcome(Page):    
    def is_displayed(player: Player):
        return player.round_number == 1
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
		  	'date_Day1': (datetime.now() - timedelta(days=C.DELAY_DAY2)).strftime("%B %d, %Y"),}
    
        
class InstructionsT3(Page):
    def is_displayed(player: Player):
        return player.round_number == 1
    
    
class QuestionT3(Page):
    form_model= "player"
    form_fields=['QT3']
    def is_displayed(player: Player):
        return player.round_number == 1
    
    def error_message(player, values):
      if values["QT3"] != "100":
          return 'Incorrect answer'
    

class Choiceinstructions_baseline(Page):
    def is_displayed(player: Player):
        return player.round_number == 2 and player.participant.vars['treatment'] == 'individual'
    
class Choiceinstructions_treat(Page):
    def is_displayed(player: Player):
        return player.round_number == 2 and player.participant.vars['treatment'] == 'matching'

class Payoffchoice_treat(Page):
    def is_displayed(player: Player):
        return player.round_number == 2 and player.participant.vars['treatment'] == 'matching'

class Choice_Questions(Page):
    form_model= "player"
    form_fields=['ChoiceQ1']
    def is_displayed(player: Player):
        return player.round_number == 2 and player.participant.vars['treatment'] == 'matching'
    
    def error_message(player, values):
      
      if values["ChoiceQ1"] != "The payoff of Task 4 minus 40":
          return 'Incorrect answer question 2'
     
class Choice(Page):
    form_model= "player"
    form_fields=['choose']
    def is_displayed(player: Player):
        return player.round_number == 2

class Instructions_Task4(Page):
    def is_displayed(player: Player):
        return player.round_number==2 and player.field_maybe_none('choose') == 'Task 4'
    
class Expected_Success(Page):
    form_model= "player"
    form_fields=['QT4_1']
    def is_displayed(player: Player):
        return player.round_number==2 and player.field_maybe_none('choose') == 'Task 4'
       
class Questions_T4_Baseline(Page):
    form_model= "player"
    form_fields=['QT4_2','QT4_4']
    def is_displayed(player: Player):
        return player.round_number==2 and player.field_maybe_none('choose') == 'Task 4' and player.participant.vars['treatment'] == 'individual'  
    
    def error_message(player, values):
      if values["QT4_2"] != "common nouns":
          return 'Incorrect answer question 1'
      if values["QT4_4"] != "200":
          return 'Incorrect answer question 2'

class Questions_T4_Treat(Page):
    form_model= "player"
    form_fields=['QT4_2','QT4_3']
    def is_displayed(player: Player):
        return player.round_number==2 and player.field_maybe_none('choose') == 'Task 4' and player.participant.vars['treatment'] == 'matching'  
    
    def error_message(player, values):
      if values["QT4_2"] != "common nouns":
          return 'Incorrect answer question 1'
      if values["QT4_3"] != "200":
          return 'Incorrect answer question 2'

class Expectation_other(Page):
    form_model= "player"
    form_fields=['QO_1','QO_2']
    def is_displayed(player: Player):
        return (player.round_number==3 and player.participant.vars['treatment'] == 'matching') 
    

class Task4(Page):
    def is_displayed(player: Player):
        return player.round_number==2 and player.field_maybe_none('choose') == 'Task 4'

    
    timeout_seconds = 240
    form_model= "player"
    form_fields=['word1','word2','word3','word4','word5','word6','word7','word8','word9','word10']  

class Creativity(Page):
    form_model= "player"
    form_fields=['q1','q2','q3','q4','q5','q6']
    def is_displayed(player: Player):
        #return player.round_number==2
        return player.round_number==C.NUM_ROUNDS


class Demographics(Page):
    form_model= "player"
    form_fields=['age','gender','nationality','education']
    def is_displayed(player: Player):
        #return player.round_number==2
        return player.round_number==C.NUM_ROUNDS


class Results(Page):
    pass

class Final_Payoff_B(Page):
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS and player.participant.vars['treatment'] == 'individual'

class Final_Payoff_TR(Page):
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS and player.participant.vars['treatment'] == 'matching'


    
page_sequence = [Welcome, InstructionsT3, QuestionT3, Task, Choiceinstructions_baseline, Choiceinstructions_treat, Payoffchoice_treat, Choice_Questions, Choice, Instructions_Task4, Questions_T4_Baseline, Questions_T4_Treat, Expected_Success, Task4 ,Expectation_other, Creativity, Demographics, Final_Payoff_B, Final_Payoff_TR ]


