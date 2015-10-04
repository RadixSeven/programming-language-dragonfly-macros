# Author:Brandon Lovrien & Eric Moyer
# This script includes some commands for various useful symbols used in programming

from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)

# Useful commands for encapsulation of quotes, etc.
class UsefulStuff(MappingRule):
    
    mapping  = {
        "in quotes":                Text("\"\"") + Key("left"),
        "in single quotes":         Text("\'\'") + Key("left"),
        "in parentheses":           Text("()") + Key("left"),
        "in brackets":              Text("[]") + Key("left"),
        "in braces":                Text("{}") + Key("left"),
        "in angle brackets":        Text("<>") + Key("left"),
        "parameters":               Text("()"),
        "arrow":                    Text("->"),
        "double arrow":             Text("=>"),
        "boom":                     Text(", "),
        "dot":                      Text("."),
        "ace":                      Text(" "),
        "bang":                     Text("!"),
        "wokka":                    Text("<"),
        "shock":                    Key("enter"),
        "starling":                 Text("*"),
        "grendel":                  Key("end"),
        "carrot":                   Text("^"),
        "hashtag":                  Text("#"),
        
    }

globalStuff = Grammar("useful custom global commands")                # Create a grammar to contain the command rule.
globalStuff.add_rule(UsefulStuff())
globalStuff.load()    
