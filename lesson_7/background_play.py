from machine import Pin, PWM, Timer
import time

buzzer = PWM(Pin(14))

pitches = {
    'C5':523,
    'D5':587,
    'E5':659,
    'F5':698,
    'G5':784,
    'A5':880,
    'B5':988,
    'S':0
}

melody = (
    ('E5',100),('S',100),('E5',100),('S',300),('E5',100),('S',300),
    ('C5',100),('S',100),('E5',100),('S',300),('G5',100)
)

tim = Timer(-1)
index = 0

def play(t):
    global melody, pitches, buzzer, tim, index
    if index > 10:
        buzzer.deinit()
    else:
        tone, tempo = melody[index]
        if tone == 'S':
            buzzer.duty(0)
        else:
            buzzer.duty(900)
            buzzer.freq(pitches[tone])
    
        index = index + 1
        tim.init(period=tempo, mode=Timer.ONE_SHOT, callback=play)
        
tim.init(period=1, mode=Timer.ONE_SHOT, callback=play)

