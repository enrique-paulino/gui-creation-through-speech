import speech_recognition as sr


def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Assistant is listening.')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
        command = listener()
    return command
