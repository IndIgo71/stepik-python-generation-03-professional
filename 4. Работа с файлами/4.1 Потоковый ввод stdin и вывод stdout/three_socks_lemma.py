import sys

players = ['Анри', 'Дима']
socks = [int(sock) for sock in sys.stdin.readlines()]

last_sock_idx = len(socks) - 1
player_step = last_sock_idx % 2
if socks[last_sock_idx] % 2 == 0:
    sys.stdout.write(players[player_step])
else:
    sys.stdout.write(players[player_step - 1])
