import re
# ------------------------------------------------------------------------------

hotkey_lut = {
    'alt': '<Alt>',
    'cmd': '<Super>',
    'command': '<Super>',
    'control': '<Ctrl>',
    'ctrl': '<Ctrl>',
    'meta': '<Meta>',
    'primary': '<Primary>',
    'print': 'Print',
    'prnt': 'Print',
    'shft': '<Shift>',
    'shift': '<Shift>',
    'super': '<Super>',
    'win': '<Super>',
    'windows': '<Super>',
    'ent': 'Enter',
    'enter': 'Enter',
    'ret': 'Return',
    'return': 'Return',
    'escape': 'Escape',
    'esc': 'Escape',
    'end': 'End',
    'f1': 'F1',
    'f2': 'F2',
    'f3': 'F3',
    'f4': 'F4',
    'f5': 'F5',
    'f6': 'F6',
    'f7': 'F7',
    'f8': 'F8',
    'f9': 'F9',
    'f10': 'F10',
    'f11': 'F11',
    'f12': 'F12',
    'f13': 'F13',
    'f14': 'F14',
    'down': 'Down',
    'up': 'Up',
    'left': 'Left',
    'right': 'Right',
    'tab': 'Tab',
    'above-tab': 'Above_Tab',
    'page-down': 'Page_Down',
    'page-up': 'Page_Up',
    'home': 'Home',
    'xf86audioforward': 'XF86AudioForward',
    'xf86audiolowervolume': 'XF86AudioLowerVolume',
    'xf86audiomedia': 'XF86AudioMedia',
    'xf86audiomicmute': 'XF86AudioMicMute',
    'xf86audiomute': 'XF86AudioMute',
    'xf86audionext': 'XF86AudioNext',
    'xf86audiopause': 'XF86AudioPause',
    'xf86audioplay': 'XF86AudioPlay',
    'xf86audioprev': 'XF86AudioPrev',
    'xf86audioraisevolume': 'XF86AudioRaiseVolume',
    'xf86audiorandomplay': 'XF86AudioRandomPlay',
    'xf86audiorepeat': 'XF86AudioRepeat',
    'xf86audiorewind': 'XF86AudioRewind',
    'xf86audiostop': 'XF86AudioStop',
    'xf86battery': 'XF86Battery',
    'xf86bluetooth': 'XF86Bluetooth',
    'xf86calculator': 'XF86Calculator',
    'xf86eject': 'XF86Eject',
    'xf86explorer': 'XF86Explorer',
    'xf86hibernate': 'XF86Hibernate',
    'xf86kbdbrightnessdown': 'XF86KbdBrightnessDown',
    'xf86kbdbrightnessup': 'XF86KbdBrightnessUp',
    'xf86kbdlightonoff': 'XF86KbdLightOnOff',
    'xf86mail': 'XF86Mail',
    'xf86monbrightnesscycle': 'XF86MonBrightnessCycle',
    'xf86monbrightnessdown': 'XF86MonBrightnessDown',
    'xf86monbrightnessup': 'XF86MonBrightnessUp',
    'xf86poweroff': 'XF86PowerOff',
    'xf86rfkill': 'XF86RFKill',
    'xf86rotatewindows': 'XF86RotateWindows',
    'xf86screensaver': 'XF86ScreenSaver',
    'xf86search': 'XF86Search',
    'xf86sleep': 'XF86Sleep',
    'xf86suspend': 'XF86Suspend',
    'xf86tools': 'XF86Tools',
    'xf86touchpadoff': 'XF86TouchpadOff',
    'xf86touchpadon': 'XF86TouchpadOn',
    'xf86touchpadtoggle': 'XF86TouchpadToggle',
    'xf86uwb': 'XF86UWB',
    'xf86wlan': 'XF86WLAN',
    'xf86www': 'XF86WWW',
}


xkb_lut = {
    'alt-l': 'Alt_L',
    'alt-r': 'Alt_R',
    'alt': 'Alt_L',
    'caps-lock': 'Caps_Lock',
    'caps': 'Caps_Lock',
    'cmd-l': 'Super_L',
    'cmd-r': 'Super_R',
    'cmd': 'Super_L',
    'command-l': 'Super_L',
    'command-r': 'Super_R',
    'command': 'Super_L',
    'control-l': 'Control_L',
    'control-r': 'Control_R',
    'control': 'Control_L',
    'ctrl-l': 'Control_L',
    'ctrl-r': 'Control_R',
    'ctrl': 'Control_L',
    'meta-l': 'Meta_L',
    'meta-r': 'Meta_R',
    'meta': 'Meta_L',
    'primary-l': 'Control_L',
    'primary-r': 'Control_R',
    'primary': 'Control_L',
    'shft-l': 'Shift_L',
    'shft-r': 'Shift_R',
    'shft': 'Shift_L',
    'shift-l': 'Shift_L',
    'shift-r': 'Shift_R',
    'shift': 'Shift_L',
    'super-l': 'Super_L',
    'super-r': 'Super_R',
    'super': 'Super_L',
    'win-l': 'Super_L',
    'win-r': 'Super_R',
    'win': 'Super_L',
    'windows-l': 'Super_L',
    'windows-r': 'Super_R',
    'windows': 'Super_L',
}


def to_hotkeys(text, lut):
    hotkeys = re.split(r' *\+ *', text)
    output = ''
    for key in hotkeys:
        k = key.lower()
        if k in lut.keys():
            key = lut[k]
        output += key
    output = re.sub('^ *', '', output)
    return output


class FilterModule:
    def filters(self):
        return dict(
            to_hotkeys=lambda x: to_hotkeys(x, hotkey_lut),
            to_xkb_hotkeys=lambda x: to_hotkeys(x, xkb_lut),
        )