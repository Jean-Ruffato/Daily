import xlwt
from django.http import HttpResponse
from Funcionarios.models import Atividades, Projetos, User


def exportar_atividades(request):
    exportar = HttpResponse(content_type='application/ms-excel')
    exportar['Content-Disposition'] = 'attachment; filename="Atividades.xls"'

    work_book = xlwt.Workbook(encoding='utf-8')
    work_sheet = work_book.add_sheet('Atividades')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    colunas = ['Ticket', 'Início', 'Fim', 'Projeto', 'Atividade', 'Descrição', 'Status', 'Horas', 'Prazo',
               'Responsável', 'Prioridade']

    for col_num in range(len(colunas)):
        work_sheet.write(row_num, col_num, colunas[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Atividades.objects.all().values_list('ID', 'Inicio', 'Fim', 'Projeto', 'Atividade', 'Descricao', 'Status',
                                                'Horas', 'Prazo', 'Nome', 'Prioridade')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            work_sheet.write(row_num, col_num, row[col_num], font_style)

    work_book.save(exportar)
    return exportar


def exportar_projetos(request):
    exportar = HttpResponse(content_type='application/ms-excel')
    exportar['Content-Disposition'] = 'attachment; filename="Projetos.xls"'

    work_book = xlwt.Workbook(encoding='utf-8')
    work_sheet = work_book.add_sheet('Projetos')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    colunas = ['Projeto', 'Responsável', 'Prazo', 'Horas', 'Status', 'Descrição', 'Valor', 'Integrantes']

    for col_num in range(len(colunas)):
        work_sheet.write(row_num, col_num, colunas[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Projetos.objects.all().values_list('Projeto', 'Responsavel', 'Prazo', 'Horas', 'Status', 'Descricao',
                                              'Valor', 'Integrantes')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            work_sheet.write(row_num, col_num, row[col_num], font_style)

    work_book.save(exportar)
    return exportar


def exportar_usuarios(request):
    exportar = HttpResponse(content_type='application/ms-excel')
    exportar['Content-Disposition'] = 'attachment; filename="Usuarios.xls"'

    work_book = xlwt.Workbook(encoding='utf-8')
    work_sheet = work_book.add_sheet('Usuários')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    colunas = ['Último Login', 'Super Usuário', 'Usuário', 'Nome', 'Sobrenome', 'E-mail',
               'Administração', 'Ativo', 'Data de criação']

    for col_num in range(len(colunas)):
        work_sheet.write(row_num, col_num, colunas[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email',
                                          'is_staff', 'is_active', 'date_joined')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            work_sheet.write(row_num, col_num, row[col_num], font_style)

    work_book.save(exportar)
    return exportar
