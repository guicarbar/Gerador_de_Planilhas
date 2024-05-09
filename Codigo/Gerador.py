# Gerador avançado de banco de dados

# area dos imports

from random import randint

# area das funçoes

def dev():
    c = randint(1,100)

    if c > 1:
        return True
    elif c == 1:
        return False

def nascimento():
    dia = randint(1,30)
    mes = randint(1,12)
    ano = randint(1960, 2005)

    return dia + '/' + mes + '/' + ano

def produtos(c):
    alet = randint(1,10)
    
    if c == 'eletronicos':
        return eletronicos[alet - 1]
    elif c == 'higiene':
        return higiene[alet - 1]
    elif c == 'moveis':
        return moveis[alet - 1]
    elif c == 'jardinagem':
        return jardinagem[alet - 1]

def categorias():
    c = randint(1,4)
    
    if c == 1:
        return eletronicos
    elif c == 2:
        return higiene
    elif c == 3:
        return moveis
    elif c == 4:
        return jardinagem

def nomes(g):
    alet = randint(1,50)
    
    if g == 'M':
        return nomes_masculinos[alet - 1]
    elif g == 'F':
        return nomes_femininos[alet - 1]

def sobrenomes():
    alet = randint(1,100)
    return list_sobrenomes[alet - 1]
    
def sexo():
    alet = randint(1,2)
    
    if alet == 1:
        return genero[alet - 1]
    elif alet == 2:
        return genero[alet - 1]

def vendedores(v):
    alet = randint(1,5)
    
    if v == 'Osasco':
        return vendedores_osasco[alet - 1]
    elif v == 'Barueri':
        return vendedores_barueri[alet - 1]
    elif v == 'Pinheiros':
        return vendedores_pinheiros[alet - 1]
    elif v == 'Faria lima':
        return vendedores_farialima[alet - 1]
    elif v == 'Vila olimpia':
        return vendedores_vilaolimpia[alet - 1]
    elif v == 'Moema':
        return vendedores_moema[alet - 1]
    
def lojas():
    alet = randint(1,6)
    return list_lojas[alet - 1]

def x(h):
    if h == 'Credito':
        return randint(1,12)
    else:
        return 0 

def pagamentos():
    alet = randint(1,3)
    
    if alet == 1:
        return list_pagamento[alet - 1]
    elif alet == 2:
        return list_pagamento[alet - 1]
    elif alet == 3:
        return list_pagamento[alet - 1]

def compra():
    dia = randint(1,30)
    mes = randint(1,12)

    return dia + '/' + mes + '/2023'

# area das listas

# usuarios

genero = [
    'M', 'F'
]

nomes_masculinos = [
    "Lucas", "Pedro", "Mateus", "João", "Gabriel", "Matheus", "Guilherme", "Felipe", "Miguel", "Rafael",
    "Enzo", "Gustavo", "Leonardo", "Daniel", "Henrique", "Bruno", "Diego", "Thiago", "Vinicius", "Carlos",
    "Eduardo", "Antônio", "Alexandre", "André", "Fernando", "Arthur", "Ricardo", "Paulo", "Luiz", "Marcelo",
    "José", "Diego", "Caio", "Igor", "Jorge", "Roberto", "Rodrigo", "Rafael", "Cristiano", "Hugo", "Anderson",
    "Francisco", "Israel", "Júlio", "Leandro", "Renato", "Sérgio", "Tomás", "Vitor", "William"
]

nomes_femininos = [
    "Maria", "Ana", "Juliana", "Mariana", "Camila", "Amanda", "Fernanda", "Carolina", "Isabela", "Patrícia",
    "Bianca", "Letícia", "Tatiane", "Jéssica", "Raquel", "Larissa", "Natália", "Vanessa", "Giovana", "Cristiane",
    "Débora", "Lívia", "Alice", "Clara", "Mirella", "Talita", "Aline", "Beatriz", "Laura", "Isabel", 
    "Priscila", "Michele", "Renata", "Thaís", "Vitória", "Gabriela", "Helena", "Luana", "Sabrina", "Valentina",
    "Evelyn", "Fátima", "Lorena", "Mônica", "Nathalia", "Olívia", "Rebeca", "Simone", "Tainá", "Wanessa"
]

list_sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Ferreira", "Almeida", "Costa", "Rodrigues", "Alves",
    "Martins", "Lima", "Gomes", "Carvalho", "Mendes", "Rocha", "Barbosa", "Fernandes", "Pinto", "Dias",
    "Castro", "Campos", "Cardoso", "Monteiro", "Teixeira", "Freitas", "Vieira", "Monteiro", "Nascimento", "Ribeiro",
    "Ramos", "Carneiro", "Melo", "Araújo", "Moreira", "Gonçalves", "Nunes", "Coelho", "Correia", "Cunha",
    "Sousa", "Moura", "Antunes", "Marques", "Viana", "Dantas", "Cavalcanti", "Fonseca", "Correia", "Lopes",
    "Diniz", "Tavares", "Borges", "Reis", "Barros", "Figueiredo", "Magalhães", "Jesus", "Lemos", "Siqueira",
    "Aragão", "Abreu", "Macedo", "Vargas", "Brito", "Rosa", "Neves", "Pacheco", "Peixoto", "Guimarães",
    "Fogaça", "Marinho", "Fagundes", "Moraes", "Caldeira", "Vasconcelos", "Lira", "Coutinho", "Vidal", "Gurgel",
    "Xavier", "Assis", "Braga", "Rangel", "Sales", "Farias", "Cavalcante", "Bessa", "Franco", "Abreu",
    "Machado", "Amorim", "Miranda", "Gusmão", "Pontes", "Domingues", "Afonso", "Leal", "Ortega", "Castanho"
]

# produtos - são 4 tipos de produtos - cada tipo com 10 produtos

categorias_produtos = [
    'eletronicos', 'higiene', 'moveis', 'jardinagem'
]

eletronicos = [
    "Smartphone", "Notebook", "Tablet", "Smartwatch", "Fone de ouvido sem fio", "Câmera digital", 
    "Televisão", "Console de videogame", "Impressora", "Roteador Wi-Fi"
]

higiene = [
    "Escova de dentes", "Pasta de dentes", "Enxaguante bucal", "Fio dental", "Sabonete", 
    "Shampoo", "Condicionador", "Desodorante", "Papel higiênico", "Hidratante corporal"
]

moveis = [
    "Sofá", "Cama", "Mesa de jantar", "Cadeira", "Guarda-roupa", 
    "Escrivaninha", "Cômoda", "Rack", "Poltrona", "Mesa de centro"
]

jardinagem = [
    "Pá de jardim", "Ancinho", "Tesoura de poda", "Regador", "Luvas de jardinagem", 
    "Vasos", "Fertilizante", "Terra vegetal", "Tela de sombreamento", "Triturador de galhos"
]

# lojas - sao 6 lojas - cada uma com 5 vendedores

list_lojas = [
    'Osasco', 'Barueri', 'Faria lima', 'Moema', 'Vila olimpia', 'Pinheiros'
]

vendedores_osasco = ["Ana", "Carlos", "Mariana", "João", "Luciana"]

vendedores_barueri = ["Bruno", "Juliana", "Pedro", "Laura", "Rafael"]

vendedores_farialima = ["Camila", "Ricardo", "Fernanda", "André", "Patrícia"]

vendedores_moema = ["Gustavo", "Tatiane", "Paulo", "Carla", "Rodrigo"]

vendedores_vilaolimpia = ["Fernando", "Mariana", "Lucas", "Aline", "Rafaela"]

vendedores_pinheiros = ["Cristiano", "Isabela", "Daniel", "Marcela", "José"]


# formas de pagamento - se for credito ele vai poder parcelar em ate 12x

list_pagamento = [
    'Credito', 'Debito', 'Pix'
]

# codigo

categoria = categorias()
produto = produtos(categoria) 
devolucao = dev()
idade = nascimento()
genero = sexo()
nome = nomes(genero)
sobrenome = sobrenomes()
ultimo_nome = sobrenomes()
loja = lojas()
vendedor = vendedores(loja)
pagamento = pagamentos()
vezes = x(pagamento)
data = compra()
quantidade = randint(1,6)
preco = 