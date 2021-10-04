"""
ante las posibles consecuencias del referendum del brexit 
escriba un programa que permita convertir unidades de volumen
de liquidos. concretamente el progrma debe convertir 
litros en galones y pintas y viceversa

1 litro = 2.6417 galones
1 litro = 2.11338 pintas
1 galon = 3.785 litros
1 galon = 8 pintas
1 pinta = 0.57 litros
1 pinta = 0.125 galones
"""
uLiquido = 0
litros = 0
galones = 0
pintas = 0

uLiquido = float(input("Unidad de volumen de liquido que desea convertir: "))

opc = int(input("""
      Digite el numero segun corresponda:
      1. Si desea convertir de Litros a Galones
      2. Si desea convertir de Litros a Pintas
      3. Si desea convertir de Galones a Litros
      4. Si desea convertir de Galones a Pintas
      5. Si desea convertir de Pintas a Litros
      6. Si desea convertir de Pintas a Galones
      """))


if opc == 1:
    galones = uLiquido*2.6417
    print(uLiquido, " litros equivalen a ", galones, " galones")
elif opc == 2:
    pintas = uLiquido*2.11338
    print(uLiquido, " litros equivalen a ", pintas, " pintas")
elif opc == 3:
    litros = 3.7854118*uLiquido
    print(uLiquido, " galones equivalen a ", litros, " litros")
elif opc == 4:
    pintas = uLiquido*8
    print(uLiquido, " galones equivalen a ", pintas, " pintas")
elif opc == 5:
    litros = 0.57*uLiquido
    print(uLiquido, " pintas equivalen a ", litros, "  litros")
elif opc == 6:
    galones = uLiquido*0.125
    print(uLiquido, " pintas equivalen a ", galones, " galones")
else:
    print("Digite un numero")
