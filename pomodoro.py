import datetime, time, random, os, playsound

hr_ligou = datetime.datetime.now()
frases_motivacionais = [
    'seu maior problema é vc',
    'o fracasso é sempre uma opção',
    'melhor professor, o fracasso é',
    'nem tente',
    'sem lutas não há derrotas',
    'o segredo do fracasso é começar',
    'tudo vai dar errado',
    'trabalhe com oq vc ama e nunca mais amará nada',
    'bom dia caralho',
    'não construa seus sonhos, construa seus fracassos',
    'nunca é tarde para desistir',
    'nada é em vão, tudo vem pra te derrotar',
    'o esforço é grande mas o fracasso é certo',
    'pequenas batalhas, grandes derrotas',
    'a vida te derruba hoje te preparando para a queda de amanhã',
    'caia sete vezes, levante-se zero',
    'você não pode mudar o seu passado, mas pode estragar o seu futuro'
]
local_audios = __file__.strip('main.py') + 'audios'
audios = [audio for audio in os.listdir(local_audios) if audio.endswith('.mp3')]
i = 1
while i < 5:
    time.sleep(1)
    hr_atual = datetime.datetime.now()
    if hr_atual.hour == hr_ligou.hour + i and hr_atual.minute == hr_ligou.minute:
        for _ in range(2):
            playsound.playsound(local_audios + '/' + audios[random.randint(0, (len(audios) - 1))])
        i += 1
        time.sleep(900)
        print(frases_motivacionais[random.randint(0, (len(frases_motivacionais) - 1))])
        a = input('aperta enter nessa porra: ')
        for _ in range(2):
            playsound.playsound(local_audios + '/' + audios[random.randint(0, (len(audios) - 1))])
