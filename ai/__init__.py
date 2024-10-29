from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'ai'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # AI forecast data
    ai_data = [3038, 2906, 3585, 3359, 3460, 3792, 3963, 4061, 3411, 3580, 3317, 3546, 3308, 3129, 3868, 3658, 3776, 4075, 4266, 4377]
    past_demand_data_block = [2913, 3238, 3340, 3401, 2898, 3055, 2807, 2990, 2764, 2666, 3246, 3137, 3248, 3494, 3582, 3798, 3189, 3288, 3075, 3209]
    demand_data_block = [3013, 2805, 3525, 3391, 3544, 3713, 3919, 4041, 3238, 3429, 3166, 3546, 3346, 3159, 3901, 3651, 3776, 3995, 4325, 4613]

    label_dict = {'Q21': 'Week 21 forecast value: 3038 units. Will you keep it?',
                  'Q22': 'Week 22 forecast value: 2906 units. Will you keep it?',
                  'Q23': 'Week 23 forecast value: 3585 units. Will you keep it?',
                  'Q24': 'Week 24 forecast value: 3359 units. Will you keep it?',
                  'Q25': 'Week 25 forecast value: 3460 units. Will you keep it?',
                  'Q26': 'Week 26 forecast value: 3792 units. Will you keep it?',
                  'Q27': 'Week 27 forecast value: 3963 units. Will you keep it?',
                  'Q28': 'Week 28 forecast value: 4061 units. Will you keep it?',
                  'Q29': 'Week 29 forecast value: 3411 units. Will you keep it?',
                  'Q30': 'Week 30 forecast value: 3580 units. Will you keep it?',
                  'Q31': 'Week 31 forecast value: 3317 units. Will you keep it?',
                  'Q32': 'Week 32 forecast value: 3546 units. Will you keep it?',
                  'Q33': 'Week 33 forecast value: 3308 units. Will you keep it?',
                  'Q34': 'Week 34 forecast value: 3129 units. Will you keep it?',
                  'Q35': 'Week 35 forecast value: 3868 units. Will you keep it?',
                  'Q36': 'Week 36 forecast value: 3658 units. Will you keep it?',
                  'Q37': 'Week 37 forecast value: 3776 units. Will you keep it?',
                  'Q38': 'Week 38 forecast value: 4075 units. Will you keep it?',
                  'Q39': 'Week 39 forecast value: 4266 units. Will you keep it?',
                  'Q40': 'Week 40 forecast value: 4377 units. Will you keep it?'}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field(label=None):
    return models.IntegerField(
        label='<b>If No, Please provide your forecast here</b>', null=True, blank=True, min=100, max=15000
    )


class Player(BasePlayer):
    Q21 = models.BooleanField(label='')
    Q21a = make_field()
    Q21b = models.IntegerField()
    Q22 = models.BooleanField(label='')
    Q22a = make_field()
    Q22b = models.IntegerField()
    Q23 = models.BooleanField(label='')
    Q23a = make_field()
    Q23b = models.IntegerField()
    Q24 = models.BooleanField(label='')
    Q24a = make_field()
    Q24b = models.IntegerField()
    Q25 = models.BooleanField(label='')
    Q25a = make_field()
    Q25b = models.IntegerField()
    Q26 = models.BooleanField(label='')
    Q26a = make_field()
    Q26b = models.IntegerField()
    Q27 = models.BooleanField(label='')
    Q27a = make_field()
    Q27b = models.IntegerField()
    Q28 = models.BooleanField(label='')
    Q28a = make_field()
    Q28b = models.IntegerField()
    Q29 = models.BooleanField(label='')
    Q29a = make_field()
    Q29b = models.IntegerField()
    Q30 = models.BooleanField(label='')
    Q30a = make_field()
    Q30b = models.IntegerField()
    Q31 = models.BooleanField(label='')
    Q31a = make_field()
    Q31b = models.IntegerField()
    Q32 = models.BooleanField(label='')
    Q32a = make_field()
    Q32b = models.IntegerField()
    Q33 = models.BooleanField(label='')
    Q33a = make_field()
    Q33b = models.IntegerField()
    Q34 = models.BooleanField(label='')
    Q34a = make_field()
    Q34b = models.IntegerField()
    Q35 = models.BooleanField(label='')
    Q35a = make_field()
    Q35b = models.IntegerField()
    Q36 = models.BooleanField(label='')
    Q36a = make_field()
    Q36b = models.IntegerField()
    Q37 = models.BooleanField(label='')
    Q37a = make_field()
    Q37b = models.IntegerField()
    Q38 = models.BooleanField(label='')
    Q38a = make_field()
    Q38b = models.IntegerField()
    Q39 = models.BooleanField(label='')
    Q39a = make_field()
    Q39b = models.IntegerField()
    Q40 = models.BooleanField(label='')
    Q40a = make_field()
    Q40b = models.IntegerField()

    # demographic questions
    Q80 = models.CharField(max_length=40, label='What is Your Prolific ID (Provide it for any bonus payments):', blank=True)
    Q41 = models.StringField(widget=widgets.RadioSelect,
                             label='What is the highest level of education you have completed or currently pursuing?',
                             choices=((1, 'Less than high school'), (2, 'High school graduate'), (3, 'Some college '),
                                      (4, '4 year degree'), (5, 'Professional degree (e.g. JD, MD, etc)'),
                                      (6, 'Masters'), (7, 'Doctorate')))
    Q42 = models.IntegerField(label='What is your age?', min=18, max=120)
    Q43 = models.StringField(widget=widgets.RadioSelect, label='What is your current annual level of income?', choices=(
    (1, 'Less than $20,000'), (2, '$20,000 - $39,999'), (3, '$40,000 - $59,999'), (4, '$60,000 - $79,999'),
    (5, '$80,000 - $99,999'), (11, '$100,000 - $149,999'), (12, 'More than $150,000')))
    Q44 = models.StringField(widget=widgets.RadioSelect, label='What is your gender?',
                             choices=((1, 'Male'), (2, 'Female'), (3, 'Non-Binary'), (4, 'Other')))
    Q44_1 = models.StringField(blank=True)  # other gender
    Q45 = models.StringField(widget=widgets.RadioSelect, label='Choose one ethnicity you consider yourself to be.',
                             choices=((1, 'White'), (2, 'Black or African American'), (3, 'Hispanic'),
                                      (21, 'American Indian or Alaska Native'), (4, 'Asian'),
                                      (5, 'Native Hawaiian or Pacific Islander'), (6, 'Other')))

    # forecasting questions
    Q46 = models.StringField(widget=widgets.RadioSelect,
                             label="Have you engaged in forecasting at your company or work place?",
                             choices=((1, 'Yes, I often do'), (2, 'Yes, I sometimes do'), (3, 'No, never at all')))
    Q47 = models.StringField(widget=widgets.RadioSelect, label="How comfortable are you with forecasting?", choices=(
    (1, 'Extremely uncomfortable'), (2, 'Somewhat uncomfortable'), (3, 'Neither comfortable nor uncomfortable'),
    (4, 'Somewhat comfortable'), (5, 'Extremely comfortable')))
    Q48 = models.StringField(widget=widgets.RadioSelect,
                             label="Have you used or are you using a Traditional forecasting system such as Exponential Smoothing for modeling or prediction?",
                             choices=(
                             (1, 'Definitely not'), (2, 'Probably not'), (3, 'Might or might not'), (4, 'Probably yes'),
                             (5, 'Definitely yes')))

    # likelyhood questions - financial
    Q13f1 = models.IntegerField(label='Betting 10% of your annual income at the horse races.', choices=(
    (1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')),
                                widget=widgets.RadioSelectHorizontal)
    Q13f2 = models.IntegerField(label='Investing 10% of your annual income in a moderate growth mutual fund ', choices=(
    (1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')),
                                widget=widgets.RadioSelectHorizontal)
    Q13f3 = models.IntegerField(label='Betting 10% of your annual income at a high-stake poker game', choices=(
    (1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')),
                                widget=widgets.RadioSelectHorizontal)
    Q13f4 = models.IntegerField(label='Investing 10% of your annual income in a very speculative stock. ', choices=(
    (1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')),
                                widget=widgets.RadioSelectHorizontal)
    Q13f5 = models.IntegerField(label='Betting 10% of your annual income on the outcome of a sporting event ', choices=(
    (1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')),
                                widget=widgets.RadioSelectHorizontal)
    Q13f6 = models.IntegerField(label='Investing 10% of your annual income in a new business venture. ', choices=(
    (1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')),
                                widget=widgets.RadioSelectHorizontal)

    Q14 = models.IntegerField(label='How many forecasting courses have you taken in college?',
                              choices=((0, 'None'), (1, '1'), (2, '2 or more')), widget=widgets.RadioSelect)
    Q15 = models.IntegerField(label='How will you rate your analytical ability?', choices=([i for i in range(0, 11)]),
                              widget=widgets.RadioSelectHorizontal)

    table_data = models.LongStringField()
    consent = models.BooleanField(label="", choices=(
    (True, "I am at least 18 years old, have read the consent information, and agree to take part in the research."),
    (False, "No, I disagree")))

    # CAT
    cat1 = models.IntegerField(
        label='1. If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how many days would it take them to drink one barrel of water together?', )
    cat2 = models.IntegerField(
        label='2. Jerry received both the 15th highest and the 15th lowest mark in the class. How many students are in the class?', )
    cat3 = models.IntegerField(
        label='3. A man buys a pig for $60, sells it for $70, buys it back for $80, and sells it finally for $90. How much has he made?', )
    cat4 = models.StringField(widget=widgets.RadioSelect,
                              label="4. Simon decided to invest $8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks went down by 50%. Three months later, on October 17, the stocks went up 75%. At this point, what has happened to the $8,000 Simon invested?",
                              choices=((1, 'broken even in the stock market'), (2, 'is ahead of where he began'),
                                       (3, 'has lost money')))

    # NT
    nt1 = models.FloatField(min=0, max=1,
                            label='1. Out of 1,000 people in a small town 500 are members of a choir. Out of these 500 members in the choir 100 are men. Out of the 500 inhabitants that are not in the choir 300 are men. What is the probability that a randomly drawn man is a member of the choir?', )
    nt2 = models.FloatField(min=0, max=1,
                            label='2. Imagine we are throwing a five-sided die 50 times. On average, out of these 50 throws how many times would this five-sided die show an odd number (1, 3 or 5)?', )
    nt3 = models.FloatField(min=0, max=1,
                            label='3. In a forest 20% of mushrooms are red, 50% brown and 30% white. A red mushroom is poisonous with a probability of 20%. A mushroom that is not red is poisonous with a probability of 5%. What is the probability that a poisonous mushroom in the forest is red?', )

    #Prolific ID


# PAGES


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        player.participant.vars['prev'] = 0


class ConsentOk(Page):
    # only participate if they consent
    @staticmethod
    def is_displayed(player):
        return player.consent


# --- get method for player data
def get_your_forecast_data_block(p):
    # get the prev variable to determine the data range
    prev = p.participant.vars['prev']
    if prev == 0:
        return []

    data = []
    forecast_data = []
    agree_data = []

    for i in range(21, 41):
        agree_data.append(p.field_maybe_none(f'Q{i}'))
        forecast_data.append(p.field_maybe_none(f'Q{i}a'))

    for i in range(0, prev):
        if agree_data[i]:
            data.append(C.ai_data[i])
        else:
            data.append(forecast_data[i])
    return data


# ------

# get CMAPE error
def cumulative_average(numbers):
    cumulative_list = []
    total_sum = 0
    for i, num in enumerate(numbers):
        total_sum += num
        average = round(total_sum / (i + 1), 2)
        cumulative_list.append(average)
    return cumulative_list


def get_cmape_error(p):
    prev = p.participant.vars['prev']
    if prev == 0:
        return []

    # get all previous forecast
    prev_ai_data = C.ai_data[:prev]
    your_prev_data = []
    for i in range(21, prev + 21):
        if p.field_maybe_none(f'Q{i}'):
            your_prev_data.append(C.ai_data[i - 21])
        else:
            your_prev_data.append(p.field_maybe_none(f'Q{i}a'))

    n = len(prev_ai_data)

    cmape_ai_error_block = []
    cmape_your_error_block = []

    for i in range(0, n):
        ai_dd_diff = abs(C.demand_data_block[i] - prev_ai_data[i])
        your_dd_diff = abs(C.demand_data_block[i] - your_prev_data[i])

        ai_sum = round(ai_dd_diff / C.demand_data_block[i], 3) * 100
        your_sum = round(your_dd_diff / C.demand_data_block[i], 3) * 100

        cmape_ai_error_block.append(ai_sum)
        cmape_your_error_block.append(your_sum)

    return cumulative_average(cmape_ai_error_block), cumulative_average(cmape_your_error_block)


class BlockQs(ConsentOk):
    template_name = "ai/Forecast.html"

    @staticmethod
    def error_message(player, values):
        v_list = []
        for k, v in values.items():
            v_list.append(k)
            if v is False:
                v_list.append(0)
            elif v is True:
                v_list.append(1)
            elif v is None:
                v_list.append(0)
            else:
                v_list.append(v)
                # ['Q21', False, 'Q21a', None]
        week = v_list[0][1:]
        if v_list[1] == 0 and v_list[3] == 0:
            return f'Please provide your forecast for week {week}!'
        if v_list[1] == 1 and v_list[3]:
            return f"You've selected to keep the forecast for week {week}!"

    @staticmethod
    def vars_for_template(player):
        # get previous page
        prev = player.participant.vars['prev']
        # reset to 0 if 20
        if prev == 20:
            prev = 0
            player.participant.vars['prev'] = prev

        table_data_horizontal = []

        if prev == 0:
            table_data = [[]]
        else:
            import ast
            table_data = ast.literal_eval(player.table_data)
            # reshape the data
            for j in reversed(range(len(table_data[0]))):
                row_data = []
                for i in table_data:
                    row_data.append(i[j])
                table_data_horizontal.append(row_data)

        current = prev + 1
        qn_n = current + 20

        # get prev round data, and calculate ai error, forecast error
        if prev == 0:
            prev_error = []
        else:
            if player.field_maybe_none(f'Q{prev + 20}'):
                prev_data = C.ai_data[prev - 1]
            else:
                prev_data = player.field_maybe_none(f'Q{prev + 20}a')

            ai_error = abs(C.demand_data_block[prev - 1] - C.ai_data[prev - 1])
            your_error = abs(C.demand_data_block[prev - 1] - prev_data)
            prev_error = [prev + 20, ai_error, your_error, get_cmape_error(player)[1][-1]]

        return dict(
            qn=current,
            qn_n=qn_n,
            label=C.label_dict['Q' + str(qn_n)],
            week_data=C.ai_data[prev],
            table_data=table_data_horizontal,
            prev_error=prev_error,
            start=False if prev == 0 else True,
        )

    @staticmethod
    def js_vars(player):
        prev = player.participant.vars['prev']

        label_block = [f'Week {i}' for i in range(1, 21)]
        demand_block = C.past_demand_data_block.copy()
        ai_data_block = [0] * 20
        your_data_block = [0] * 20
        abs_ai_cmape = [0] * 20
        abs_your_cmape = [0] * 20

        if prev > 0:
            dd_data = C.demand_data_block[:prev].copy()
            ai_data = C.ai_data[:prev].copy()
            your_data = get_your_forecast_data_block(player)

            label_block.extend([f'Week {i}' for i in range(21, prev + 21)])
            ai_data_block.extend(ai_data)
            demand_block.extend(dd_data)
            your_data_block.extend(your_data)

            cmape_data_blocks = get_cmape_error(player)

            # CMAPE blocks
            abs_ai_cmape.extend(cmape_data_blocks[0])
            abs_your_cmape.extend(cmape_data_blocks[1])

        ai_forecast_error = [0] * 20
        abs_forecast_error = [0] * 20

        for i in range(20, len(label_block)):
            abs_error = abs(demand_block[i] - your_data_block[i])
            ai_error = abs(demand_block[i] - ai_data_block[i])
            abs_forecast_error.extend([abs_error])
            ai_forecast_error.extend([ai_error])
        table_data_block = [label_block, demand_block, ai_data_block, ai_forecast_error, abs_ai_cmape, your_data_block,
                            abs_forecast_error, abs_your_cmape]
        player.table_data = str(table_data_block)

        return dict(
            label_block=label_block,
            ai_data_block=ai_data_block,
            your_data_block=your_data_block,
            actual_demand_block=demand_block,
        )


class Graph(ConsentOk):
    @staticmethod
    def vars_for_template(player):
        prev = player.participant.vars['prev']
        table_data_horizontal = []

        if prev == 0:
            table_data = [[]]
        else:
            import ast
            table_data = ast.literal_eval(player.table_data)
            # reshape the data
            for j in reversed(range(len(table_data[0]))):
                row_data = []
                for i in table_data:
                    row_data.append(i[j])
                table_data_horizontal.append(row_data)

        return dict(
            table_data=table_data_horizontal,
        )

    @staticmethod
    def js_vars(player):
        prev = player.participant.vars['prev']

        label_block = [f'Week {i}' for i in range(1, 21)]
        demand_block = C.past_demand_data_block.copy()
        ai_data_block = [0] * 20
        your_data_block = [0] * 20
        abs_ai_cmape = [0] * 20
        abs_your_cmape = [0] * 20

        if prev > 0:
            dd_data = C.demand_data_block[:prev].copy()
            ai_data = C.ai_data[:prev].copy()
            your_data = get_your_forecast_data_block(player)

            label_block.extend([f'Week {i}' for i in range(21, prev + 21)])
            ai_data_block.extend(ai_data)
            demand_block.extend(dd_data)
            your_data_block.extend(your_data)

            cmape_data_blocks = get_cmape_error(player)

            # CMAPE blocks
            abs_ai_cmape.extend(cmape_data_blocks[0])
            abs_your_cmape.extend(cmape_data_blocks[1])

        ai_forecast_error = [0] * 20
        abs_forecast_error = [0] * 20

        for i in range(20, len(label_block)):
            abs_error = abs(demand_block[i] - your_data_block[i])
            ai_error = abs(demand_block[i] - ai_data_block[i])
            abs_forecast_error.extend([abs_error])
            ai_forecast_error.extend([ai_error])
        table_data_block = [label_block, demand_block, ai_data_block, ai_forecast_error, abs_ai_cmape, your_data_block,
                            abs_forecast_error, abs_your_cmape]
        player.table_data = str(table_data_block)

        return dict(
            label_block=label_block,
            ai_data_block=ai_data_block,
            your_data_block=your_data_block,
            actual_demand_block=demand_block,
        )


# each question on a separate page ---
class BlockQ21(BlockQs):
    form_model = 'player'
    form_fields = ['Q21', 'Q21a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        if player.participant.vars['prev'] == 20:
            player.participant.vars['prev'] = 1
        player.participant.vars['prev'] = 1
        # save the ai data value
        player.Q21b = C.ai_data[0]


class BlockQ22(BlockQs):
    form_model = 'player'
    form_fields = ['Q22', 'Q22a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 2
        # save the ai data value
        player.Q22b = C.ai_data[1]


class BlockQ23(BlockQs):
    form_model = 'player'
    form_fields = ['Q23', 'Q23a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 3
        # save the ai data value
        player.Q23b = C.ai_data[2]


class BlockQ24(BlockQs):
    form_model = 'player'
    form_fields = ['Q24', 'Q24a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 4
        # save the ai data value
        player.Q24b = C.ai_data[3]


class BlockQ25(BlockQs):
    form_model = 'player'
    form_fields = ['Q25', 'Q25a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 5
        # save the ai data value
        player.Q25b = C.ai_data[4]


class BlockQ26(BlockQs):
    form_model = 'player'
    form_fields = ['Q26', 'Q26a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 6
        # save the ai data value
        player.Q26b = C.ai_data[5]


class BlockQ27(BlockQs):
    form_model = 'player'
    form_fields = ['Q27', 'Q27a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 7
        # save the ai data value
        player.Q27b = C.ai_data[6]


class BlockQ28(BlockQs):
    form_model = 'player'
    form_fields = ['Q28', 'Q28a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 8
        # save the ai data value
        player.Q28b = C.ai_data[7]


class BlockQ29(BlockQs):
    form_model = 'player'
    form_fields = ['Q29', 'Q29a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 9
        # save the ai data value
        player.Q29b = C.ai_data[8]


class BlockQ30(BlockQs):
    form_model = 'player'
    form_fields = ['Q30', 'Q30a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 10
        # save the ai data value
        player.Q30b = C.ai_data[9]


class BlockQ31(BlockQs):
    form_model = 'player'
    form_fields = ['Q31', 'Q31a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 11
        # save the ai data value
        player.Q31b = C.ai_data[10]


class BlockQ32(BlockQs):
    form_model = 'player'
    form_fields = ['Q32', 'Q32a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 12
        # save the ai data value
        player.Q32b = C.ai_data[11]


class BlockQ33(BlockQs):
    form_model = 'player'
    form_fields = ['Q33', 'Q33a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 13
        # save the ai data value
        player.Q33b = C.ai_data[12]


class BlockQ34(BlockQs):
    form_model = 'player'
    form_fields = ['Q34', 'Q34a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 14
        # save the ai data value
        player.Q34b = C.ai_data[13]


class BlockQ35(BlockQs):
    form_model = 'player'
    form_fields = ['Q35', 'Q35a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 15
        # save the ai data value
        player.Q35b = C.ai_data[14]


class BlockQ36(BlockQs):
    form_model = 'player'
    form_fields = ['Q36', 'Q36a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 16
        # save the ai data value
        player.Q36b = C.ai_data[15]


class BlockQ37(BlockQs):
    form_model = 'player'
    form_fields = ['Q37', 'Q37a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 17
        # save the ai data value
        player.Q37b = C.ai_data[16]


class BlockQ38(BlockQs):
    form_model = 'player'
    form_fields = ['Q38', 'Q38a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 18
        # save the ai data value
        player.Q38b = C.ai_data[17]


class BlockQ39(BlockQs):
    form_model = 'player'
    form_fields = ['Q39', 'Q39a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 19
        # save the ai data value
        player.Q39b = C.ai_data[18]


class BlockQ40(BlockQs):
    form_model = 'player'
    form_fields = ['Q40', 'Q40a']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        # a variable to capture the previous page
        player.participant.vars['prev'] = 20
        # save the ai data value
        player.Q40b = C.ai_data[19]


# -------------------------------


# ------ other pages -----
class Block6(ConsentOk):
    # survey page
    template_name = "ai/Survey.html"

    form_model = 'player'
    form_fields = ['Q80','Q41', 'Q42', 'Q43', 'Q44', 'Q44_1', 'Q45']

    @staticmethod
    def is_displayed(player):
        return player.consent


class Instruction(ConsentOk):
    pass


class Block7(ConsentOk):
    # forecasting survey
    template_name = "ai/Survey2.html"

    form_model = 'player'
    form_fields = ['Q46', 'Q47', 'Q48']


class Block8(ConsentOk):
    # Likelyhood - behavioral traits
    template_name = "ai/Likely.html"

    form_model = 'player'
    form_fields = ['Q13f1', 'Q13f2', 'Q13f3', 'Q13f4', 'Q13f5', 'Q13f6', 'Q14', 'Q15']


class CAT(ConsentOk):
    form_model = 'player'
    form_fields = ['cat1', 'cat2', 'cat3', 'cat4']


class NT(ConsentOk):
    form_model = 'player'
    form_fields = ['nt1', 'nt2', 'nt3']



class Block9(Page):
    # last page / thank you
    template_name = "ai/Thanks.html"





# ----end other pages ---------

page_sequence = [Consent, Block6, Instruction, BlockQ21, BlockQ22, BlockQ23, BlockQ24, BlockQ25, BlockQ26, BlockQ27,
                 BlockQ28, BlockQ29, BlockQ30, BlockQ31, BlockQ32, BlockQ33, BlockQ34, BlockQ35, BlockQ36, BlockQ37,
                 BlockQ38, BlockQ39, BlockQ40, Graph, Block7, Block8, CAT, NT, Block9]
