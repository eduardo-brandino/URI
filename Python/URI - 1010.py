#https://www.beecrowd.com.br/judge/pt/problems/view/1010


a = input().split()
ca, qa, va = a
b = input().split()
cb, qb, vb = b

t = float(int(qa) * float(va) + int(qb) * float(vb))
print('VALOR A PAGAR: R$ {:.2f}'.format(t))
