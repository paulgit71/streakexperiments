from otree.api import *
import random
import string


doc = """
Final hot-hand / gambler's fallacy experiment with statistical system-generated forecasts.
Participants observe forecast-performance blocks for periods 1-30.
Participants make forecast accept/reject decisions only for periods 31-40.
Perceived Accuracy Question (PAQ) and Confidence Level (CL) are asked after each block.
"""


# ---------------------------------------------------------------------
# Module-level constants.
# ---------------------------------------------------------------------

ACTUAL_DEMAND = [1420, 915, 1688, 1215, 1876, 784, 1326, 1762, 1018, 1547, 1904, 846, 1135, 1642, 731, 1298, 1815, 972, 1486, 1193, 1711, 808, 1364, 1920, 1057, 1579, 889, 1238, 1746, 764, 1452, 1831, 997, 1605, 1186, 1220, 1050, 1512, 970, 1342]

SYSTEM_FORECAST = [1368, 880, 1755, 1267, 1787, 845, 1217, 1893, 1080, 1460, 1986, 813, 1101, 1685, 749, 1262, 1870, 933, 1550, 1219, 1622, 760, 1451, 2047, 1135, 1460, 965, 1117, 1595, 712, 1528, 1914, 957, 1543, 1215, 1262, 1092, 1577, 1019, 1424]

# Displayed System APE values. Periods 36-40 follow the requested APE targets.
SYSTEM_APE = [3.66, 3.83, 3.97, 4.28, 4.74, 7.78, 8.22, 7.43, 6.09, 5.62, 4.31, 3.9, 3.0, 2.62, 2.46, 2.77, 3.03, 4.01, 4.31, 2.49, 5.2, 5.94, 6.38, 6.61, 7.38, 7.54, 8.55, 9.77, 8.65, 6.81, 5.23, 4.53, 4.01, 3.86, 2.45, 3.43, 3.99, 4.32, 5.01, 6.12]

# Display-only "Your APE" values used on pre-decision PAQ pages.
# None means the column should be blank or hidden depending on the PAQ page.
DISPLAY_YOUR_APE = {1: None, 2: None, 3: None, 4: None, 5: None, 6: 10.69, 7: 7.91, 8: 7.43, 9: 8.71, 10: 5.62, 11: 6.22, 12: 7.33, 13: 3.47, 14: 5.53, 15: 1.42, 16: None, 17: None, 18: None, 19: 2.21, 20: 6.62, 21: 7.76, 22: 4.55, 23: 8.13, 24: 4.47, 25: 7.38, 26: 7.54, 27: 4.27, 28: 10.21, 29: None, 30: None, 31: None, 32: None, 33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None}

# Periods 1-30 are observation/feedback periods. Periods 31-40 are decision periods.
STAGE = ['observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'observation', 'decision', 'decision', 'decision', 'decision', 'decision', 'decision', 'decision', 'decision', 'decision', 'decision']

CONDITION = ['observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'observation_feedback', 'decision_streak', 'decision_streak', 'decision_streak', 'decision_streak', 'decision_streak', 'decision_streak', 'decision_streak', 'decision_mixed_control', 'decision_mixed_control', 'decision_mixed_control']

BLOCK_ID = [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12]

BLOCK_LENGTH = [5, 5, 5, 5, 5, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 2, 2, 3, 3, 3]

BLOCK_CONDITION = CONDITION.copy()

# A = within 5% of actual demand; I = outside 5%.
ACCURACY_FLAG = ['A', 'A', 'A', 'A', 'A', 'I', 'I', 'I', 'I', 'I', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'I', 'I']

# PAQ timing by block:
# PAQ1 after 1-5; PAQ2 after 6-7; PAQ3 after 8-10; PAQ4 after 11-15;
# PAQ5 after 16-18; PAQ6 after 19-20; PAQ7 after 21-25;
# PAQ8 after 26-28; PAQ9 after 29-30; PAQ10 after 31-35;
# PAQ11 after 36-37; PAQ12 after 38-40.
PAQ_PERIODS = [5, 7, 10, 15, 18, 20, 25, 28, 30, 35, 37, 40]

# PAQ pages where the "Your APE" column should be displayed.
SHOW_YOUR_APE_ON_PAQ = {1: False, 2: True, 3: True, 4: True, 5: False, 6: True, 7: True, 8: True, 9: False, 10: True, 11: True, 12: True}

PAQ_NOTES = {5: '.', 9: '.'}

LABEL_DICT = {
    f'fa{i}': f'Period {i} system forecast value: {SYSTEM_FORECAST[i - 1]} units. Will you keep it?'
    for i in range(1, 41)
}


class C(BaseConstants):
    NAME_IN_URL = 'ai'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    NUM_PERIODS = 40
    INITIAL_OBSERVATION_PERIODS = 5
    OBSERVATION_PERIODS = 30
    DECISION_PERIODS = list(range(31, 41))
    PAQ_PERIODS = PAQ_PERIODS

    actual_demand = ACTUAL_DEMAND
    system_forecast = SYSTEM_FORECAST
    system_ape = SYSTEM_APE
    display_your_ape = DISPLAY_YOUR_APE
    stage = STAGE
    condition = CONDITION
    block_id = BLOCK_ID
    block_length = BLOCK_LENGTH
    block_condition = BLOCK_CONDITION
    accuracy_flag = ACCURACY_FLAG
    show_your_ape_on_paq = SHOW_YOUR_APE_ON_PAQ
    paq_notes = PAQ_NOTES

    # Backward compatibility with old templates/functions.
    ai_data = SYSTEM_FORECAST
    demand_data_block = ACTUAL_DEMAND
    past_demand_data_block = ACTUAL_DEMAND[:INITIAL_OBSERVATION_PERIODS]
    label_dict = LABEL_DICT


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_adjustment_field():
    return models.IntegerField(
        label='<b>If No, please provide your forecast here</b>',
        null=True,
        blank=True,
        min=100,
        max=5000,
    )


def make_accept_field():
    return models.IntegerField(
        label='',
        choices=[(1, 'Yes'), (0, 'No')],
        widget=widgets.RadioSelect,
        null=True,
        blank=True,
    )


class Player(BasePlayer):
    # Actual demand and system forecast values stored by period.
    for i in range(1, 41):
        locals()[f'ad{i}'] = models.IntegerField(blank=True, null=True)
        locals()[f'sf{i}'] = models.IntegerField(blank=True, null=True)

        # fa = forecast acceptance indicator. accept = 1, reject = 0.
        locals()[f'fa{i}'] = make_accept_field()

        # fmag = participant final forecast magnitude.
        # If accept, fmag is automatically set to the system forecast.
        # If reject, participant must enter a numeric value from 100 to 5000.
        locals()[f'fmag{i}'] = make_adjustment_field()

        locals()[f'time_w{i}'] = models.FloatField(blank=True, null=True)
        locals()[f'system_error{i}'] = models.IntegerField(blank=True, null=True)
        locals()[f'participant_error{i}'] = models.IntegerField(blank=True, null=True)
        locals()[f'system_ape{i}'] = models.FloatField(blank=True, null=True)
        locals()[f'participant_ape{i}'] = models.FloatField(blank=True, null=True)

    # Perceived Accuracy Question and Confidence Level after observation and each streak block.
    for i in range(1, 13):
        locals()[f'PAQ{i}'] = models.IntegerField(
            label='Based on the forecast system’s performance so far, how likely do you think the statistical forecast system is to be accurate in the next periods?',
            min=0,
            max=100,
            blank=True,
            null=True,
        )
        locals()[f'CL{i}'] = models.IntegerField(
            label='How confident are you that the system forecast accuracy in the next periods will be?',
            min=0,
            max=100,
            blank=True,
            null=True,
        )
        locals()[f'time_paq{i}'] = models.FloatField(blank=True, null=True)
    del i

    # CAT question time tracking
    cat1_time = models.FloatField(blank=True, default=0.0)
    cat2_time = models.FloatField(blank=True, default=0.0)
    cat3_time = models.FloatField(blank=True, default=0.0)
    cat4_time = models.FloatField(blank=True, default=0.0)

    # NT question time tracking
    nt1_time = models.FloatField(blank=True, default=0.0)
    nt2_time = models.FloatField(blank=True, default=0.0)
    nt3_time = models.FloatField(blank=True, default=0.0)

    # demographic questions
    Q41 = models.StringField(
        widget=widgets.RadioSelect,
        label='What is the highest level of education you have completed or currently pursuing?',
        choices=(
            (1, 'Less than high school'),
            (2, 'High school graduate'),
            (3, 'Some college'),
            (4, '4 year degree'),
            (5, 'Professional degree (e.g. JD, MD, etc)'),
            (6, 'Masters'),
            (7, 'Doctorate'),
        ),
    )
    Q42 = models.IntegerField(label='What is your age?', min=18, max=120)
    Q43 = models.StringField(
        widget=widgets.RadioSelect,
        label='What is your current annual level of income?',
        choices=(
            (1, 'Less than $20,000'),
            (2, '$20,000 - $39,999'),
            (3, '$40,000 - $59,999'),
            (4, '$60,000 - $79,999'),
            (5, '$80,000 - $99,999'),
            (6, '$100,000 - $149,999'),
            (7, 'More than $150,000'),
        ),
    )
    Q44 = models.StringField(
        widget=widgets.RadioSelect,
        label='What is your gender?',
        choices=((1, 'Male'), (2, 'Female'), (3, 'Non-Binary'), (4, 'Other')),
    )
    Q44_1 = models.StringField(blank=True)
    Q45 = models.StringField(
        widget=widgets.RadioSelect,
        label='Choose one ethnicity you consider yourself to be.',
        choices=(
            (1, 'White'),
            (2, 'Black or African American'),
            (3, 'Hispanic'),
            (7, 'American Indian or Alaska Native'),
            (4, 'Asian'),
            (5, 'Native Hawaiian or Pacific Islander'),
            (6, 'Other'),
        ),
    )

    # forecasting questions
    Q46 = models.StringField(
        widget=widgets.RadioSelect,
        label='Have you engaged in forecasting at your company or workplace?',
        choices=((1, 'Yes, I often do'), (2, 'Yes, I sometimes do'), (3, 'No, never at all')),
    )
    Q47 = models.StringField(
        widget=widgets.RadioSelect,
        label='How comfortable are you with forecasting?',
        choices=(
            (1, 'Extremely uncomfortable'),
            (2, 'Somewhat uncomfortable'),
            (3, 'Neither comfortable nor uncomfortable'),
            (4, 'Somewhat comfortable'),
            (5, 'Extremely comfortable'),
        ),
    )
    Q48 = models.StringField(
        widget=widgets.RadioSelect,
        label='Have you used or are you using a statistical, analytical, or AI-based tool for modeling or prediction?',
        choices=(
            (1, 'Definitely not'),
            (2, 'Probably not'),
            (3, 'Might or might not'),
            (4, 'Probably yes'),
            (5, 'Definitely yes'),
        ),
    )

    ACQ1 = models.StringField(
        widget=widgets.RadioSelect,
        label='Please choose Definitely yes for this question. Do you answer questions to the best of your abilities?',
        choices=(
            (1, 'Definitely not'),
            (2, 'Probably not'),
            (3, 'Might or might not'),
            (4, 'Probably yes'),
            (5, 'Definitely yes'),
        ),
    )

    # likelihood questions - financial risk preference
    Q13f1 = models.IntegerField(label='Betting 10% of your annual income at the horse races.', choices=((1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')), widget=widgets.RadioSelectHorizontal)
    Q13f2 = models.IntegerField(label='Investing 10% of your annual income in a moderate growth mutual fund.', choices=((1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')), widget=widgets.RadioSelectHorizontal)
    Q13f3 = models.IntegerField(label='Betting 10% of your annual income at a high-stake poker game.', choices=((1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')), widget=widgets.RadioSelectHorizontal)
    Q13f4 = models.IntegerField(label='Investing 10% of your annual income in a very speculative stock.', choices=((1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')), widget=widgets.RadioSelectHorizontal)
    Q13f5 = models.IntegerField(label='Betting 10% of your annual income on the outcome of a sporting event.', choices=((1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')), widget=widgets.RadioSelectHorizontal)
    Q13f6 = models.IntegerField(label='Investing 10% of your annual income in a new business venture.', choices=((1, 'Very unlikely'), (2, 'Unlikely'), (3, 'Not sure'), (4, 'Likely'), (5, 'Very likely')), widget=widgets.RadioSelectHorizontal)


    Q14 = models.IntegerField(label='How many forecasting courses have you taken in college?', choices=((0, 'None'), (1, '1'), (2, '2 or more')), widget=widgets.RadioSelect)
    Q15 = models.IntegerField(label='How will you rate your analytical ability?', min=0, max=10, blank=True, null=True)

    table_data = models.LongStringField(blank=True)
    consent = models.BooleanField(
        label='',
        choices=(
            (True, 'I am at least 18 years old, have read the consent information, and agree to take part in the research.'),
            (False, 'No, I disagree'),
        ),
    )

    # CAT
    cat1 = models.IntegerField(label='1. If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how many days would it take them to drink one barrel of water together?')
    cat2 = models.IntegerField(label='2. Jerry received both the 15th highest and the 15th lowest mark in the class. How many students are in the class?')
    cat3 = models.IntegerField(label='3. A man buys a pig for $60, sells it for $70, buys it back for $80, and sells it finally for $90. How much has he made?')
    cat4 = models.StringField(
        widget=widgets.RadioSelect,
        label='4. Simon decided to invest $8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks went down by 50%. Three months later, on October 17, the stocks went up 75%. At this point, what has happened to the $8,000 Simon invested?',
        choices=((1, 'broken even in the stock market'), (2, 'is ahead of where he began'), (3, 'has lost money')),
    )

    # NT
    nt1 = models.FloatField(min=0, max=1, label='1. Out of 1,000 people in a small town 500 are members of a choir. Out of these 500 members in the choir 100 are men. Out of the 500 inhabitants that are not in the choir 300 are men. What is the probability that a randomly drawn man is a member of the choir?')
    nt2 = models.FloatField(min=0, max=1000, label='2. Imagine we are throwing a five-sided die 50 times. On average, out of these 50 throws how many times would this five-sided die show an odd number (1, 3 or 5)?')
    nt3 = models.FloatField(min=0, max=1, label='3. In a forest 20% of mushrooms are red, 50% brown and 30% white. A red mushroom is poisonous with a probability of 20%. A mushroom that is not red is poisonous with a probability of 5%. What is the probability that a poisonous mushroom in the forest is red?')

    name = models.StringField(label='')
    country = models.StringField(label='')
    capital = models.StringField(label='')
    state = models.StringField(label='', blank=True)
    length_of_stay = models.IntegerField(label='', min=0, max=120)
    unique_code = models.StringField(blank=True)

    def generate_unique_code(self):
        self.unique_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))



def creating_session(subsession):
    for p in subsession.get_players():
        for i in range(1, 41):
            actual = C.actual_demand[i - 1]
            system = C.system_forecast[i - 1]
            setattr(p, f'ad{i}', actual)
            setattr(p, f'sf{i}', system)
            setattr(p, f'system_error{i}', abs(actual - system))
            setattr(p, f'system_ape{i}', C.system_ape[i - 1])
        p.participant.vars['prev'] = C.INITIAL_OBSERVATION_PERIODS
        p.table_data = str(get_table_rows(p, C.INITIAL_OBSERVATION_PERIODS))


# -------------------------
# Helper functions
# -------------------------

def period_info(period):
    idx = period - 1
    actual = C.actual_demand[idx]
    system = C.system_forecast[idx]
    return dict(
        period=period,
        actual=actual,
        system=system,
        stage=C.stage[idx],
        condition=C.condition[idx],
        block_id=C.block_id[idx],
        block_length=C.block_length[idx],
        block_condition=C.block_condition[idx],
        accuracy_flag=C.accuracy_flag[idx],
        system_error=abs(actual - system),
        system_ape=C.system_ape[idx],
    )


def final_forecast_for_period(player, period):
    if period < 31:
        return None

    fa = player.field_maybe_none(f'fa{period}')
    fmag = player.field_maybe_none(f'fmag{period}')
    if fa == 1:
        return C.system_forecast[period - 1]
    if fa == 0:
        return fmag
    return None


def completed_periods(player):
    return int(player.participant.vars.get('prev', C.INITIAL_OBSERVATION_PERIODS))


def cmape(values):
    if not values:
        return []
    out = []
    total = 0
    for i, value in enumerate(values):
        total += value
        out.append(round(total / (i + 1), 2))
    return out


def get_table_rows(player, upto_period=None):
    if upto_period is None:
        upto_period = completed_periods(player)

    rows = []
    system_apes = []
    participant_apes = []

    for period in range(1, upto_period + 1):
        actual = C.actual_demand[period - 1]
        system = C.system_forecast[period - 1]
        system_error = abs(actual - system)
        system_ape = C.system_ape[period - 1]
        system_apes.append(system_ape)

        if period < 31:
            your_forecast = ''
            your_error = ''
            your_cmape = ''
        else:
            your_forecast = final_forecast_for_period(player, period)
            if your_forecast is None:
                your_error = ''
                your_cmape = ''
            else:
                your_error = abs(actual - your_forecast)
                participant_ape = round(your_error / actual * 100, 2)
                participant_apes.append(participant_ape)
                your_cmape = cmape(participant_apes)[-1]

        rows.append([
            f'Period {period}',
            actual,
            system,
            system_error,
            cmape(system_apes)[-1],
            your_forecast,
            your_error,
            your_cmape,
        ])

    return rows


def chart_data(player, upto_period=None):
    if upto_period is None:
        upto_period = completed_periods(player)

    labels = [f'Period {i}' for i in range(1, upto_period + 1)]
    actual = C.actual_demand[:upto_period]
    system = C.system_forecast[:upto_period]
    your = []

    for period in range(1, upto_period + 1):
        if period < 31:
            your.append(None)
        else:
            your.append(final_forecast_for_period(player, period))

    return labels, actual, system, your


def save_period_outcomes(player, period):
    fa = player.field_maybe_none(f'fa{period}')
    if fa == 1:
        setattr(player, f'fmag{period}', C.system_forecast[period - 1])

    final_value = final_forecast_for_period(player, period)
    if final_value is not None:
        actual = C.actual_demand[period - 1]
        err = abs(actual - final_value)
        setattr(player, f'participant_error{period}', err)
        setattr(player, f'participant_ape{period}', round(err / actual * 100, 2))

    player.participant.vars['prev'] = period
    player.table_data = str(get_table_rows(player, period))


def make_observation_table():
    rows = []
    for period in range(1, C.INITIAL_OBSERVATION_PERIODS + 1):
        info = period_info(period)
        rows.append([
            period,
            info['actual'],
            info['system'],
            info['system_error'],
            info['system_ape'],
            'Accurate' if info['accuracy_flag'] == 'A' else 'Inaccurate',
        ])
    return rows


def paq_prior_rows(player, paq_number):
    after_period = C.PAQ_PERIODS[paq_number - 1]

    if paq_number == 1:
        start_period = 1
    else:
        start_period = C.PAQ_PERIODS[paq_number - 2] + 1

    rows = []

    for period in range(start_period, after_period + 1):
        info = period_info(period)

        participant_ape = ''
        if C.show_your_ape_on_paq.get(paq_number, False):
            if period < 31:
                participant_ape = C.display_your_ape.get(period, '')
                if participant_ape is None:
                    participant_ape = ''
            else:
                participant_ape = player.field_maybe_none(f'participant_ape{period}')
                if participant_ape is None:
                    participant_ape = ''

        rows.append([
            period,
            info['actual'],
            info['system'],
            info['system_error'],
            info['system_ape'],
            participant_ape,
        ])

    return rows


# -------------------------
# Page classes
# -------------------------

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        player.participant.vars['prev'] = C.INITIAL_OBSERVATION_PERIODS
        player.table_data = str(get_table_rows(player, C.INITIAL_OBSERVATION_PERIODS))


class ConsentOk(Page):
    @staticmethod
    def is_displayed(player):
        return player.consent


class Name(ConsentOk):
    form_model = 'player'
    form_fields = ['name', 'country', 'capital', 'state', 'length_of_stay']


def name_error_message(player, value):
    if value and len(value) > 60:
        return 'Error, your name cannot contain more than 60 characters!'


class Survey(ConsentOk):
    template_name = 'ai/Survey.html'
    form_model = 'player'
    form_fields = ['Q41', 'Q42', 'Q43', 'Q44', 'Q44_1', 'Q45']


class Instruction(ConsentOk):
    template_name = 'ai/Instruction.html'

    @staticmethod
    def vars_for_template(player):
        return dict(observation_table=make_observation_table())

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        player.participant.vars['prev'] = C.INITIAL_OBSERVATION_PERIODS
        player.table_data = str(get_table_rows(player, C.INITIAL_OBSERVATION_PERIODS))


# -------------------------
# Dynamically generated PAQ and forecast pages
# -------------------------

def make_paq_page(n):
    class PAQPage(ConsentOk):
        template_name = 'ai/PAQ.html'
        form_model = 'player'
        form_fields = [f'PAQ{n}', f'CL{n}', f'time_paq{n}']

        @staticmethod
        def vars_for_template(player):
            after_period = C.PAQ_PERIODS[n - 1]
            block_len = C.block_length[after_period - 1]
            block_cond = C.block_condition[after_period - 1]
            show_your_ape = C.show_your_ape_on_paq.get(n, False)

            return dict(
                paq_number=n,
                after_period=after_period,
                block_length=block_len,
                block_condition=block_cond.replace('_', ' ').title(),
                recent_rows=paq_prior_rows(player, n),
                show_participant_ape=show_your_ape,
                paq_note=C.paq_notes.get(n, ''),
            )

        @staticmethod
        def before_next_page(player, timeout_happened=False):
            after_period = C.PAQ_PERIODS[n - 1]
            player.participant.vars['prev'] = after_period
            player.table_data = str(get_table_rows(player, after_period))

    PAQPage.__name__ = f'PAQ{n}'
    return PAQPage


def make_forecast_page(period):
    class ForecastPage(ConsentOk):
        template_name = 'ai/Forecast.html'
        form_model = 'player'
        form_fields = [f'fa{period}', f'fmag{period}', f'time_w{period}']

        @staticmethod
        def error_message(player, values):
            fa = values.get(f'fa{period}')
            fmag = values.get(f'fmag{period}')
            if fa is None:
                return 'Please indicate whether you want to keep the system forecast.'
            if fa == 0 and fmag is None:
                return 'You selected No. Please provide your own forecast value.'

        @staticmethod
        def vars_for_template(player):
            info = period_info(period)
            prev = period - 1
            prev_feedback = None

            if period > 31:
                previous_period = period - 1
                actual_prev = C.actual_demand[previous_period - 1]
                system_prev = C.system_forecast[previous_period - 1]
                your_prev = final_forecast_for_period(player, previous_period)

                if your_prev is not None:
                    previous_rows = get_table_rows(player, previous_period)
                    prev_feedback = [
                        previous_period,
                        abs(actual_prev - system_prev),
                        abs(actual_prev - your_prev),
                        previous_rows[-1][7],
                    ]

            return dict(
                qn=period,
                qn_n=period,
                period=period,
                week_data=info['system'],
                label=C.label_dict[f'fa{period}'],
                start=prev_feedback is not None,
                prev_error=prev_feedback,
                table_data=list(reversed(get_table_rows(player, prev))),
            )

        @staticmethod
        def js_vars(player):
            labels, actual, system, your = chart_data(player, period - 1)
            return dict(
                label_block=labels,
                actual_demand_block=actual,
                ai_data_block=system,
                your_data_block=your,
            )

        @staticmethod
        def before_next_page(player, timeout_happened=False):
            save_period_outcomes(player, period)

    ForecastPage.__name__ = f'ForecastP{period}'
    return ForecastPage


PAQ1 = make_paq_page(1)
PAQ2 = make_paq_page(2)
PAQ3 = make_paq_page(3)
PAQ4 = make_paq_page(4)
PAQ5 = make_paq_page(5)
PAQ6 = make_paq_page(6)
PAQ7 = make_paq_page(7)
PAQ8 = make_paq_page(8)
PAQ9 = make_paq_page(9)
PAQ10 = make_paq_page(10)
PAQ11 = make_paq_page(11)
PAQ12 = make_paq_page(12)

FORECAST_PAGES = {period: make_forecast_page(period) for period in range(31, 41)}

# -------------------------
# Remaining original app pages
# -------------------------

class Graph(ConsentOk):
    template_name = 'ai/Graph.html'

    @staticmethod
    def vars_for_template(player):
        return dict(table_data=get_table_rows(player, C.NUM_PERIODS))

    @staticmethod
    def js_vars(player):
        labels, actual, system, your = chart_data(player, C.NUM_PERIODS)
        return dict(
            label_block=labels,
            actual_demand_block=actual,
            ai_data_block=system,
            your_data_block=your,
        )


class Survey2(ConsentOk):
    template_name = 'ai/Survey2.html'
    form_model = 'player'
    form_fields = ['Q46', 'Q47', 'Q48', 'ACQ1', 'Q14']


class Likely(ConsentOk):
    template_name = 'ai/Likely.html'
    form_model = 'player'
    form_fields = ['Q13f1', 'Q13f2', 'Q13f3', 'Q13f4', 'Q13f5', 'Q13f6', 'Q15']



class CAT(ConsentOk):
    template_name = 'ai/CAT.html'
    form_model = 'player'
    form_fields = ['cat1', 'cat2', 'cat3', 'cat4', 'cat1_time', 'cat2_time', 'cat3_time', 'cat4_time']


class NT(ConsentOk):
    template_name = 'ai/NT.html'
    form_model = 'player'
    form_fields = ['nt1', 'nt2', 'nt3', 'nt1_time', 'nt2_time', 'nt3_time']


class Thanks(ConsentOk):
    template_name = 'ai/Thanks.html'

    @staticmethod
    def before_next_page(player, timeout_happened=False):
        if player.field_maybe_none('unique_code') is None:
            player.generate_unique_code()

    @staticmethod
    def vars_for_template(player):
        if player.field_maybe_none('unique_code') is None:
            player.generate_unique_code()
        return dict(unique_code=player.field_maybe_none('unique_code'))



# -------------------------
# Page sequence
# -------------------------

page_sequence = [Consent, Name, Survey, Instruction, PAQ1, PAQ2, PAQ3, PAQ4, PAQ5, PAQ6, PAQ7, PAQ8, PAQ9]
page_sequence += [FORECAST_PAGES[31], FORECAST_PAGES[32], FORECAST_PAGES[33], FORECAST_PAGES[34], FORECAST_PAGES[35], PAQ10]
page_sequence += [FORECAST_PAGES[36], FORECAST_PAGES[37], PAQ11]
page_sequence += [FORECAST_PAGES[38], FORECAST_PAGES[39], FORECAST_PAGES[40], PAQ12]
page_sequence += [Graph, Survey2, Likely, CAT, NT, Thanks]
