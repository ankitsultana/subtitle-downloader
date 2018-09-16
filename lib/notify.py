from subprocess import call

def notify(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
    call(["osascript", "-e", "display notification \"" + info_text +
        "\" with title \"" + title +
        "\" subtitle \"" + subtitle +
        "\" sound name \"frog\""])

if __name__ == '__main__':
    notify("Test message", "Subtitle", "This message should appear instantly, with a sound", delay=1000, sound=True)
