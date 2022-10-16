def draw_square(width: int):
    print(f'{"*" * width}\n'
          f'*{" " * (width - 2)}*\n'
          f'*{" " * (width - 2)}*\n'
          f'{"*" * width}\n')
    # print('*********\n*       *\n*       *\n*********')


draw_square(9)
