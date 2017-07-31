

import re

import ply.lex as lex
from ply.lex import TOKEN

from MTG import color, card_type

def token_from_enum(enum_class, token_name):
    def tok_fun(t):
        t.value = enum_class[t.value.upper()]
        return t
    tok_fun.__doc__ = r'|'.join(item.name for item in list(enum_class))
    tok_fun.__name__ = 't_{}'.format(token_name)
    return tok_fun

keyword_abilities = {
    r'flying' : 'FLYING',
    r'soulshift' : 'SOULSHIFT',
    r'first strike' : 'FIRST_STRIKE',
    r'trample' : 'TRAMPLE',
    r'haste' : 'HASTE',
    r'unearth' : 'UNEARTH'
}

keyword_actions = {
    r'regenerate' : 'REGENERATE',
    r'sacrifice' : 'SACRIFICE'
}

tokens = (
    'MANA_SYMBOL',
    'COLON',
    'COLOR',
    'REMINDER',
    'TAP_SYMBOL',
    'TARGET',
    'TYPE',
    'BECOME',
    'ARTICLE',
    'OR',
    'LAND_TYPE',
    'UNTIL',
    'EOT',
    'ABILITY_END',
    'EFFECT_END',
    'NUMBER',
    'GET',
    'PT_CHANGE',
    'SELF',
    'CHOOSE',
    'PLAYER',
    'YOU',
    'COMMA',
    'WHEN',
    'IT',
    'DRAW',
    'OBJECT',
    'WAY',
    'MAY',
    'ENTER_BATTLEFIELD',
    'GAIN',
    'LIFE',
    'IN',
    'POSSESSIVE',
    'FOR_EACH',
    'ZONE',
    'TURN_PART',
    'BEGINNING',
    'OF',
    'AT'
) + tuple(keyword_abilities.values()) + tuple(keyword_actions.values())

t_AT = r'\bat\b'
t_OF = r'\bof\b'
t_BEGINNING = r'\bbeginning\b'
t_TURN_PART = r'\b(beginning|main|combat|ending)\sphase|(untap|upkeep|draw|beginning\sof\scombat|declare\s(attackers|blockers)|combat\sdamage|end(\sof\scombat)?|cleanup)\sstep\b'
t_ZONE = r'\b(battlefield|library|libraries|hand|graveyard|command\szone|stack)s?\b'
t_FOR_EACH = r'\bfor\seach\b'
t_POSSESSIVE = r'\b(your|their|his\sor\sher)s?\b'
t_IN = r'\bin\b'
t_LIFE = r'\blife\b'
t_GAIN = r'\bgains?\b'
t_ENTER_BATTLEFIELD = r'\benters?\sthe\sbattlefield'
t_DRAW = r'\bdraws?\b'
t_MAY = r'\bmay\b'
t_WAY = r'\bway\b'
t_OBJECT = r'\b(permanent|spell|card)s?\b'
t_IT = r'\bit\b'
t_WHEN = r'\b(when(ever)?)\b'
t_COMMA = r','
t_YOU = r'\byou\b'
t_PLAYER = r'\b(player|opponent)s?\b'
t_CHOOSE = r'\bchooses?\b'
t_SELF = r'<self>'
t_GET = r'\bgets?\b'
t_NUMBER = r'\d+'
t_COLON = r':'
t_TAP_SYMBOL = r'\{T\}'
t_TARGET = r'target'
t_BECOME = r'becomes?'
t_ARTICLE = r'\b(a|an|any|the|this|that|these|those|another)\b'
t_OR = r'\bor\b'
t_UNTIL = r'\buntil\b'
t_EOT = r'end\sof\sturn'
t_ABILITY_END = r'[\n]'
t_EFFECT_END = r'[.]'
t_ignore_REMINDER = r'\(.*?\)'
t_ignore = ' \t'

t_COLOR = token_from_enum(color.Color, 'COLOR')
t_TYPE = token_from_enum(card_type.CardType, 'TYPE')
t_LAND_TYPE = token_from_enum(card_type.LandType, 'LAND_TYPE')

@TOKEN(re.sub(r'\s+', r'\s+', r'|'.join(keyword_abilities.keys())))
def t_KEYWORD_ABILITIES(t):
    t.type = keyword_abilities[re.sub('\s+', ' ', t.value.lower())]
    return t

@TOKEN(r'\b({})s?\b'.format(r'|'.join(keyword_actions.keys())))
def t_KEYWORD_ACTIONS(t):
    t.type = keyword_actions[t.value.lower().rstrip('s')]
    return t;

def t_MANA_SYMBOL(t):
    r'\{(\d+|[WUBRG]P?|[WUBRG]/[WUBRG]|2/[WUBRG]|S|[XYZ])\}'
    return t

def t_PT_CHANGE(t):
    r'[+-](\d+|X)/[+-](\d+|X)'
    return t

def t_error(t):
    raise ValueError("Unrecognized token '{}'".format(t.value))

lexer = lex.lex(reflags=re.IGNORECASE)