"""All indexed colors available on a 256 colors terminal. The first 16 colors
are XTERM system colors (and text mode as well).

Source: [256 COLORS - CHEAT SHEET](https://jonasjacek.github.io/colors/)

<style>
.docstring p span {
    border-color: #000;
    border-radius: 1em;
    border-style: dotted;
    border-width: 1px;
    display:block;
    float:right;
    width: 25%;
}
</style>"""

BLACK = 0
"""BLACK = rgb(0,0,0) <span style='background:#000000'>&nbsp;</span>"""
MAROON = 1
"""MAROON = rgb(128,0,0) <span style='background:#800000'>&nbsp;</span>"""
GREEN = 2
"""GREEN = rgb(0,128,0) <span style='background:#008000'>&nbsp;</span>"""
OLIVE = 3
"""OLIVE = rgb(128,128,0) <span style='background:#808000'>&nbsp;</span>"""
NAVY = 4
"""NAVY = rgb(0,0,128) <span style='background:#000080'>&nbsp;</span>"""
PURPLE = 5
"""PURPLE = rgb(128,0,128) <span style='background:#800080'>&nbsp;</span>"""
TEAL = 6
"""TEAL = rgb(0,128,128) <span style='background:#008080'>&nbsp;</span>"""
SILVER = 7
"""SILVER = rgb(192,192,192) <span style='background:#c0c0c0'>&nbsp;</span>"""
GREY = 8
"""GREY = rgb(128,128,128) <span style='background:#808080'>&nbsp;</span>"""
RED = 9
"""RED = rgb(255,0,0) <span style='background:#ff0000'>&nbsp;</span>"""
LIME = 10
"""LIME = rgb(0,255,0) <span style='background:#00ff00'>&nbsp;</span>"""
YELLOW = 11
"""YELLOW = rgb(255,255,0) <span style='background:#ffff00'>&nbsp;</span>"""
BLUE = 12
"""BLUE = rgb(0,0,255) <span style='background:#0000ff'>&nbsp;</span>"""
FUCHSIA = 13
"""FUCHSIA = rgb(255,0,255) <span style='background:#ff00ff'>&nbsp;</span>"""
AQUA = 14
"""AQUA = rgb(0,255,255) <span style='background:#00ffff'>&nbsp;</span>"""
WHITE = 15
"""WHITE = rgb(255,255,255) <span style='background:#ffffff'>&nbsp;</span>"""
GREY0 = 16
"""GREY0 = rgb(0,0,0) <span style='background:#000000'>&nbsp;</span>"""
NAVYBLUE = 17
"""NAVYBLUE = rgb(0,0,95) <span style='background:#00005f'>&nbsp;</span>"""
DARKBLUE = 18
"""DARKBLUE = rgb(0,0,135) <span style='background:#000087'>&nbsp;</span>"""
BLUE3 = 19
"""BLUE3 = rgb(0,0,175) <span style='background:#0000af'>&nbsp;</span>"""
BLUE3 = 20
"""BLUE3 = rgb(0,0,215) <span style='background:#0000d7'>&nbsp;</span>"""
BLUE1 = 21
"""BLUE1 = rgb(0,0,255) <span style='background:#0000ff'>&nbsp;</span>"""
DARKGREEN = 22
"""DARKGREEN = rgb(0,95,0) <span style='background:#005f00'>&nbsp;</span>"""
DEEPSKYBLUE4 = 23
"""DEEPSKYBLUE4 = rgb(0,95,95) <span style='background:#005f5f'>&nbsp;</span>"""
DEEPSKYBLUE4 = 24
"""DEEPSKYBLUE4 = rgb(0,95,135) <span style='background:#005f87'>&nbsp;</span>"""
DEEPSKYBLUE4 = 25
"""DEEPSKYBLUE4 = rgb(0,95,175) <span style='background:#005faf'>&nbsp;</span>"""
DODGERBLUE3 = 26
"""DODGERBLUE3 = rgb(0,95,215) <span style='background:#005fd7'>&nbsp;</span>"""
DODGERBLUE2 = 27
"""DODGERBLUE2 = rgb(0,95,255) <span style='background:#005fff'>&nbsp;</span>"""
GREEN4 = 28
"""GREEN4 = rgb(0,135,0) <span style='background:#008700'>&nbsp;</span>"""
SPRINGGREEN4 = 29
"""SPRINGGREEN4 = rgb(0,135,95) <span style='background:#00875f'>&nbsp;</span>"""
TURQUOISE4 = 30
"""TURQUOISE4 = rgb(0,135,135) <span style='background:#008787'>&nbsp;</span>"""
DEEPSKYBLUE3 = 31
"""DEEPSKYBLUE3 = rgb(0,135,175) <span style='background:#0087af'>&nbsp;</span>"""
DEEPSKYBLUE3 = 32
"""DEEPSKYBLUE3 = rgb(0,135,215) <span style='background:#0087d7'>&nbsp;</span>"""
DODGERBLUE1 = 33
"""DODGERBLUE1 = rgb(0,135,255) <span style='background:#0087ff'>&nbsp;</span>"""
GREEN3 = 34
"""GREEN3 = rgb(0,175,0) <span style='background:#00af00'>&nbsp;</span>"""
SPRINGGREEN3 = 35
"""SPRINGGREEN3 = rgb(0,175,95) <span style='background:#00af5f'>&nbsp;</span>"""
DARKCYAN = 36
"""DARKCYAN = rgb(0,175,135) <span style='background:#00af87'>&nbsp;</span>"""
LIGHTSEAGREEN = 37
"""LIGHTSEAGREEN = rgb(0,175,175) <span style='background:#00afaf'>&nbsp;</span>"""
"""DEEPSKYBLUE2 = rgb(0,175,215) <span style='background:#00afd7'>&nbsp;</span>"""
DEEPSKYBLUE2 = 38
DEEPSKYBLUE1 = 39
"""DEEPSKYBLUE1 = rgb(0,175,255) <span style='background:#00afff'>&nbsp;</span>"""
GREEN3 = 40
"""GREEN3 = rgb(0,215,0) <span style='background:#00d700'>&nbsp;</span>"""
SPRINGGREEN3 = 41
"""SPRINGGREEN3 = rgb(0,215,95) <span style='background:#00d75f'>&nbsp;</span>"""
SPRINGGREEN2 = 42
"""SPRINGGREEN2 = rgb(0,215,135) <span style='background:#00d787'>&nbsp;</span>"""
CYAN3 = 43
"""CYAN3 = rgb(0,215,175) <span style='background:#00d7af'>&nbsp;</span>"""
DARKTURQUOISE = 44
"""DARKTURQUOISE = rgb(0,215,215) <span style='background:#00d7d7'>&nbsp;</span>"""
TURQUOISE2 = 45
"""TURQUOISE2 = rgb(0,215,255) <span style='background:#00d7ff'>&nbsp;</span>"""
GREEN1 = 46
"""GREEN1 = rgb(0,255,0) <span style='background:#00ff00'>&nbsp;</span>"""
SPRINGGREEN2 = 47
"""SPRINGGREEN2 = rgb(0,255,95) <span style='background:#00ff5f'>&nbsp;</span>"""
SPRINGGREEN1 = 48
"""SPRINGGREEN1 = rgb(0,255,135) <span style='background:#00ff87'>&nbsp;</span>"""
MEDIUMSPRINGGREEN = 49
"""MEDIUMSPRINGGREEN = rgb(0,255,175) <span style='background:#00ffaf'>&nbsp;</span>"""
CYAN2 = 50
"""CYAN2 = rgb(0,255,215) <span style='background:#00ffd7'>&nbsp;</span>"""
CYAN1 = 51
"""CYAN1 = rgb(0,255,255) <span style='background:#00ffff'>&nbsp;</span>"""
DARKRED = 52
"""DARKRED = rgb(95,0,0) <span style='background:#5f0000'>&nbsp;</span>"""
DEEPPINK4 = 53
"""DEEPPINK4 = rgb(95,0,95) <span style='background:#5f005f'>&nbsp;</span>"""
PURPLE4 = 54
"""PURPLE4 = rgb(95,0,135) <span style='background:#5f0087'>&nbsp;</span>"""
PURPLE4 = 55
"""PURPLE4 = rgb(95,0,175) <span style='background:#5f00af'>&nbsp;</span>"""
PURPLE3 = 56
"""PURPLE3 = rgb(95,0,215) <span style='background:#5f00d7'>&nbsp;</span>"""
BLUEVIOLET = 57
"""BLUEVIOLET = rgb(95,0,255) <span style='background:#5f00ff'>&nbsp;</span>"""
ORANGE4 = 58
"""ORANGE4 = rgb(95,95,0) <span style='background:#5f5f00'>&nbsp;</span>"""
GREY37 = 59
"""GREY37 = rgb(95,95,95) <span style='background:#5f5f5f'>&nbsp;</span>"""
MEDIUMPURPLE4 = 60
"""MEDIUMPURPLE4 = rgb(95,95,135) <span style='background:#5f5f87'>&nbsp;</span>"""
SLATEBLUE3 = 61
"""SLATEBLUE3 = rgb(95,95,175) <span style='background:#5f5faf'>&nbsp;</span>"""
SLATEBLUE3 = 62
"""SLATEBLUE3 = rgb(95,95,215) <span style='background:#5f5fd7'>&nbsp;</span>"""
ROYALBLUE1 = 63
"""ROYALBLUE1 = rgb(95,95,255) <span style='background:#5f5fff'>&nbsp;</span>"""
CHARTREUSE4 = 64
"""CHARTREUSE4 = rgb(95,135,0) <span style='background:#5f8700'>&nbsp;</span>"""
DARKSEAGREEN4 = 65
"""DARKSEAGREEN4 = rgb(95,135,95) <span style='background:#5f875f'>&nbsp;</span>"""
PALETURQUOISE4 = 66
"""PALETURQUOISE4 = rgb(95,135,135) <span style='background:#5f8787'>&nbsp;</span>"""
STEELBLUE = 67
"""STEELBLUE = rgb(95,135,175) <span style='background:#5f87af'>&nbsp;</span>"""
STEELBLUE3 = 68
"""STEELBLUE3 = rgb(95,135,215) <span style='background:#5f87d7'>&nbsp;</span>"""
CORNFLOWERBLUE = 69
"""CORNFLOWERBLUE = rgb(95,135,255) <span style='background:#5f87ff'>&nbsp;</span>"""
CHARTREUSE3 = 70
"""CHARTREUSE3 = rgb(95,175,0) <span style='background:#5faf00'>&nbsp;</span>"""
DARKSEAGREEN4 = 71
"""DARKSEAGREEN4 = rgb(95,175,95) <span style='background:#5faf5f'>&nbsp;</span>"""
CADETBLUE = 72
"""CADETBLUE = rgb(95,175,135) <span style='background:#5faf87'>&nbsp;</span>"""
CADETBLUE = 73
"""CADETBLUE = rgb(95,175,175) <span style='background:#5fafaf'>&nbsp;</span>"""
SKYBLUE3 = 74
"""SKYBLUE3 = rgb(95,175,215) <span style='background:#5fafd7'>&nbsp;</span>"""
STEELBLUE1 = 75
"""STEELBLUE1 = rgb(95,175,255) <span style='background:#5fafff'>&nbsp;</span>"""
CHARTREUSE3 = 76
"""CHARTREUSE3 = rgb(95,215,0) <span style='background:#5fd700'>&nbsp;</span>"""
PALEGREEN3 = 77
"""PALEGREEN3 = rgb(95,215,95) <span style='background:#5fd75f'>&nbsp;</span>"""
SEAGREEN3 = 78
"""SEAGREEN3 = rgb(95,215,135) <span style='background:#5fd787'>&nbsp;</span>"""
AQUAMARINE3 = 79
"""AQUAMARINE3 = rgb(95,215,175) <span style='background:#5fd7af'>&nbsp;</span>"""
MEDIUMTURQUOISE = 80
"""MEDIUMTURQUOISE = rgb(95,215,215) <span style='background:#5fd7d7'>&nbsp;</span>"""
STEELBLUE1 = 81
"""STEELBLUE1 = rgb(95,215,255) <span style='background:#5fd7ff'>&nbsp;</span>"""
CHARTREUSE2 = 82
"""CHARTREUSE2 = rgb(95,255,0) <span style='background:#5fff00'>&nbsp;</span>"""
SEAGREEN2 = 83
"""SEAGREEN2 = rgb(95,255,95) <span style='background:#5fff5f'>&nbsp;</span>"""
SEAGREEN1 = 84
"""SEAGREEN1 = rgb(95,255,135) <span style='background:#5fff87'>&nbsp;</span>"""
SEAGREEN1 = 85
"""SEAGREEN1 = rgb(95,255,175) <span style='background:#5fffaf'>&nbsp;</span>"""
AQUAMARINE1 = 86
"""AQUAMARINE1 = rgb(95,255,215) <span style='background:#5fffd7'>&nbsp;</span>"""
DARKSLATEGRAY2 = 87
"""DARKSLATEGRAY2 = rgb(95,255,255) <span style='background:#5fffff'>&nbsp;</span>"""
DARKRED = 88
"""DARKRED = rgb(135,0,0) <span style='background:#870000'>&nbsp;</span>"""
DEEPPINK4 = 89
"""DEEPPINK4 = rgb(135,0,95) <span style='background:#87005f'>&nbsp;</span>"""
DARKMAGENTA = 90
"""DARKMAGENTA = rgb(135,0,135) <span style='background:#870087'>&nbsp;</span>"""
DARKMAGENTA = 91
"""DARKMAGENTA = rgb(135,0,175) <span style='background:#8700af'>&nbsp;</span>"""
DARKVIOLET = 92
"""DARKVIOLET = rgb(135,0,215) <span style='background:#8700d7'>&nbsp;</span>"""
PURPLE = 93
"""PURPLE = rgb(135,0,255) <span style='background:#8700ff'>&nbsp;</span>"""
ORANGE4 = 94
"""ORANGE4 = rgb(135,95,0) <span style='background:#875f00'>&nbsp;</span>"""
LIGHTPINK4 = 95
"""LIGHTPINK4 = rgb(135,95,95) <span style='background:#875f5f'>&nbsp;</span>"""
PLUM4 = 96
"""PLUM4 = rgb(135,95,135) <span style='background:#875f87'>&nbsp;</span>"""
MEDIUMPURPLE3 = 97
"""MEDIUMPURPLE3 = rgb(135,95,175) <span style='background:#875faf'>&nbsp;</span>"""
MEDIUMPURPLE3 = 98
"""MEDIUMPURPLE3 = rgb(135,95,215) <span style='background:#875fd7'>&nbsp;</span>"""
SLATEBLUE1 = 99
"""SLATEBLUE1 = rgb(135,95,255) <span style='background:#875fff'>&nbsp;</span>"""
YELLOW4 = 100
"""YELLOW4 = rgb(135,135,0) <span style='background:#878700'>&nbsp;</span>"""
WHEAT4 = 101
"""WHEAT4 = rgb(135,135,95) <span style='background:#87875f'>&nbsp;</span>"""
GREY53 = 102
"""GREY53 = rgb(135,135,135) <span style='background:#878787'>&nbsp;</span>"""
LIGHTSLATEGREY = 103
"""LIGHTSLATEGREY = rgb(135,135,175) <span style='background:#8787af'>&nbsp;</span>"""
MEDIUMPURPLE = 104
"""MEDIUMPURPLE = rgb(135,135,215) <span style='background:#8787d7'>&nbsp;</span>"""
LIGHTSLATEBLUE = 105
"""LIGHTSLATEBLUE = rgb(135,135,255) <span style='background:#8787ff'>&nbsp;</span>"""
YELLOW4 = 106
"""YELLOW4 = rgb(135,175,0) <span style='background:#87af00'>&nbsp;</span>"""
DARKOLIVEGREEN3 = 107
"""DARKOLIVEGREEN3 = rgb(135,175,95) <span style='background:#87af5f'>&nbsp;</span>"""
DARKSEAGREEN = 108
"""DARKSEAGREEN = rgb(135,175,135) <span style='background:#87af87'>&nbsp;</span>"""
LIGHTSKYBLUE3 = 109
"""LIGHTSKYBLUE3 = rgb(135,175,175) <span style='background:#87afaf'>&nbsp;</span>"""
LIGHTSKYBLUE3 = 110
"""LIGHTSKYBLUE3 = rgb(135,175,215) <span style='background:#87afd7'>&nbsp;</span>"""
SKYBLUE2 = 111
"""SKYBLUE2 = rgb(135,175,255) <span style='background:#87afff'>&nbsp;</span>"""
CHARTREUSE2 = 112
"""CHARTREUSE2 = rgb(135,215,0) <span style='background:#87d700'>&nbsp;</span>"""
DARKOLIVEGREEN3 = 113
"""DARKOLIVEGREEN3 = rgb(135,215,95) <span style='background:#87d75f'>&nbsp;</span>"""
PALEGREEN3 = 114
"""PALEGREEN3 = rgb(135,215,135) <span style='background:#87d787'>&nbsp;</span>"""
DARKSEAGREEN3 = 115
"""DARKSEAGREEN3 = rgb(135,215,175) <span style='background:#87d7af'>&nbsp;</span>"""
DARKSLATEGRAY3 = 116
"""DARKSLATEGRAY3 = rgb(135,215,215) <span style='background:#87d7d7'>&nbsp;</span>"""
SKYBLUE1 = 117
"""SKYBLUE1 = rgb(135,215,255) <span style='background:#87d7ff'>&nbsp;</span>"""
CHARTREUSE1 = 118
"""CHARTREUSE1 = rgb(135,255,0) <span style='background:#87ff00'>&nbsp;</span>"""
LIGHTGREEN = 119
"""LIGHTGREEN = rgb(135,255,95) <span style='background:#87ff5f'>&nbsp;</span>"""
LIGHTGREEN = 120
"""LIGHTGREEN = rgb(135,255,135) <span style='background:#87ff87'>&nbsp;</span>"""
PALEGREEN1 = 121
"""PALEGREEN1 = rgb(135,255,175) <span style='background:#87ffaf'>&nbsp;</span>"""
AQUAMARINE1 = 122
"""AQUAMARINE1 = rgb(135,255,215) <span style='background:#87ffd7'>&nbsp;</span>"""
DARKSLATEGRAY1 = 123
"""DARKSLATEGRAY1 = rgb(135,255,255) <span style='background:#87ffff'>&nbsp;</span>"""
RED3 = 124
"""RED3 = rgb(175,0,0) <span style='background:#af0000'>&nbsp;</span>"""
DEEPPINK4 = 125
"""DEEPPINK4 = rgb(175,0,95) <span style='background:#af005f'>&nbsp;</span>"""
MEDIUMVIOLETRED = 126
"""MEDIUMVIOLETRED = rgb(175,0,135) <span style='background:#af0087'>&nbsp;</span>"""
MAGENTA3 = 127
"""MAGENTA3 = rgb(175,0,175) <span style='background:#af00af'>&nbsp;</span>"""
DARKVIOLET = 128
"""DARKVIOLET = rgb(175,0,215) <span style='background:#af00d7'>&nbsp;</span>"""
PURPLE = 129
"""PURPLE = rgb(175,0,255) <span style='background:#af00ff'>&nbsp;</span>"""
DARKORANGE3 = 130
"""DARKORANGE3 = rgb(175,95,0) <span style='background:#af5f00'>&nbsp;</span>"""
INDIANRED = 131
"""INDIANRED = rgb(175,95,95) <span style='background:#af5f5f'>&nbsp;</span>"""
HOTPINK3 = 132
"""HOTPINK3 = rgb(175,95,135) <span style='background:#af5f87'>&nbsp;</span>"""
MEDIUMORCHID3 = 133
"""MEDIUMORCHID3 = rgb(175,95,175) <span style='background:#af5faf'>&nbsp;</span>"""
MEDIUMORCHID = 134
"""MEDIUMORCHID = rgb(175,95,215) <span style='background:#af5fd7'>&nbsp;</span>"""
MEDIUMPURPLE2 = 135
"""MEDIUMPURPLE2 = rgb(175,95,255) <span style='background:#af5fff'>&nbsp;</span>"""
DARKGOLDENROD = 136
"""DARKGOLDENROD = rgb(175,135,0) <span style='background:#af8700'>&nbsp;</span>"""
LIGHTSALMON3 = 137
"""LIGHTSALMON3 = rgb(175,135,95) <span style='background:#af875f'>&nbsp;</span>"""
ROSYBROWN = 138
"""ROSYBROWN = rgb(175,135,135) <span style='background:#af8787'>&nbsp;</span>"""
GREY63 = 139
"""GREY63 = rgb(175,135,175) <span style='background:#af87af'>&nbsp;</span>"""
MEDIUMPURPLE2 = 140
"""MEDIUMPURPLE2 = rgb(175,135,215) <span style='background:#af87d7'>&nbsp;</span>"""
MEDIUMPURPLE1 = 141
"""MEDIUMPURPLE1 = rgb(175,135,255) <span style='background:#af87ff'>&nbsp;</span>"""
GOLD3 = 142
"""GOLD3 = rgb(175,175,0) <span style='background:#afaf00'>&nbsp;</span>"""
DARKKHAKI = 143
"""DARKKHAKI = rgb(175,175,95) <span style='background:#afaf5f'>&nbsp;</span>"""
NAVAJOWHITE3 = 144
"""NAVAJOWHITE3 = rgb(175,175,135) <span style='background:#afaf87'>&nbsp;</span>"""
GREY69 = 145
"""GREY69 = rgb(175,175,175) <span style='background:#afafaf'>&nbsp;</span>"""
LIGHTSTEELBLUE3 = 146
"""LIGHTSTEELBLUE3 = rgb(175,175,215) <span style='background:#afafd7'>&nbsp;</span>"""
LIGHTSTEELBLUE = 147
"""LIGHTSTEELBLUE = rgb(175,175,255) <span style='background:#afafff'>&nbsp;</span>"""
YELLOW3 = 148
"""YELLOW3 = rgb(175,215,0) <span style='background:#afd700'>&nbsp;</span>"""
DARKOLIVEGREEN3 = 149
"""DARKOLIVEGREEN3 = rgb(175,215,95) <span style='background:#afd75f'>&nbsp;</span>"""
DARKSEAGREEN3 = 150
"""DARKSEAGREEN3 = rgb(175,215,135) <span style='background:#afd787'>&nbsp;</span>"""
DARKSEAGREEN2 = 151
"""DARKSEAGREEN2 = rgb(175,215,175) <span style='background:#afd7af'>&nbsp;</span>"""
LIGHTCYAN3 = 152
"""LIGHTCYAN3 = rgb(175,215,215) <span style='background:#afd7d7'>&nbsp;</span>"""
LIGHTSKYBLUE1 = 153
"""LIGHTSKYBLUE1 = rgb(175,215,255) <span style='background:#afd7ff'>&nbsp;</span>"""
GREENYELLOW = 154
"""GREENYELLOW = rgb(175,255,0) <span style='background:#afff00'>&nbsp;</span>"""
DARKOLIVEGREEN2 = 155
"""DARKOLIVEGREEN2 = rgb(175,255,95) <span style='background:#afff5f'>&nbsp;</span>"""
PALEGREEN1 = 156
"""PALEGREEN1 = rgb(175,255,135) <span style='background:#afff87'>&nbsp;</span>"""
DARKSEAGREEN2 = 157
"""DARKSEAGREEN2 = rgb(175,255,175) <span style='background:#afffaf'>&nbsp;</span>"""
DARKSEAGREEN1 = 158
"""DARKSEAGREEN1 = rgb(175,255,215) <span style='background:#afffd7'>&nbsp;</span>"""
PALETURQUOISE1 = 159
"""PALETURQUOISE1 = rgb(175,255,255) <span style='background:#afffff'>&nbsp;</span>"""
RED3 = 160
"""RED3 = rgb(215,0,0) <span style='background:#d70000'>&nbsp;</span>"""
DEEPPINK3 = 161
"""DEEPPINK3 = rgb(215,0,95) <span style='background:#d7005f'>&nbsp;</span>"""
DEEPPINK3 = 162
"""DEEPPINK3 = rgb(215,0,135) <span style='background:#d70087'>&nbsp;</span>"""
MAGENTA3 = 163
"""MAGENTA3 = rgb(215,0,175) <span style='background:#d700af'>&nbsp;</span>"""
MAGENTA3 = 164
"""MAGENTA3 = rgb(215,0,215) <span style='background:#d700d7'>&nbsp;</span>"""
MAGENTA2 = 165
"""MAGENTA2 = rgb(215,0,255) <span style='background:#d700ff'>&nbsp;</span>"""
DARKORANGE3 = 166
"""DARKORANGE3 = rgb(215,95,0) <span style='background:#d75f00'>&nbsp;</span>"""
INDIANRED = 167
"""INDIANRED = rgb(215,95,95) <span style='background:#d75f5f'>&nbsp;</span>"""
HOTPINK3 = 168
"""HOTPINK3 = rgb(215,95,135) <span style='background:#d75f87'>&nbsp;</span>"""
HOTPINK2 = 169
"""HOTPINK2 = rgb(215,95,175) <span style='background:#d75faf'>&nbsp;</span>"""
ORCHID = 170
"""ORCHID = rgb(215,95,215) <span style='background:#d75fd7'>&nbsp;</span>"""
MEDIUMORCHID1 = 171
"""MEDIUMORCHID1 = rgb(215,95,255) <span style='background:#d75fff'>&nbsp;</span>"""
ORANGE3 = 172
"""ORANGE3 = rgb(215,135,0) <span style='background:#d78700'>&nbsp;</span>"""
LIGHTSALMON3 = 173
"""LIGHTSALMON3 = rgb(215,135,95) <span style='background:#d7875f'>&nbsp;</span>"""
LIGHTPINK3 = 174
"""LIGHTPINK3 = rgb(215,135,135) <span style='background:#d78787'>&nbsp;</span>"""
PINK3 = 175
"""PINK3 = rgb(215,135,175) <span style='background:#d787af'>&nbsp;</span>"""
PLUM3 = 176
"""PLUM3 = rgb(215,135,215) <span style='background:#d787d7'>&nbsp;</span>"""
VIOLET = 177
"""VIOLET = rgb(215,135,255) <span style='background:#d787ff'>&nbsp;</span>"""
GOLD3 = 178
"""GOLD3 = rgb(215,175,0) <span style='background:#d7af00'>&nbsp;</span>"""
LIGHTGOLDENROD3 = 179
"""LIGHTGOLDENROD3 = rgb(215,175,95) <span style='background:#d7af5f'>&nbsp;</span>"""
TAN = 180
"""TAN = rgb(215,175,135) <span style='background:#d7af87'>&nbsp;</span>"""
MISTYROSE3 = 181
"""MISTYROSE3 = rgb(215,175,175) <span style='background:#d7afaf'>&nbsp;</span>"""
THISTLE3 = 182
"""THISTLE3 = rgb(215,175,215) <span style='background:#d7afd7'>&nbsp;</span>"""
PLUM2 = 183
"""PLUM2 = rgb(215,175,255) <span style='background:#d7afff'>&nbsp;</span>"""
YELLOW3 = 184
"""YELLOW3 = rgb(215,215,0) <span style='background:#d7d700'>&nbsp;</span>"""
KHAKI3 = 185
"""KHAKI3 = rgb(215,215,95) <span style='background:#d7d75f'>&nbsp;</span>"""
LIGHTGOLDENROD2 = 186
"""LIGHTGOLDENROD2 = rgb(215,215,135) <span style='background:#d7d787'>&nbsp;</span>"""
LIGHTYELLOW3 = 187
"""LIGHTYELLOW3 = rgb(215,215,175) <span style='background:#d7d7af'>&nbsp;</span>"""
GREY84 = 188
"""GREY84 = rgb(215,215,215) <span style='background:#d7d7d7'>&nbsp;</span>"""
LIGHTSTEELBLUE1 = 189
"""LIGHTSTEELBLUE1 = rgb(215,215,255) <span style='background:#d7d7ff'>&nbsp;</span>"""
YELLOW2 = 190
"""YELLOW2 = rgb(215,255,0) <span style='background:#d7ff00'>&nbsp;</span>"""
DARKOLIVEGREEN1 = 191
"""DARKOLIVEGREEN1 = rgb(215,255,95) <span style='background:#d7ff5f'>&nbsp;</span>"""
DARKOLIVEGREEN1 = 192
"""DARKOLIVEGREEN1 = rgb(215,255,135) <span style='background:#d7ff87'>&nbsp;</span>"""
DARKSEAGREEN1 = 193
"""DARKSEAGREEN1 = rgb(215,255,175) <span style='background:#d7ffaf'>&nbsp;</span>"""
HONEYDEW2 = 194
"""HONEYDEW2 = rgb(215,255,215) <span style='background:#d7ffd7'>&nbsp;</span>"""
LIGHTCYAN1 = 195
"""LIGHTCYAN1 = rgb(215,255,255) <span style='background:#d7ffff'>&nbsp;</span>"""
RED1 = 196
"""RED1 = rgb(255,0,0) <span style='background:#ff0000'>&nbsp;</span>"""
DEEPPINK2 = 197
"""DEEPPINK2 = rgb(255,0,95) <span style='background:#ff005f'>&nbsp;</span>"""
DEEPPINK1 = 198
"""DEEPPINK1 = rgb(255,0,135) <span style='background:#ff0087'>&nbsp;</span>"""
DEEPPINK1 = 199
"""DEEPPINK1 = rgb(255,0,175) <span style='background:#ff00af'>&nbsp;</span>"""
MAGENTA2 = 200
"""MAGENTA2 = rgb(255,0,215) <span style='background:#ff00d7'>&nbsp;</span>"""
MAGENTA1 = 201
"""MAGENTA1 = rgb(255,0,255) <span style='background:#ff00ff'>&nbsp;</span>"""
ORANGERED1 = 202
"""ORANGERED1 = rgb(255,95,0) <span style='background:#ff5f00'>&nbsp;</span>"""
INDIANRED1 = 203
"""INDIANRED1 = rgb(255,95,95) <span style='background:#ff5f5f'>&nbsp;</span>"""
INDIANRED1 = 204
"""INDIANRED1 = rgb(255,95,135) <span style='background:#ff5f87'>&nbsp;</span>"""
HOTPINK = 205
"""HOTPINK = rgb(255,95,175) <span style='background:#ff5faf'>&nbsp;</span>"""
HOTPINK = 206
"""HOTPINK = rgb(255,95,215) <span style='background:#ff5fd7'>&nbsp;</span>"""
MEDIUMORCHID1 = 207
"""MEDIUMORCHID1 = rgb(255,95,255) <span style='background:#ff5fff'>&nbsp;</span>"""
DARKORANGE = 208
"""DARKORANGE = rgb(255,135,0) <span style='background:#ff8700'>&nbsp;</span>"""
SALMON1 = 209
"""SALMON1 = rgb(255,135,95) <span style='background:#ff875f'>&nbsp;</span>"""
LIGHTCORAL = 210
"""LIGHTCORAL = rgb(255,135,135) <span style='background:#ff8787'>&nbsp;</span>"""
PALEVIOLETRED1 = 211
"""PALEVIOLETRED1 = rgb(255,135,175) <span style='background:#ff87af'>&nbsp;</span>"""
ORCHID2 = 212
"""ORCHID2 = rgb(255,135,215) <span style='background:#ff87d7'>&nbsp;</span>"""
ORCHID1 = 213
"""ORCHID1 = rgb(255,135,255) <span style='background:#ff87ff'>&nbsp;</span>"""
ORANGE1 = 214
"""ORANGE1 = rgb(255,175,0) <span style='background:#ffaf00'>&nbsp;</span>"""
SANDYBROWN = 215
"""SANDYBROWN = rgb(255,175,95) <span style='background:#ffaf5f'>&nbsp;</span>"""
LIGHTSALMON1 = 216
"""LIGHTSALMON1 = rgb(255,175,135) <span style='background:#ffaf87'>&nbsp;</span>"""
LIGHTPINK1 = 217
"""LIGHTPINK1 = rgb(255,175,175) <span style='background:#ffafaf'>&nbsp;</span>"""
PINK1 = 218
"""PINK1 = rgb(255,175,215) <span style='background:#ffafd7'>&nbsp;</span>"""
PLUM1 = 219
"""PLUM1 = rgb(255,175,255) <span style='background:#ffafff'>&nbsp;</span>"""
GOLD1 = 220
"""GOLD1 = rgb(255,215,0) <span style='background:#ffd700'>&nbsp;</span>"""
LIGHTGOLDENROD2 = 221
"""LIGHTGOLDENROD2 = rgb(255,215,95) <span style='background:#ffd75f'>&nbsp;</span>"""
LIGHTGOLDENROD2 = 222
"""LIGHTGOLDENROD2 = rgb(255,215,135) <span style='background:#ffd787'>&nbsp;</span>"""
NAVAJOWHITE1 = 223
"""NAVAJOWHITE1 = rgb(255,215,175) <span style='background:#ffd7af'>&nbsp;</span>"""
MISTYROSE1 = 224
"""MISTYROSE1 = rgb(255,215,215) <span style='background:#ffd7d7'>&nbsp;</span>"""
THISTLE1 = 225
"""THISTLE1 = rgb(255,215,255) <span style='background:#ffd7ff'>&nbsp;</span>"""
YELLOW1 = 226
"""YELLOW1 = rgb(255,255,0) <span style='background:#ffff00'>&nbsp;</span>"""
LIGHTGOLDENROD1 = 227
"""LIGHTGOLDENROD1 = rgb(255,255,95) <span style='background:#ffff5f'>&nbsp;</span>"""
KHAKI1 = 228
"""KHAKI1 = rgb(255,255,135) <span style='background:#ffff87'>&nbsp;</span>"""
WHEAT1 = 229
"""WHEAT1 = rgb(255,255,175) <span style='background:#ffffaf'>&nbsp;</span>"""
CORNSILK1 = 230
"""CORNSILK1 = rgb(255,255,215) <span style='background:#ffffd7'>&nbsp;</span>"""
GREY100 = 231
"""GREY100 = rgb(255,255,255) <span style='background:#ffffff'>&nbsp;</span>"""
GREY3 = 232
"""GREY3 = rgb(8,8,8) <span style='background:#080808'>&nbsp;</span>"""
GREY7 = 233
"""GREY7 = rgb(18,18,18) <span style='background:#121212'>&nbsp;</span>"""
GREY11 = 234
"""GREY11 = rgb(28,28,28) <span style='background:#1c1c1c'>&nbsp;</span>"""
GREY15 = 235
"""GREY15 = rgb(38,38,38) <span style='background:#262626'>&nbsp;</span>"""
GREY19 = 236
"""GREY19 = rgb(48,48,48) <span style='background:#303030'>&nbsp;</span>"""
GREY23 = 237
"""GREY23 = rgb(58,58,58) <span style='background:#3a3a3a'>&nbsp;</span>"""
GREY27 = 238
"""GREY27 = rgb(68,68,68) <span style='background:#444444'>&nbsp;</span>"""
GREY30 = 239
"""GREY30 = rgb(78,78,78) <span style='background:#4e4e4e'>&nbsp;</span>"""
GREY35 = 240
"""GREY35 = rgb(88,88,88) <span style='background:#585858'>&nbsp;</span>"""
GREY39 = 241
"""GREY39 = rgb(98,98,98) <span style='background:#626262'>&nbsp;</span>"""
GREY42 = 242
"""GREY42 = rgb(108,108,108) <span style='background:#6c6c6c'>&nbsp;</span>"""
GREY46 = 243
"""GREY46 = rgb(118,118,118) <span style='background:#767676'>&nbsp;</span>"""
GREY50 = 244
"""GREY50 = rgb(128,128,128) <span style='background:#808080'>&nbsp;</span>"""
GREY54 = 245
"""GREY54 = rgb(138,138,138) <span style='background:#8a8a8a'>&nbsp;</span>"""
GREY58 = 246
"""GREY58 = rgb(148,148,148) <span style='background:#949494'>&nbsp;</span>"""
GREY62 = 247
"""GREY62 = rgb(158,158,158) <span style='background:#9e9e9e'>&nbsp;</span>"""
GREY66 = 248
"""GREY66 = rgb(168,168,168) <span style='background:#a8a8a8'>&nbsp;</span>"""
GREY70 = 249
"""GREY70 = rgb(178,178,178) <span style='background:#b2b2b2'>&nbsp;</span>"""
GREY74 = 250
"""GREY74 = rgb(188,188,188) <span style='background:#bcbcbc'>&nbsp;</span>"""
GREY78 = 251
"""GREY78 = rgb(198,198,198) <span style='background:#c6c6c6'>&nbsp;</span>"""
GREY82 = 252
"""GREY82 = rgb(208,208,208) <span style='background:#d0d0d0'>&nbsp;</span>"""
GREY85 = 253
"""GREY85 = rgb(218,218,218) <span style='background:#dadada'>&nbsp;</span>"""
GREY89 = 254
"""GREY89 = rgb(228,228,228) <span style='background:#e4e4e4'>&nbsp;</span>"""
GREY93 = 255
"""GREY93 = rgb(238,238,238) <span style='background:#eeeeee'>&nbsp;</span>"""
