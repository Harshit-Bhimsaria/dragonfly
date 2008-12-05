﻿#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU Lesser General Public License as published 
#   by the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public 
#   License along with Dragonfly.  If not, see 
#   <http://www.gnu.org/licenses/>.
#

#---------------------------------------------------------------------------
from dragonfly.log      import get_log
from dragonfly.config   import Config, Section, Item

#---------------------------------------------------------------------------
from dragonfly.grammar.grammar_base       import Grammar
from dragonfly.grammar.grammar_connection import ConnectionGrammar
from dragonfly.grammar.rule               import Rule
from dragonfly.grammar.compoundrule       import CompoundRule
from dragonfly.grammar.mappingrule        import MappingRule
from dragonfly.grammar.elements           import ElementBase, Sequence, Alternative, \
                                                 Optional, Repetition, Literal, RuleRef, \
                                                 ListRef, DictListRef, Dictation, Empty, \
                                                 Compound, Choice
from dragonfly.grammar.context      import Context, AppContext
from dragonfly.grammar.list         import ListBase, List, DictList
from dragonfly.grammar.wordinfo     import Word, FormatState

#---------------------------------------------------------------------------
from dragonfly.actions.actions      import (ActionBase, Key, Text, Paste,
                                            Pause)
from dragonfly.actions.keyboard     import Typeable, Keyboard
from dragonfly.actions.typeables    import typeables

#---------------------------------------------------------------------------
from dragonfly.windows.window       import Window
from dragonfly.windows.monitor      import Monitor
from dragonfly.windows.clipboard    import Clipboard

#---------------------------------------------------------------------------
def get_number_module(language="en"):
#    if language and integer_languages:
#        mod = __import__(integer_languages[language])
    import dragonfly.grammar.number_en as mod
    return mod

Integer = get_number_module().Integer
Digits  = get_number_module().Digits
