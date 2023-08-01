import PyPDF2


def csv_upload(csv):
    rows = csv_to_array(csv)
    json = array_to_json(rows)
    return json


def array_to_json(list):
    json = []
    for row in list:
        dict = {"name": row.split(',')[0], "value": row.split(',')[2],
                "lote_id": row.split(',')[1].rjust(4, '0'), "bar_code": row.split(',')[3]}
        json.append(dict)
        dict = {}
    return json


def csv_to_array(csv):
    string = csv.decode('utf-8').replace('\r', '')
    array = string.split('\n')
    array.pop(0)
    return array


def pdf_to_dict(pdf):
    array = pdf_to_string(pdf)
    json = string_to_json(array)
    return json


def pdf_to_string(pdf):
    with open("./app/temp/boleto_temp.pdf", "wb") as data:
        data.write(pdf)
    get_pdf = open("./app/temp/boleto_temp.pdf", "rb")
    read_pdf = PyPDF2.PdfFileReader(get_pdf)
    output = ''
    number_pages = read_pdf.numPages
    if read_pdf.isEncrypted:
        read_pdf.decrypt("")
        for i in range(number_pages):
            output += read_pdf.getPage(i).extract_text()

    else:
        for i in range(number_pages):
            output += read_pdf.getPage(i).extract_text()

    return output


def string_to_json(pdf):
    json = []
    auxiliar_dict = {}
    rows_splited = pdf.split('\n')
    for x in range(len(rows_splited)):
        if 'NOME:' in rows_splited[x]:
            if 'VALOR:' in rows_splited[x+3]:
                auxiliar_dict['name'] = f'{rows_splited[x+1]} {rows_splited[x+2]}'
            elif 'VALOR:' in rows_splited[x+4]:
                auxiliar_dict['name'] = f'{rows_splited[x+1]} {rows_splited[x+2]} {rows_splited[x+3]}'
        elif 'VALOR:' in rows_splited[x]:
            auxiliar_dict['value'] = float(rows_splited[x+1])
        elif 'DIGITAVEL:' in rows_splited[x]:
            auxiliar_dict['bar_code'] = f'{rows_splited[x+1]}'
        elif 'LOTE:' in rows_splited[x]:
            lote = int(rows_splited[x+1].split('PAGINA')[0])
            auxiliar_dict['lote_id'] = lote

            json.append(auxiliar_dict)
            auxiliar_dict = {}

    return json
