primeiro_ano = input('Digite um ano de nascimento: ')
segundo_ano = input('Digite outro ano de nascimento: ')


if primeiro_ano >= segundo_ano:
    print(
        f'{primeiro_ano=} é maior ou igual '
        f'ao que {segundo_ano=}'

    )

else:
    print(
        f'{segundo_ano=} é maior '
        f'que o {primeiro_ano=}'

    )
